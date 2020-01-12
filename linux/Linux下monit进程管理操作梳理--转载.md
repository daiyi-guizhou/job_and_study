

本文转自 (https://cloud.tencent.com/developer/article/1027097)
Monit对运维人员来说可谓神器，它是一款功能非常丰富的进程、文件、目录和设备的监测工具，用于Unix平台。它可以自动修复那些已经停止运作的程序，特使适合处理那些由于多种原因导致的软件错误。
Monit不但本地监控十分有效，还可以监控远程服务，只要花点功夫就能永远实现服务的“死而复生”，就是说它可以使它监控的服务程序在宕停后迅速自启动，不需要人工干预。绝对牛X的一款系统监控神奇！
比如下面两个场景：
1）持续邮件提醒
默认情况下，如果服务Down了，无论它持续Down了多久，Monit程序只会邮件提醒你一次。下一次提醒，就是服务恢复的时候。
如果希望，在多个周期内，即使服务状态没有变化（持续宕机着），也能收到邮件提醒，那么加上这句：
alert foo@bar with reminder on 10 cycles   此句表示，在10个周期内都会邮件提醒。

2）误报提醒解决
有些时候，Monit也会误报，这很正常，任何监控软件都会。大多数是由于网络状况不佳。比如某一个服务，Monit发现停了，又迅速启动了，那就不要来烦了，别总是一封邮件接着一封。这样设置：
if failed host 172.16.5.1 port 8599 for 3 times within 4 cycles then alert  这样就是:若在四个周期内，三次 8599（我的电驴口）端口都无法通，则邮件通知。很方便！

废话不多说，下面对monit监控环境的部署做一梳理：

需求说明：
随着线上服务器数量的增加，各种开源软件和工具的广泛使用，一些服务自动停止或无响应的情况时有发生，其中有很大一部分是由于软件自身的稳定性或者机器硬件资源限制而造成的。按道理来讲，这些情况都应该设法找到本质原因，然后避免再次出现。但现实是残酷的，不少软件本身的稳定性有待提升，机器的硬件资源提升会触及成本，因此在集群的环境中，具备冗余，使得执行简单的服务重启成为了最现实的选择。这本身不是什么困难的事情，实现的方法有很多，比如在Zabbix或Nagios的报警中增加Action或Commands，或自己写脚本放到计划任务中执行都可以。然而下面要介绍的就是专门来做这种事情的一个工具：Monit。它最大的特点是配置文件简单易读，同时支持进程和系统状态的监控，并灵活的提供了各种检测的方式，周期，并进行报警和响应（重启服务，执行命令等）

# Centos6下部署Monit环境过程：
### 1）安装EPEL仓库

```
[root@bastion-IDC src]# wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
[root@bastion-IDC src]# rpm -ivh epel-release-latest-6.noarch.rpm 
```


### 2）安装monit

```
[root@bastion-IDC src]#  yum install -y monit
```



--------------------------------------------------------------------------------------------------------------
源码安装包下载：https://mmonit.com/monit/dist/binary/

```
#wget https://mmonit.com/monit/dist/binary/5.20.0/monit-5.20.0-linux-x86.tar.gz
#tar -zvxf monit-5.20.0-linux-x86.tar.gz
#mv monit-5.20.0 /usr/local/monit
#cp /usr/local/monit/conf/monitrc /etc/
```
然后编辑配置文件/etc/monitrc即可。centos6的配置文件是monit.conf，centos7的配置文件是monitrc
### 3）monit配置说明（官网配置说明：https://mmonit.com/monit/documentation/monit.html）
Monit配置文件/etc/monit.conf，可以将默认配置文件备份下，然后自定义配置

```
[root@bastion-IDC src]# cp /etc/monit.conf /etc/monit.conf.bak
[root@bastion-IDC src]# cat /etc/monit.conf         //自定义配置如下
set daemon 120              #Poll at 2-minute intervals         //每2分钟检查一次，单位为秒；monit做不到实时监控。
set logfile /home/monit/log/monit.log                  //monit的日志文件
set alert zhouwei@chinabank.com.cn with reminder on 1 cycle //出现1次错误就发报警邮件到指定邮箱。多个邮箱地址就配置多行;with后的配置可以不加。
#set mailserver mail.tildeslash.com, mail.foo.bar port 10025, localhost with timeout 15 seconds
set mailserver 10.10.9.109             //设置邮件服务器
set httpd port 2812 and use address 10.10.8.2            //设置http监控页面的端口和ip
    allow localhost           #Allow localhost to connect        //允许本机访问
    allow 10.10.8.0/24            //允许此IP段访问
    allow admin:nishiwode      #Allow Basic Auth          //认证的用户名和密码
# all system               //平均负载.内存使用率,cpu使用率
check system 10.10.8.2
   if loadavg (1min) > 4 then alert
   if loadavg (5min) > 2 then alert
   if memory usage > 75% then alert
   if cpu usage (user) > 70% then alert
   if cpu usage (system) > 30% then alert
   if cpu usage (wait) > 20% then alert
# all disk                    //磁盘空间使用率
check device data with path /dev/sda2
   if space usage > 90% then alert
   if inode usage > 85% then alert
check device home with path /dev/sda3
   if space usage > 85% for 5 cycles then alert      //如果在5个监控周期内，space使用率超过85%就发报警邮件  
   if inode usage > 85% for 5 cycles then alert
# all rsync
#10.10.8.2
check process sshd with pidfile /var/run/sshd.pid        //监控ssh服务
   start program "/etc/init.d/sshd start"
   stop program "/etc/init.d/sshd stop"
   if failed host 127.0.0.1 port 22 protocol ssh then restart
   if 3 restarts within 5 cycles then timeout              //设置在5个监控周期内重启3次则超时，那么就不再监控这个服务程序

check process httpd with pidfile /var/run/httpd.pid       //监控http服务
   start program = "/etc/init.d/httpd start"
   stop program = "/etc/init.d/httpd stop"
   if failed host 127.0.0.1 port 80 protocol http then restart
   if 5 restarts within 5 cycles then timeout

check process web_lb with pidfile /data/v20/server/web_lb/httpd.pid     //监控自定义服务
   start program = "/data/v20/bin/lb.sh"                 //启动脚本
   stop  program = "/data/v20/bin/lb_stop.sh"         //停止脚本
   if failed host 10.10.8.2 port 16101 proto http then restart
   if failed host 10.10.8.2 port 16101 proto http for 5 times within 5 cycles then exec "/data/v20/bin/lb_pay.sh"
   if failed host 10.10.8.2 port 16102 type TCPSSL proto http then restart
   if failed host 10.10.8.2 port 16102 type TCPSSL proto http for 5 times within 5 cycles then exec "/data/v20/bin/lb_pay.sh
```




### 4）monit的启动（monit的默认端口是30000。最好在本地的/etc/hosts里面做下本机主机名的映射关系，将hostname映射到127.0.0.1）

```
[root@bastion-IDC src]# /etc/init.d/monit start/stop/reload/status/restart

[root@bastion-IDC ~]# monit -t                     //检测monit配置是否正确
[root@bastion-IDC ~]# monit reload              //重载monit配置
[root@bastion-IDC ~]# monit status             //查看monit进程监控情况
```




若启动monit的时候报错如下：

```
Cannot translate 'huanqiu_web2' to FQDN name -- Name or service not known
Generated unique Monit id af76cbce671f323782e09e0d114857fd and stored to '/root/.monit.id'
Reinitializing monit daemon
No daemon process found
```



解决办法：
在本机的/etc/hosts里面做下主机映射，即
127.0.0.1 huanqiu_web2

---------------------------------------------线上用过的一个配置------------------------------------------------

```
[root@huanqiu_web1 ~]# cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
127.0.0.1 huanqiu_web1
 
[root@huanqiu_web1 ~]# cat /etc/monit.conf
set daemon 30
set logfile syslog facility log_daemon
set pidfile /var/run/monit.pid
set httpd port 30000
use address 127.0.0.1
allow 127.0.0.1
 
check process nginx with pidfile /Data/app/nginx/logs/nginx.pid
        start program = "/Data/app/nginx/sbin/nginx"
        stop program = "/Data/app/nginx/sbin/nginx -s stop"
 
check process php-fpm with pidfile /Data/app/php5.6.26/var/run/php-fpm.pid 
       start program = "/Data/app/php5.6.26/sbin/php-fpm"
       stop program = "/bin/bash -c 'kill -s SIGTERM `ps -ef|grep /Data/app/php5.6.26/etc/php-fpm.conf|grep -v grep|awk -F" " '{print $2}'`'"

check process mysql with pidfile /Data/app/mysql5.1.57/var/dev-new-test.pid
       start program = "/Data/app/mysql5.1.57/bin/mysqld_safe --defaults-file=/Data/app/mysql5.1.57/my.cnf &"
       stop program = "/bin/bash -c 'kill -s SIGTERM `ps -ef|grep mysqld_safe|grep -v grep|awk -F" " '{print $2}'`'"

check process tomcat-7-admin-wls matching "/Data/app/tomcat-7-wls/conf"
        start program = "/Data/app/tomcat-7-wls/bin/startup.sh"
        stop program = "/bin/bash -c 'kill -s SIGTERM `ps -ef|grep /Data/app/tomcat-7-wls/conf|grep -v grep|awk -F" " '{print $2}'`'"
 
check process tomcat-7-wls matching "/Data/app/tomcat-7-wls/conf"
        start program = "/Data/app/tomcat-7-wls/bin/startup.sh"
        stop program = "/bin/bash -c 'kill -s SIGTERM `ps -ef|grep /Data/app/tomcat-7-wls/conf|grep -v grep|awk -F" " '{print $2}'`'"
 
check process tomcat-7 matching "/Data/app/tomcat-7/conf"
        start program = "/Data/app/tomcat-7/bin/startup.sh"
        stop program = "/bin/bash -c 'kill -s SIGTERM `ps -ef|grep /Data/app/tomcat-7/conf|grep -v grep|awk -F" " '{print $2}'`'"

check process tomcat-7-banshanbandao matching "/Data/app/tomcat-7-banshanbandao/conf"
        start program = "/Data/app/tomcat-7-banshanbandao/bin/startup.sh"
        stop program = "/bin/bash -c 'kill -s SIGTERM `ps -ef|grep /Data/app/tomcat-7-banshanbandao/conf|grep -v grep|awk -F" " '{print $2}'`'"

check process vpn matching "/etc/vpnc/vpnc-script"
        start program = "/bin/sh /bin/vpn_start"
        stop program = "/bin/bash -c 'kill -s SIGTERM `ps -ef|grep vpnc-script|grep -v grep|awk -F" " '{print $2}'`'"

[root@huanqiu_web1 ~]# monit -t
Control file syntax OK
[root@huanqiu_web1 ~]# /etc/init.d/monit start
Starting monit:                                            [  OK  ]
 
[root@huanqiu_web1 ~]# lsof -i:30000
COMMAND  PID USER   FD   TYPE     DEVICE SIZE/OFF NODE NAME
monit   6109 root    5u  IPv4 2438183462      0t0  TCP localhost:30000 (LISTEN)

[root@huanqiu_web1 ~]# monit reload
Reinitializing monit daemon
 
[root@huanqiu_web1 ~]# monit status
The Monit daemon 5.14 uptime: 8m 

Process 'nginx'
  status                            Running
  monitoring status                 Monitored
  pid                               499
  parent pid                        1
  uid                               0
  effective uid                     0
  gid                               0
  uptime                            28d 20h 17m 
  children                          8
  memory                            19.6 MB
  memory total                      381.6 MB
  memory percent                    0.0%
  memory percent total              0.5%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  data collected                    Wed, 22 Mar 2017 11:32:42

Process 'php-fpm'
  status                            Running
  monitoring status                 Monitored
  pid                               3153
  parent pid                        1
  uid                               0
  effective uid                     0
  gid                               0
  uptime                            43d 19h 26m 
  children                          16
  memory                            8.7 MB
  memory total                      352.3 MB
  memory percent                    0.0%
  memory percent total              0.5%
  cpu percent                       0.0%
  cpu percent total                 0.1%
  data collected                    Wed, 22 Mar 2017 11:32:42

Process 'mysql'
  status                            Running
  monitoring status                 Monitored
  pid                               46403
  parent pid                        46254
  uid                               500
  effective uid                     500
  gid                               500
  uptime                            93d 0h 34m 
  children                          0
  memory                            317.8 MB
  memory total                      317.8 MB
  memory percent                    0.4%
  memory percent total              0.4%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  data collected                    Wed, 22 Mar 2017 11:32:42

Process 'tomcat-7-admin-wls'
  status                            Running
  monitoring status                 Monitored
  pid                               34188
  parent pid                        1
  uid                               0
  effective uid                     0
  gid                               0
  uptime                            4d 19h 15m 
  children                          0
  memory                            803.6 MB
  memory total                      803.6 MB
  memory percent                    1.2%
  memory percent total              1.2%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  data collected                    Wed, 22 Mar 2017 11:32:42

Process 'tomcat-7-wls'
  status                            Running
  monitoring status                 Monitored
  pid                               34188
  parent pid                        1
  uid                               0
  effective uid                     0
  gid                               0
  uptime                            4d 19h 15m 
  children                          0
  memory                            803.6 MB
  memory total                      803.6 MB
  memory percent                    1.2%
  memory percent total              1.2%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  data collected                    Wed, 22 Mar 2017 11:32:42

Process 'tomcat-7'
  status                            Running
  monitoring status                 Monitored
  pid                               14524
  parent pid                        1
  uid                               0
  effective uid                     0
  gid                               0
  uptime                            5d 21h 43m 
  children                          0
  memory                            581.2 MB
  memory total                      581.2 MB
  memory percent                    0.9%
  memory percent total              0.9%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  data collected                    Wed, 22 Mar 2017 11:32:42

Process 'tomcat-7-banshanbandao'
  status                            Running
  monitoring status                 Monitored
  pid                               29217
  parent pid                        1
  uid                               0
  effective uid                     0
  gid                               0
  uptime                            117d 0h 35m 
  children                          0
  memory                            1.4 GB
  memory total                      1.4 GB
  memory percent                    2.1%
  memory percent total              2.1%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  data collected                    Wed, 22 Mar 2017 11:32:42

Process 'vpn'
  status                            Running
  monitoring status                 Monitored
  pid                               13774
  parent pid                        1
  uid                               0
  effective uid                     0
  gid                               0
  uptime                            1h 36m 
  children                          0
  memory                            2.4 MB
  memory total                      2.4 MB
  memory percent                    0.0%
  memory percent total              0.0%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  data collected                    Wed, 22 Mar 2017 11:32:42

System 'huanqiu_web1'
  status                            Running
  monitoring status                 Monitored
  load average                      [0.00] [0.04] [0.09]
  cpu                               0.6%us 0.1%sy 0.0%wa
  memory usage                      5.1 GB [8.0%]
  swap usage                        0 B [0.0%]
  data collected                    Wed, 22 Mar 2017 11:32:42

```



### 5）monit监控程序进程的方式
a）利用进程的pid文件进行监控：with pidfile
b）利用进程的关键字匹配方式进行监控: matching；可以使用“monit procmatch 进程名 CLI”来查找要匹配的唯一关键字
不管是pid文件里的pid号还是进程的关键字，都要求是唯一性的！必须是唯一的，如果matching匹配字段不唯一，那么监控无效！

下面罗列几个平时工作中常用的几个监控项：

```
[root@bastion-IDC ~]# cat /etc/monit.conf

set daemon 30
set logfile syslog facility log_daemon
set pidfile /var/run/monit.pid
set httpd port 30000
use address 127.0.0.1
allow 127.0.0.1
............
check process nginx with pidfile /usr/local/nginx/logs/nginx.pid
        start program = "/usr/local/nginx/sbin/nginx"
        stop program = "/usr/local/nginx/sbin/nginx -s stop"

check process nginx with pidfile /webserver/nginx/run/nginx.pid 
        start program = "/webserver/init.d/nginx start" with timeout 10 seconds 
        stop program = "/webserver/init.d/nginx stop" 
        if failed host heylinux.com port 80 protocol http with timeout 10 seconds then restart 
        if 3 restarts within 5 cycles then timeout group webserver

check process php-fpm with pidfile /var/run/php-fpm/php-fpm.pid
       start program = "/etc/init.d/php-fpm start"
       stop program = "/etc/init.d/php-fpm stop"

check process mysqld  with pidfile "/letv/mysql2/data/cdn.oss.letv.com.pid"
       start program = "/etc/init.d/mysqld start"
       stop program = "/etc/init.d/mysqld stop"
       if failed host 127.0.0.1 port 3306 then restart

check process mysql with pidfile /webserver/mysql/run/mysqld.pid 
       start program = "/webserver/init.d/mysqld start" with timeout 10 seconds 
       stop program = "/webserver/init.d/mysqld stop" 
       if failed port 3307 protocol mysql with timeout 10 seconds then restart 
       if 3 restarts within 5 cycles then timeout group webserver

check process memcached with pidfile "/var/run/memcached/memcached.pid"
       start program = "/etc/init.d/memcached start"
       stop program = "/etc/init.d/memcached stop"
       if failed host 127.0.0.1 port 11211 protocol memcache then restart

check process zabbix    with pidfile "/usr/local/zabbix/zabbix_agentd.pid"
        start program = "/usr/local/zabbix/sbin/zabbix_agentd -c /usr/local/zabbix/conf/zabbix_agentd.conf"
        stop program = "/bin/bash -c 'kill -s SIGTERM `cat /usr/local/zabbix/zabbix_agentd.pid`'"
        if failed host 127.0.0.1 port 10050 type tcp 2 times within 2 cycles then restart

check process httpd
        with pidfile "/usr/local/apache/logs/httpd.pid"
        start program = "/usr/local/apache/bin/httpd -k start"
        stop  program = "/bin/bash -c 'kill -s SIGTERM `cat /usr/local/apache/logs/httpd.pid`'"

check process redis
        with pidfile "/var/run/redis.pid"
        start program = "/usr/local/bin/redis-server /letv/uss/redis/redis.conf"
        stop  program = "/bin/bash -c 'kill -s SIGTERM `cat /var/run/redis.pid`'"

check process rsync with pidfile "/var/run/rsyncd.pid"
        start program = "/usr/bin/rsync --daemon"
        stop program = "/bin/bash -c 'kill -s SIGTERM `cat /var/run/rsyncd.pid`'"

check process pytask.py matching "/letv/p2sp/offline/pytask.py"
        start program = "/usr/bin/python /letv/p2sp/offline/pytask.py"
        stop program = "/bin/bash -c 'kill -s SIGTERM `ps -ef|grep offline/pytask.py|grep -v grep|awk -F" " '{print $2}'`'"

check process pytimed.py matching "/letv/p2sp/offline/pytimed.py"
        start program = "/usr/bin/python /letv/p2sp/offline/pytimed.py"
        stop program = "/bin/bash -c 'kill -s SIGTERM `ps -ef|grep offline/pytimed.py|grep -v grep|awk -F" " '{print $2}'`'"

check process hadoop with pidfile "/usr/local/hadoop/pids/hadoop-hadoop-datanode.pid"
     start program = "/usr/bin/sudo -u hadoop  -i  hadoop-daemon.sh start  datanode"
     stop program = "/usr/bin/sudo -u hadoop  -i  hadoop-daemon.sh stop  datanode"

check process ETMDaemon matching "/letv/p2sp/xware/lib/ETMDaemon"
        start program = "/letv/p2sp/xware/portal"
        stop program = "/bin/bash -c 'kill -s SIGTERM `ps -ef|grep ETMDaemon|grep -v grep |awk '{print $2}'`'"


```
如果监控配置项比较多，不想放在/etc/monit.conf文件里，那么可以定义include选项，比如：
```
[root@bastion-IDC ~]# vim /etc/monit.conf
.......
include /etc/services.cfg

```
然后创建/etc/services.cfg，将监控进程的配置集中放到这个文件里。
```
[root@bastion-IDC ~]# vim /etc/services.cfg
check process nginx with pidfile /usr/local/nginx/logs/nginx.pid
        start program = "/usr/local/nginx/sbin/nginx"
        stop program = "/usr/local/nginx/sbin/nginx -s stop"
check process php-fpm with pidfile /var/run/php-fpm/php-fpm.pid
       start program = "/etc/init.d/php-fpm start"
       stop program = "/etc/init.d/php-fpm stop"
check process mysqld  with pidfile "/letv/mysql2/data/cdn.oss.letv.com.pid"
       start program = "/etc/init.d/mysqld start"
       stop program = "/etc/init.d/mysqld stop"
.........
```


monit.conf文件里的邮件通知就可以这样配置：
```
# mail-server
set mailserver  smtp.huanqiu.cn port 587
# email-format
set mail-format {
 from: monit@huanqiu.cn
 subject: $SERVICE $EVENT at $DATE on $HOST
 message: Monit $ACTION $SERVICE $EVENT at $DATE on $HOST : $DESCRIPTION.

       Yours sincerely,
          Monit

  }

set alert wangshibo@huanqiu.cn
```


Monit会提供几个内部变量（$DATE、$EVENT、$HOST等），你可以按照你的需求自定义邮件内容。如果你想要从Monit所在机器发送邮件，就需要一个已经安装的与sendmail兼容的程序（如postfix或者ssmtp）。

监控本机部分性能： 

```
check system 127.0.0.1
    if loadavg (5min) > 4 for 4 times 5 cycles then exec "/etc/monit/script/sendsms sysload 5min >4"
    if memory usage > 90% then exec "/etc/monit/script/sendsms 127.0.0.1 memory useage>90%"
    if cpu usage (user)  > 70% for 4 times within 5 cycles then exec "/etc/monit/script/sendsms cpu(user) >70%"
    if cpu usage (system) > 30% for 4 times within 5 cycles then exec "/etc/monit/script/sendsms cpu(system) >30% "
    if cpu usage (wait)  > 20% for 4 times within 5 cycles then exec "/etc/monit/script/sendsms system busy! cpu(wait) >20%"
```


监控远程机器的部分端口：

```
check host Unicom_mobi with address 211.90.246.51
      if failed icmp type echo count 10 with timeout 20 seconds then exec "/etc/monit/script/sendsms Unicom_mobi  211.90.246.51 ping failed!"
      if failed port 22 type tcp with timeout 10 seconds for 2 times within 3 cycles then exec "/etc/monit/script/sendsms unicom 211.90.246.51:2222 connect failed!"
      if failed port 9528 type tcp with timeout 10 seconds for 2 times within 3 cycles then exec "/etc/monit/script/sendsms unicom 211.90.246.51:9528 connect failed!"
      if failed port 9529 type tcp with timeout 10 seconds for 2 times within 3 cycles then exec "/etc/monit/script/sendsms unicom 211.90.246.51:9529 connect failed!"
      if failed port 9530 type tcp with timeout 10 seconds for 2 times within 3 cycles then exec "/etc/monit/script/sendsms unicom 211.90.246.51:9530 connect failed!"
```



monit好处是可以在监控故障设置重启服务和执行自定义脚本，如下

```
check filesystem root with path /dev/mapper/VolGroup00-LogVol00
      if space usage > 80% for 5 times within 15 cycles then exec "/etc/monit/script/clear_core.sh"
         else if succeed for 1 times within 2 cycles then exec "/etc/monit/script/sendsms '/dev/sda1 usage > 90% clear core file succeed!'>/dev/null 2"
```



### 再来看看几个小配置：

##### 1）监控本地服务器的CPU、内存占用
check system localhost
    if loadavg (1min) > 10 then alert
    if loadavg (5min) > 6 then alert
    if memory usage > 75% then alert
    if cpu usage (user) > 70% then alert
    if cpu usage (system) > 60% then alert
    if cpu usage (wait) > 75% then alert

如果某个监控项不需要每个周期都检查，可以如下配置：
    if loadavg (1min) > 10 for 2 cycles then alert

##### 2）设置一个检查远程SMTP服务器（如192.168.1.102）的监控。假定SMTP服务器运行着SMTP、IMAP、SSH服务。
check host MAIL with address 192.168.1.102
   if failed icmp type echo within 10 cycles then alert
   if failed port 25  protocol smtp then alert
      else if recovered then exec "/scripts/mail-script"
   if failed port 22  protocol ssh  then alert
   if failed port 143 protocol imap then alert
检查远程主机是否响应ICMP协议。如果我们在10个周期内没有收到ICMP回应，就发送一条报警。如果监测到25端口上的SMTP协议是异常的，就发送一条报警。如果在一次监测失败后又监测成功了，就运行一个脚本（/scripts/mail-script）。如果检查22端口上的SSH或者143端口上的IMAP协议不正常，同样发送报警。


##### 3）存在性测试：
Monit当发现一个文件不存或者一个服务没有启动的时候默认操作是重启这个操作
check file with path /home/laicb/test.txt 
   if does not exist for 5 cycles then alert
注意：
检测的是文件（使用的是path），如果只写了/home/laicb那么监视的时候就会提示，path不是一个有效的类型！
如果检测目录的话，就用directory替换path

##### 4）资源测试：
有些资源可以在check system路口，有些可以在check entry路口，有些都可以。
if cpu is greater than 50% for 5 cycles then restart
注意：greater表示大于，%也可以用字节或者GB，MB等字符

##### 5）时间戳测试：
时间戳[1]是指文件属性里的创建、修改、访问的时间。（下面的exec表示执行后面的命令动作）
改变形式：
 check file httpd.conf with path /usr/local/apache/conf/httpd.conf
   if changed timestamp
     then exec "/usr/local/apache/bin/apachectl graceful"
常量模式：
check file stored.ckp with path /msg-foo/config/stored.ckp
   if timestamp > 1 minute then alert

##### 6）文件大小测试：
这个只能用在check file入口
check file with path /home/laicb/test.txt  
    if does not exist for 5 cycles then alert  
    if changed size for  1 cycles then alert            //如果没有指定，查看服务所对应的会发现是for 5 times within 5cycles   

如果更改文件大小，那么文件大小变化之后就在状态栏里显示size changed


##### 7）权限测试：
check file monit.bin with path "/usr/local/bin/monit"
       if failed permission 0555 then unmonitor    //如果/usr/local/bin/monit文件权限不是555就拒绝执行

check file passwd with path /etc/passwd           
       if failed uid root then unmonitor    //如果不是root访问/etc/passwd那么拒绝访问
 
##### 8）PID测试
 check process sshd with pidfile /var/run/sshd.pid
       if changed pid then exec "/my/script"

##### 9）更新时间测试：
正常运行时间测试：
check process myapp with pidfile /var/run/myapp.pid
    start program = "/etc/init.d/myapp start"
    stop program = "/etc/init.d/myapp stop"
    if uptime > 3 days then restart

##### 10）监控主机通信
 check host www.huanqiu.com with address www.huanqiu.com
       if failed icmp type echo count 5 with timeout 15 seconds
          then alert

##### 11）apache程序监控
 check process apache with pidfile /var/run/httpd.pid
       start program = "/etc/init.d/httpd start"
       stop program  = "/etc/init.d/httpd stop"
       if cpu > 40% for 2 cycles then alert
       if totalcpu > 60% for 2 cycles then alert
       if totalcpu > 80% for 5 cycles then restart
       if mem > 100 MB for 5 cycles then stop
       if loadavg(5min) greater than 10.0 for 8 cycles then stop

-------------------------------------------------------------------------------------------
### 来看看下面遇到的几种monit不能使用的解决办法：
##### 1）monit进程连接错误！（缺少http的端口支持，少了这部分内容）
最后经过排查发现，monit的配置文件/etc/monitrc里面少了下面两行：
set httpd port 30000
allow 127.0.0.1

将上面两行添加上，monit即可恢复正常使用状态中
[root@cdn ~]# cat /etc/monitrc
set daemon 30
set logfile syslog facility log_daemon
set pidfile /var/run/monit.pid
set httpd port 30000
allow 127.0.0.1
#allow admin:TVA3z3i
..........

##### 2）另外一种错误：（修改127.0.0.1为localhost）
在monit -t和monit reload都没有报错的情况下，monit status报错如下：
[root@cdn ~]# monit status
monit: cannot read status from the monit daemon

查看日志信息：
[root@cdn ~]# tail -f /var/log/messages
Aug 18 19:27:21 cdn monit[14491]: monit: Denied connection from non-authorized client [220.181.153.243]
Aug 18 19:27:21 cdn monit[16899]: monit: cannot read status from the monit daemon

解决办法：
将monit配置文件中的“allow 127.0.0.1”修改为“allow localhost”即可！！
[root@cdn ~]# vim /etc/monitrc
set daemon 30
set logfile syslog facility log_daemon
set pidfile /var/run/monit.pid
set httpd port 30000
allow localhost 
.........

这样，问题得到解决

[root@cdn ~]# monit status
The Monit daemon 5.3.2 uptime: 5m
.........................
Process 'nginx_down'
  status                            Running
  monitoring status                 Monitored
  pid                               18671
  parent pid                        1
  uptime                            145d 5h 17m
  children                          8
  memory kilobytes                  484
  memory kilobytes total            4572
  memory percent                    0.0%
  memory percent total              0.0%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  data collected                    Mon, 18 Aug 2014 19:34:25
.............

##### 3）下面的错误在使用上面两种方法后，仍不能解决问题！ （添加use address 127.0.0.1）
[root@182 conf]# monit -t
Control file syntax OK
[root@182 conf]# monit reload
Reinitializing monit daemon
[root@182 conf]# monit status
monit: error connecting to the monit daemon

查看monit配置文件 
[root@182 conf]# cat /etc/monitrc.bak
set daemon 30
set httpd port 30000
allow 127.0.0.1
set logfile syslog facility log_daemon
set pidfile /var/run/monit.pid
..................

最后解决办法：
需要在monit配置文件中添加“use address 127.0.0.1"内容！
[root@182 conf]# cat /etc/monitrc
set daemon 30
set httpd port 30000
use address 127.0.0.1
allow 127.0.0.1
set logfile syslog facility log_daemon
set pidfile /var/run/monit.pid
.............

查看，问题已经得到解决
[root@182 conf]# monit status
The Monit daemon 5.3.2 uptime: 7m
..............
Process 'rsync'
  status                            Running
  monitoring status                 Monitored
  pid                               13519
  parent pid                        1
  uptime                            393d 9h 8m
  children                          0
  memory kilobytes                  540
  memory kilobytes total            540
  memory percent                    0.0%
  memory percent total              0.0%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  data collected                    Thu, 21 Aug 2014 19:24:58
..............

注意：
上面的第3钟方式是最全面的，如果添加了use address 127.0.0.1后，使用monit status仍然出现下面的情况：
[root@ly-u-gfs1 ~]# monit status
monit: error connecting to the monit daemon

那么就稍微等待一会儿，等一小段时间后，就会发现monit使用顺畅了
[root@ly-u-gfs1 ~]# monit status
The Monit daemon 5.3.2 uptime: 6m

Process 'net-snmp'
  status                            Running
  monitoring status                 Monitored

-------------------------------------------------------------------------------------------------------------------------
# Centos7下部署Monit环境过程：
[root@linux-node2 ~]# yum update 
[root@linux-node2 ~]# yum install -y monit
[root@linux-node2 ~]# rpm -ql monit
/etc/logrotate.d/monit
/etc/monit.d
/etc/monit.d/logging
/etc/monitrc
/usr/bin/monit
/usr/lib/systemd/system/monit.service
/usr/share/doc/monit-5.14
/usr/share/doc/monit-5.14/COPYING
/usr/share/doc/monit-5.14/README
/usr/share/man/man1/monit.1.gz
/var/log/monit.log
[root@linux-node2 ~]# monit -V
This is Monit version 5.14
Copyright (C) 2001-2016 Tildeslash Ltd. All Rights Reserved.

[root@linux-node2 ~]# monit -v
Adding host allow 'localhost'
Skipping redundant host 'localhost'
Adding credentials for user 'admin'
Runtime constants:
 Control file       = /etc/monitrc
 Log file           = /var/log/monit.log
 Pid file           = /run/monit.pid
 Id file            = /root/.monit.id
 State file         = /root/.monit.state
 Debug              = True
 Log                = True
 Use syslog         = False
 Is Daemon          = True
 Use process engine = True
 Poll time          = 30 seconds with start delay 0 seconds
 Expect buffer      = 256 bytes
 Mail from          = (not defined)
 Mail subject       = (not defined)
 Mail message       = (not defined)
 Start monit httpd  = True
 httpd bind address = localhost
 httpd portnumber   = 2812
 httpd ssl          = Disabled
 httpd signature    = Enabled
 httpd auth. style  = Basic Authentication and Host/Net allow list

The service list contains the following entries:

System Name           = linux-node2.openstack
 Monitoring mode      = active

查看默认的配置文件内容
[root@linux-node2 ~]# grep -v '^#' /etc/monitrc
set daemon  30               # check services at 30 seconds intervals
set logfile syslog

set httpd port 2812 and
    use address localhost         # only accept connection from localhost
    allow localhost                   # allow localhost to connect to the server and
    allow admin:monit              # require user 'admin' with password 'monit'
    allow @monit                    # allow users of group 'monit' to connect (rw)
    allow @users readonly       # allow users of group 'users' to connect readonly

include /etc/monit.d/*

[root@linux-node2 ~]# cat /etc/logrotate.d/monit
/var/log/monit.log {
    missingok
    notifempty
    size 100k
    create 0644 root root
    postrotate
        /bin/systemctl reload monit.service > /dev/null 2>&1 || :
    endscript
}

[root@linux-node2 ~]# cat /etc/monit.d/logging 
#log to monit.log
set logfile /var/log/monit.log                     //监视周期为60秒，日志输出及日志滚动以配置好了

配置monit
[root@linux-node2 ~]# vim /etc/monitrc

set daemon  5   
set logfile syslog
 
set httpd port 2812 and
    use address localhost
    allow localhost       
    allow admin:monit     
    allow @monit          
    allow @users readonly    
 
include /etc/monit.d/*
 
check process sshd with pidfile /var/run/sshd.pid
    start program "/usr/bin/systemctl start sshd.service"
    stop program "/usr/bin/systemctl stop sshd.service"
    if failed port 22 protocol ssh then restart
    if 5 restart within 5 cycles then timeout
 
check process apache with pidfile /etc/httpd/run/httpd.pid
  start program = "/usr/bin/systemctl start httpd" with timeout 60 seconds
  stop program  = "/usr/bin/systemctl stop httpd"
  if failed host linux-node2.openstack port 80 protocol http
     and request "/readme.html"
     then restart
  if 3 restarts within 5 cycles then timeout
  group apache
 
check process mariadb with pidfile "/var/lib/mysql/linux-node2.pid"
    start = "/usr/bin/systemctl start mariadb.service"
    stop = "/usr/bin/systemctl stop mariadb.service"
    if failed host 127.0.0.1 port 3306 protocol mysql then restart
    if 5 restarts within 5 cycles then timeout

----------------------------------------------------------------------------------------------
查看mysql服务的pid
MariaDB [(none)]> show variables like "%pid%";
+---------------+--------------------------------+
| Variable_name | Value                          |
+---------------+--------------------------------+
| pid_file      | /var/lib/mysql/linux-node2.pid |
+---------------+--------------------------------+
1 row in set (0.00 sec)


启动monit
[root@linux-node2 ~]# systemctl enable monit.service
Created symlink from /etc/systemd/system/multi-user.target.wants/monit.service to /usr/lib/systemd/system/monit.service.
[root@linux-node2 ~]# systemctl start monit.service
[root@linux-node2 ~]# lsof -i:2812
COMMAND   PID USER   FD   TYPE    DEVICE SIZE/OFF NODE NAME
monit   89106 root    5u  IPv4 172788270      0t0  TCP localhost:atmtcp (LISTEN)
[root@linux-node2 ~]# systemctl status monit.service
● monit.service - Pro-active monitoring utility for unix systems
   Loaded: loaded (/usr/lib/systemd/system/monit.service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2017-02-03 10:47:22 CST; 50s ago
 Main PID: 89106 (monit)
   CGroup: /system.slice/monit.service
           └─89106 /usr/bin/monit -I

Feb 03 10:47:22 linux-node2.openstack systemd[1]: Started Pro-active monitoring utility for unix systems.
Feb 03 10:47:23 linux-node2.openstack systemd[1]: Starting Pro-active monitoring utility for unix systems...
Feb 03 10:47:23 linux-node2.openstack monit[89106]: /etc/monitrc:20: Program does not exist: 'systemctl'
Feb 03 10:47:23 linux-node2.openstack monit[89106]: /etc/monitrc:21: Program does not exist: 'systemctl'
Feb 03 10:47:23 linux-node2.openstack monit[89106]: Starting Monit 5.14 daemon with http interface at [localhost]:2812

查看monit状态

[root@linux-node2 ~]# monit status
The Monit daemon 5.14 uptime: 9m 

Process 'sshd'
  status                            Running
  monitoring status                 Monitored
  pid                               1755
  parent pid                        1
  uid                               0
  effective uid                     0
  gid                               0
  uptime                            86d 19h 39m 
  children                          6
  memory                            3.5 MB
  memory total                      25.1 MB
  memory percent                    0.0%
  memory percent total              0.0%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  port response time                0.021s to [localhost]:22 type TCP/IP protocol SSH
  data collected                    Fri, 03 Feb 2017 10:57:20

Process 'apache'
  status                            Not monitored
  monitoring status                 Not monitored
  data collected                    Fri, 03 Feb 2017 10:50:21

Process 'mariadb'
  status                            Running
  monitoring status                 Monitored
  pid                               46235
  parent pid                        1
  uid                               27
  effective uid                     27
  gid                               27
  uptime                            29d 16h 1m 
  children                          0
  memory                            296.1 MB
  memory total                      296.1 MB
  memory percent                    0.4%
  memory percent total              0.4%
  cpu percent                       0.0%
  cpu percent total                 0.0%
  port response time                0.001s to [127.0.0.1]:3306 type TCP/IP protocol MYSQL
  data collected                    Fri, 03 Feb 2017 10:57:20

System 'linux-node2.openstack'
  status                            Running
  monitoring status                 Monitored
  load average                      [2.01] [1.86] [1.94]
  cpu                               5.2%us 2.0%sy 0.0%wa
  memory usage                      44.0 GB [70.1%]
  swap usage                        2.6 MB [0.1%]
  data collected                    Fri, 03 Feb 2017 10:57:20

重新载入monit服务
[root@linux-node2 ~]# monit reload
Reinitializing monit daemon

确认monit自动启动进程
停止nginx进程之后，查看monit.log文件
[root@linux-node2 ~]# systemctl stop nginx.service
[root@linux-node2 ~]# tailf /var/log/monit.log
[CST Apr  5 21:35:18] error    : 'nginx' process is not running
[CST Apr  5 21:35:18] info     : 'nginx' trying to restart
[CST Apr  5 21:35:18] info     : 'nginx' start: /usr/bin/systemctl

配置启动启动。根据系统及版本自动启动的命令不同，在这里介绍CentOS7上配置自动启动的方法
[root@linux-node2 ~]# systemctl list-unit-files | grep monit.service
monit.service                          disabled
[root@linux-node2 ~]# systemctl enable monit.service
ln -s '/usr/lib/systemd/system/monit.service' '/etc/systemd/system/multi-user.target.wants/monit.service'
[root@linux-node2 ~]# systemctl list-unit-files | grep monit.service
monit.service                          enabled

本文转自 (https://cloud.tencent.com/developer/article/1027097)

###  附上自己写的监控 

```
root@iZwz93z41dx386tb44eba4Z:~# cat /home/dc/dc_code/frp_0.27.0_linux_amd64/frps-control.sh 
if [[ $1 == "start" ]];then
	systemctl start daiyi-frps.service
elif [[ $1 == "stop" ]];then
	systemctl stop daiyi-frps.service
fi;
root@iZwz93z41dx386tb44eba4Z:~# 
```
monit的配置文件里
```
check process frps with matching "frps"
        start program = "/home/dc/dc_code/frp_0.27.0_linux_amd64/frps-control.sh start" with timeout 60 seconds
        stop program  = "/home/dc/dc_code/frp_0.27.0_linux_amd64/frps-control.sh stop"

```
重启monit
```
systemctl restart monit.service
```

多次 kill 掉之后， 他还是会立刻恢复， 很有效果啊， 
```
root@iZwz93z41dx386tb44eba4Z:~# ps -ef|grep frps
root     10227     1  0 09:20 ?        00:00:00 /bin/bash /home/dc/dc_code/frp_0.27.0_linux_amd64/start_frps.sh
root     10235 10227  0 09:20 ?        00:00:00 sudo /home/dc/dc_code/frp_0.27.0_linux_amd64/frps -c /home/dc/dc_code/frp_0.27.0_linux_amd64/frps.ini
root     10237 10235  0 09:20 ?        00:00:00 /home/dc/dc_code/frp_0.27.0_linux_amd64/frps -c /home/dc/dc_code/frp_0.27.0_linux_amd64/frps.ini
root     11644 11230  0 09:52 pts/1    00:00:00 grep --color=auto frps
root@iZwz93z41dx386tb44eba4Z:~# kill -9 10227

root@iZwz93z41dx386tb44eba4Z:/home/dc/dc_code/monit-5.25.3/conf# ps -ef|grep frps
root     10068     1  0 09:18 ?        00:00:00 /bin/bash /home/dc/dc_code/frp_0.27.0_linux_amd64/start_frps.sh
root     10072 10068  0 09:18 ?        00:00:00 sudo /home/dc/dc_code/frp_0.27.0_linux_amd64/frps -c /home/dc/dc_code/frp_0.27.0_linux_amd64/frps.ini
root     10080 10072  0 09:18 ?        00:00:00 /home/dc/dc_code/frp_0.27.0_linux_amd64/frps -c /home/dc/dc_code/frp_0.27.0_linux_amd64/frps.ini
root     10129  9060  0 09:19 pts/0    00:00:00 grep --color=auto frps
[1]+  Killed                  systemctl status daiyi-frps.service

root@iZwz93z41dx386tb44eba4Z:/home/dc/dc_code/monit-5.25.3/conf# kill -9 10080
root@iZwz93z41dx386tb44eba4Z:/home/dc/dc_code/monit-5.25.3/conf# ps -ef|grep frps
root     10146     1  0 09:19 ?        00:00:00 /bin/bash /home/dc/dc_code/frp_0.27.0_linux_amd64/start_frps.sh
root     10153 10146  0 09:19 ?        00:00:00 sudo /home/dc/dc_code/frp_0.27.0_linux_amd64/frps -c /home/dc/dc_code/frp_0.27.0_linux_amd64/frps.ini
root     10155 10153  4 09:19 ?        00:00:00 /home/dc/dc_code/frp_0.27.0_linux_amd64/frps -c /home/dc/dc_code/frp_0.27.0_linux_amd64/frps.ini
root     10169  9060  0 09:19 pts/0    00:00:00 grep --color=auto frps

root@iZwz93z41dx386tb44eba4Z:/home/dc/dc_code/monit-5.25.3/conf# kill -9 10153
root@iZwz93z41dx386tb44eba4Z:/home/dc/dc_code/monit-5.25.3/conf# ps -ef|grep frps
root     10189     1  0 09:19 ?        00:00:00 /bin/bash /home/dc/dc_code/frp_0.27.0_linux_amd64/start_frps.sh
root     10190 10189  0 09:19 ?        00:00:00 sudo /home/dc/dc_code/frp_0.27.0_linux_amd64/frps -c /home/dc/dc_code/frp_0.27.0_linux_amd64/frps.ini
root     10203 10190  2 09:19 ?        00:00:00 /home/dc/dc_code/frp_0.27.0_linux_amd64/frps -c /home/dc/dc_code/frp_0.27.0_linux_amd64/frps.ini
root     10213  9060  0 09:19 pts/0    00:00:00 grep --color=auto frps

```

