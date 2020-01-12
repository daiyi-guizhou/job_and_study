##参考 官网。https://github.com/open-falcon/mail-provider
#open-falcon2.0的最新版。2018-10-18
#下载安装包
```
cd /home/work/open-falcon
wget http://cactifans.hi-www.com/open-falcon/mail-provider.tar.gz
mkdir -p mail-provider
tar zxvf mail-provider.tar.gz  -C mail-provider
cd mail-provider
```
#修改配置文件`vi  cfg.json`  
#你的邮箱的权限要打开，stmp。否则各种报错。查看日志来解决问题。
![在这里插入图片描述](https://img-blog.csdn.net/20181018142221779?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

#启动 mail-provider

```
./control start
```

#修改open-falcon中的alarm的配置文件

```
vi /home/work/open-falcon/alarm/config/cfg.json
```
![127.0.0.1如果不行，就换成本机IP。](https://img-blog.csdn.net/20181018142835147?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
#127.0.0.1如果不行，就换成本机IP
####### 这里的dashboard:  就是你的dashboard的地址, 这里配置的作用就是, 当你发报警邮件的时候, 他会有个链接地址, 就是 在这里配置的dashboard的地址.
###  open-project的邮件通知也是一样的。
选择下面的 SMTP HELLO 域。
![在这里插入图片描述](https://img-blog.csdnimg.cn/2019021419163318.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)

#接着配置告警触发，  就收到了 
![在这里插入图片描述](https://img-blog.csdn.net/20181018143135734?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)



##配置告警expression的时候, 如果你的metric有多个tag,应该都写上, 
比如.我的有两个tag.     之前只写一个, 结果就没有触发告警, 
后来两个都写上.才触发告警的.
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181214122314891.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)


















