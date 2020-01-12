#话不多说，先来脚本
```
#!/usr/bin/python
import netifaces
import requests
import time
import json
import re
import commands

mac="GPU-machine" + ip    #此处用你的ip
print(mac)
TEMP="GPU Current Temp"

(status,output)=commands.getstatusoutput("nvidia-smi -q | grep 'GPU Current Temp' | cut -d' ' -f 24")
print(status)
print(output)
#此处 'GPU Current Temp' 在函数内部，先用'',外部用“”。否则报错。就是外部'',内部"",则引用不了内部。报错。
def push():
    ts = int(time.time())
    payload = [
            {
            "endpoint": mac,    #若是字符，用“”或者''. 变量就直接用。
            "metric": "GPU-temperture",
            "timestamp": ts,
            "step": 20,
            "value": output,
            "counterType": "GAUGE",
            "tags": "idc=lg,loc=beijing",
                }
            ]
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    print(r.text)
    print(mac)
while True:
    push()
    time.sleep(1)
```

# 1 GPU温度
nvidia-smi -q -i 0 -d TEMPERATURE|grep 'GPU Current'|cut -d" " -f 24
-i0 看第0块GPU
这句命令是用来查看当前GPU的温度的


# 2 python中匹配字符， 需要用 re正则模块。 否则报错。








# 3 python中执行shell命令，不能直接运行，

第一想到的就是os.system，
os.system('cat /proc/cpuinfo')
但是发现页面上打印的命令执行结果 0或者1，当然不满足需求了。

尝试第二种方案 os.popen()
output = os.popen('cat /proc/cpuinfo')
print output.read()
通过 os.popen() 返回的是 file read 的对象，对其进行读取 read() 的操作可以看到执行的输出。但是无法读取程序执行的返回值）

尝试第三种方案 commands.getstatusoutput() 一个方法就可以获得到返回值和输出，非常好用。
(status, output) = commands.getstatusoutput('cat /proc/cpuinfo')
print status, output

参考链接(https://www.cnblogs.com/hei-hei-hei/p/7216434.html)

#  subprocess
 commands模块是python2时用的， 结果我的环境是python3，所以新模块subprocess。
 #先试试Popen

```
>>> tem=subprocess.Popen("nvidia-smi -q | grep 'GPU Current Temp' | cut -d' ' -f 24",shell=True,stdout=subprocess.PIPE,universal_newlines=True)
>>> tem2,err=tem.communicate()
>>> print(tem2)
36

>>> print(tem2)
36

```
#结果是得到了。 但是36下面有个 空行什么意思， 这就不方便传参了。 
换一个subprocess.getstatusoutput
```


>>> subprocess.getstatusoutput("nvidia-smi -q | grep 'GPU Current Temp' | cut -d' ' -f 24")
(0, '36')
>>> a,b=subprocess.getstatusoutput("nvidia-smi -q | grep 'GPU Current Temp' | cut -d' ' -f 24")
>>> print(b)
36
>>> print(b)
36
>>> print(b)
36
>>> 
```
#这就很好， 
