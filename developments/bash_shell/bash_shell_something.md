# if 判断用 [[ ]]
这是一个简单的 if　判断。
```
if [ `ps ax | grep -i 'open-falcon' |wc -l` == 2 ] || [ `ps ax | grep -i 'open-falcon' | awk -F " " '{print $7}'|head -n 1` == "/home/work/open-falcon/agent/config/cfg.json" ];then
	echo "ok,i see, $PROG is currently running! so stop it"
	systemctl stop falcon-agent.service
else
	echo "no ,this is nothing."
fi
```
当我用git　CI 打包的时候，　他就会有报错，　　一元等式 == 　出错。

后来,　改为 if  [[  ]] ;then  结果就成功了. 就没有任何报错了。　

```
if [[ `ps ax | grep -i 'open-falcon' |wc -l` == 2 ]] || [[ `ps ax | grep -i 'open-falcon' | awk -F " " '{print $7}'|head -n 1` == "/home/work/open-falcon/agent/config/cfg.json" ]];then
	echo "ok,i see, $PROG is currently running! so stop it"
	systemctl stop falcon-agent.service
else
	echo "no ,this is nothing."
fi
```

# 用绝对路径
这个脚本，　　生成文件，读文件，　
主要是这两句，　之前直接用相对　路径，ip

```
grep rtsp /opt//config.yaml | awk -F'/' '{ print $3 }'| awk -F':' '{ print $1 }' > ip_all.txt 
if ping -c 1 `head -n $i ip_all.txt | tail -1` >/dev/null 2>&1
```
结果 ip_all.txt文件就只是在 /root/目录下， 而没有在 我们工作的目录，/home/work/open-falcon/push-scripts/　下，导致脚本失败。
添加了绝对路径后，就在/home/work/open-falcon/push-scripts/ 有文件 ip_all.txt.

```
grep rtsp /opt//config.yaml | awk -F'/' '{ print $3 }'| awk -F':' '{ print $1 }' > /home/work/open-falcon/push-scripts/ip_all.txt 
if ping -c 1 `head -n $i /home/work/open-falcon/push-scripts/ip_all.txt | tail -1` >/dev/null 2>&1
```


```
#!/bin/bash
num=`grep rtsp /opt/config.yaml|wc -l`
grep rtsp /opt//config.yaml | awk -F'/' '{ print $3 }'| awk -F':' '{ print $1 }' > /home/work/open-falcon/push-scripts/ip_all.txt 

#cat /home/work/open-falcon/push-scripts/ip_all.txt 
num_true=0
num_fail=0
#for i in {1..5}
for i in `seq 1 $num`
do
	if ping -c 1 `head -n $i /home/work/open-falcon/push-scripts/ip_all.txt | tail -1` >/dev/null 2>&1
	then 
		#echo yes_ping
		num_true=$(($num_true + 1))
	else 
		#echo no_ping;
		#echo $i;
		num_fail=$(($num_fail + 1))
	fi
done

#echo $num_fail

if [ $num_fail == 0 ]
then
	echo 100
else
	echo $((100*$num_true/$num))
fi
```

# timeout

```
timeout 30 nvidia-smi | wc -l
```
if you donot make sure how long the command (bash shell) will cost,
command is good for you to control the time.        

like  the example at top,  if time is longer than  30 seconds,  the system will kill the process of "nvidia-smi". 
# runuser
runuser命令使用一个替代的用户或者组ID运行一个Shell。这个命令仅在root用户时有用。

仅以会话PAM钩子运行，并且没有密码提示。如果用一个非root用户，并且该用户没有权限设置user ID，这个命令将会因为程序没有setuid而失败。因runuser不会运行认证和账户PAM钩子，它比su更底层。

语法：

```
runuser -l userNameHere -c 'command'
runuser -l userNameHere -c '/path/to/command arg1 arg2'
```
举例来说，作为一个root用户，你也许想检查下oracle用户下的shell资源限制，输入：

```
# runuser -l oracle -c 'ulimit -SHa'
```
或者监察下nginx或lighttpd web服务器限制：

```
# runuser -l nginx -c 'ulimit -SHa'
```
