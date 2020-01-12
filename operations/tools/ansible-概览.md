本文转自(http://blog.51cto.com/changfei/1657221)
ansible 官网－中文(https://ansible-tran.readthedocs.io/en/latest/docs/faq.html)

ansible安装

```
[root@ju ~]# yum install ansible -y
```
定义主机与组
```
[root@ju ~]# vim /etc/ansible/hosts  #添加主机，并在所配置的主机上与ansible建立互信
192.168.116.138
192.168.116.139
192.168.116.139:7022 #定义一个ssh端口为7022的主机
juserver ansible_ssh_port=22  ansible_ssh_host=192.168.116.25 #利用别名定义一个主机，使用的时候直接使用juserver这个别名即可
[webserver]   #建立分组
192.168.116.2
192.168.116.3
192.168.116.4
www[01:50].example.com  #支持通配符匹配www01 www02 ...www50
[dbserver]
192.168.116.5
192.168.116.6
db-[a:f].example.com  #支持字母匹配a b c...f
[weballserver:children] #组嵌套，不过这个只能用在playbook中，ansible命令行中使用不了
webserver
dbserver
[myserver]
192.168.116.7 http_port=8000 maxRequestsPerChild=808 #可以为每个主机单独指定一些变量，这些变量可以在playbooks中使用
192.168.116.8 http_port=303 maxRequestsPerChild=909
[weixinserver]
192.168.116.9
192.168.116.10
[weixinserver:vars]  #也可以为一个组指定变量，组内每个主机都可以使用该变量
ntp_server=ntp.weixinserver.example.com
proxy=proxy.weixinserver.example.com
```




ansible保留主机变量

```
#ansible_ssh_host：指定主机别名对应的真实IP，如：251 ansible_ssh_host=192.168.116.251，随后连接该主机无须指定完整IP，只需指定251 就行
#ansible_ssh_port：指定连接到这个主机的ssh 端口，默认22
#ansible_ssh_user：连接到该主机的ssh用户
#ansible_ssh_pass：连接到该主机的ssh密码（连-k 选项都省了），安全考虑还是建议使用私钥或在命令行指定-k 选项输入
#ansible_sudo_pass：sudo 密码
#ansible_sudo_exe(v1.8+的新特性):sudo 命令路径
#ansible_connection：连接类型，可以是local、ssh 或paramiko，ansible1.2 之前默认为paramiko
#ansible_ssh_private_key_file：私钥文件路径
#ansible_shell_type：目标系统的shell类型，默认为sh,如果设置csh/fish，那么命令需要遵循它们语法
#ansible_python_interpreter：python 解释器路径，默认是/usr/bin/python，但是如要要连freeBSD系统的话，就需要该指令修改python路径
#ansible_*_interpreter：这里的"*"可以是ruby或perl或其他语言的解释器，作用和ansible_python_interpreter类似
```



分离主机和组的变量定义

```
#为host 和group 定义一些比较复杂的变量时（如array、hash），可以用单独文件保存host和group 变量，以YAML 格式书写变量，避免都写在hosts 文件显得混乱，如果hosts 文件路径为：
/etc/ansible/hosts
#则host 和group 变量目录结构：
/etc/ansible/host_vars/all   #host_vars 目录用于存放host 变量，all 文件对所有主机有效
/etc/ansible/host_vars/foosball  #文件foosball 要和hosts 里面定义的主机名一样，表示只对foosball 主机有效
/etc/ansible/group_vars/all  #group_vars 目录用于存放group 变量，all 文件对所有组有效
/etc/ansible/group_vars/raleigh  #文件raleigh 要和hosts 里面定义的组名一样，表示对raleigh 组下的所有主机有效
#这里/etc/ansible/group_vars/raleigh 格式如下，YAML 格式要求：
ntp_server: acme.example.org    #变量名:变量值
database_server: storage.example.org

```

主机匹配方式

```
#表示通配inventory 中的所有主机
all
'*' #星号必须引起来
#也可以指定具有规则特征的主机或者主机名
one.example.com
one.example.com:two.example.com
192.168.1.50
192.168.1.*
#意思是这两个组中的所有主机
webservers:dbservers
#非模式匹配：表示在webservers 组不在phoenix 组的主机
webservers:!phoenix
#交集匹配：表示同时都在webservers 和staging 组的主机
webservers:&staging
```



命令行简单举例

```
#ansible <pattern_goes_here> -m <module_name> -a <arguments>

[root@ju ~]# ansible 192.168.116.138 -m ping   #对单台主机测试ping
[root@ju ~]# ansible all -m ping   #对/etc/ansible/hosts中所有主机测试ping
[root@ju ~]# ansible webserver -a "/bin/echo hello" #运行命令
[root@ju ~]# ansible all -a "uptime"
[root@ju ~]# ansible dbserver -m copy -a "src=/tmp/ansible dest=/tmp/ansible_1"  #copy文件
[root@ju ~]# ansible 192.168.116.138 -m file -a "dest=/tmp/ansible_1 mode=600 owner=ju group=ju" #改变文件属性
[root@ju ~]# ansible 192.168.116.138 -m service -a "name=httpd state=running" #启动服务，或者放到开机启动的同时运行
[root@ju ~]# ansible all -m setup  #打印主机的清单，将输出用于描述每一台主机的JSON对象，其中包括总体内存、已使用内存、CPU、网络、磁盘信息、操作系统版本以及内核版本等等。
```




查看模块帮助

```
[root@db ansible]# ansible-doc ping
> PING
  A trivial test module, this module always returns `pong' on  successful contact. It does not make sense in playbooks, but it is  useful from `/usr/bin/ansible'
#Test 'webservers' status 
ansible webservers -m ping
```

# ansible常用模块
并行性和shell命令command|script|shell

```
#重启webservers主机组的所有机器，每次重启10 台
ansible webservers -a "/sbin/reboot" -f 10
#以ju 用户身份在webservers组的所有主机运行foo 命令
ansible webservers -a "/usr/bin/foo" -u ju
#以ju 用户身份sudo 执行命令foo（--ask-sudo-pass (-K) 如果有sudo 密码请使用此参数）
ansible webservers -a "/usr/bin/foo" -u ju --sudo [--ask-sudo-pass]
#也可以sudo 到其他用户执行命令非root
ansible webservers -a "/usr/bin/foo" -u username -U otheruser [--ask-sudo-pass]
#默认情况下，ansible 使用的module 是command，这个模块并不支持shell 变量和管道等，若想使用shell 来执行模块，请使用-m 参数指定shell 模块
#使用shell 模块在远程主机执行命令或脚本
ansible dbservers -m shell -a 'echo $TERM'
ansible dbservers -m shell -a '/tmp/test.sh'
#script命令模块，在远程主机执行主控端本地的脚本文件，相当于scp+shell
ansible dbservers -m script -a '/tmp/test.sh 111  222'
```



传输文件copy|file

```
#拷贝本地的/etc/hosts 文件到myserver主机组所有主机的/tmp/hosts（空目录除外）,如果使用playbooks 则可以充分利用template 模块
ansible myserver -m copy -a "src=/etc/hosts dest=/tmp/hosts mode=600 owner=ju group=ju"
#file 模块允许更改文件的用户及权限
ansible webservers -m file -a "dest=/srv/foo/a.txt mode=600"
ansible webservers -m file -a "dest=/srv/foo/b.txt mode=600 owner=ju group=ju"
#使用file 模块创建目录，类似mkdir -p
ansible webservers -m file -a "dest=/path/to/c mode=755 owner=ju group=ju state=directory"
#使用file 模块删除文件或者目录
ansible webservers -m file -a "dest=/path/to/c state=absent"
```



获取远程文件信息stat

```
ansible webservers -m stat -a "path=/etc/password"
```



下载指定定url到远程主机get_url

```
ansible webservers -m get_url -a "url=  mode=0440 force=yes"
```



管理软件包yum

```
#确保acme 包已经安装，但不更新
ansible webservers -m yum -a "name=acme state=present"
#确保安装包到一个特定的版本
ansible webservers -m yum -a "name=acme-1.5 state=present"
#确保一个软件包是最新版本
ansible webservers -m yum -a "name=acme state=latest"
#确保一个软件包没有被安装
ansible webservers -m yum -a "name=acme state=absent"
#Ansible 支持很多操作系统的软件包管理，使用时-m 指定相应的软件包管理工具模块，如果没有这样的模块，可以自己定义类似的模块或者使用command 模块来安装软件包
```



用户和用户组user

```
#使用user 模块对于创建新用户和更改、删除已存在用户非常方便
ansible all -m user -a "name=foo password=<crypted password here>"
ansible all -m user -a "name=foo state=absent"
生成加密密码方法
mkpasswd --method=SHA-512
pip install passlib
python -c "from passlib.hash import sha512_crypt; import getpass; print sha512_crypt.encrypt(getpass.getpass())"
```



服务管理service

```
#确保webservers 组所有主机的httpd 是启动的
ansible webservers -m service -a "name=httpd state=started"
#重启webservers 组所有主机的httpd 服务
ansible webservers -m service -a "name=httpd state=restarted"
#确保webservers 组所有主机的httpd 是关闭的
ansible webservers -m service -a "name=httpd state=stopped192.168.116"
```


后台运行

```
#长时间运行的操作可以放到后台执行，ansible 会检查任务的状态；在主机上执行的同一个任务会分配同一个job ID
#后台执行命令3600s，-B 表示后台执行的时间
ansible all -B 3600 -a "/usr/bin/long_running_operation --do-stuff"
#检查任务的状态
ansible all -m async_status -a "jid=123456789"
#后台执行命令最大时间是1800s 即30 分钟，-P 每60s 检查下状态默认15s
ansible all -B 1800 -P 60 -a "/usr/bin/long_running_operation --do-stuff"
```



搜集系统信息setup



```
#通过命令获取所有的系统信息
#搜集主机的所有系统信息
ansible all -m setup
#搜集系统信息并以主机名为文件名分别保存在/tmp/facts 目录
ansible all -m setup --tree /tmp/facts
#搜集和内存相关的信息
ansible all -m setup -a 'filter=ansible_*_mb'
#搜集网卡信息
ansible all -m setup -a 'filter=ansible_eth[0-2]'
```
计划任务cron
```
ansible all -m cron -a 'name="jutest" hour="5" job="/bin/bash /tmp/test.sh"'
效果如下：
* 5 * * *  /bin/bash /tmp/test.sh
```

挂载模块mount

```
ansible all -m mount -a 'name=/mnt src=/dev/sda5 fstype=ext4 opts=rostate=present
```


