#  错误1
#在open-falcon的agent端定义了一个 push脚本


```
root@hypereal-test-10:/home# cat test
#!/usr/bin/python
#!-*- coding:utf8 -*-
import requests
import time
import json
ts = int(time.time())
def kk():
    payload = [
        {   
            "endpoint": "test-endpoint-dm/",
            "metric": "camera0.interfram_avg",
            "timestamp": ts,
            "step": 60, 
            "value": 336,                                    
            "counterTpye": "GAUGE", 
            "tags": "cluster=detection-machine",
        },
        {
            "endpoint": "test-endpoint-dm/",
            "metric": "test-metric",
            "timestamp": ts,
            "step": 60,
            "value": 1,
            "counterType": "GAUGE",
            "tags": "cluster=detection-machine",
        },
    ]
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    print(r.text)
while True:
    kk()
    time.sleep(1)
```
   #但是在dashboard端只发现了一个数据， 

#检查日志

```
Oct 29 19:09:12 hypereal-test-10 falcon-agent[30171]: 2018/10/29 19:09:12 var.go:95: <= <Total=1, Invalid:1, Latency=0ms, Message:ok>
Oct 29 19:09:12 hypereal-test-10 falcon-agent[30171]: 2018/10/29 19:09:12 var.go:88: => <Total=2> <Endpoint:test-endpoint-dm/70:85:c2:81:d5:0e, Metric:camera0.interfram_avg, Type:, Tags:cluster=detection-machine,cluster=detection-machine, Step:60, Time:1540811050, Value:336>
Oct 29 19:09:12 hypereal-test-10 falcon-agent[30171]: 2018/10/29 19:09:12 var.go:95: <= <Total=2, Invalid:1, Latency=0ms, Message:ok>
Oct 29 19:09:13 hypereal-test-10 falcon-agent[30171]: 2018/10/29 19:09:13 var.go:88: => <Total=2> <Endpoint:test-endpoint-dm/70:85:c2:81:d5:0e, Metric:camera0.interfram_avg, Type:, Tags:cluster=detection-machine,cluster=detection-machine, Step:60, Time:1540811050, Value:336>
```

#<Total=2, Invalid:1   这是什么鬼， 就是一直报错。

#后来在大神的指导下， Invaild 就是说有格式错误。 OK就是好的，2个里面有一个有了问题。

#再次检查自己的脚本

```
"counterTpye": "GAUGE",    #  Tpye 是什么，额，，，， 改成Type。
```

 #再次查看日志
 

```
Oct 29 19:47:29 hypereal-test-10 falcon-agent[30171]: 2018/10/29 19:47:29 var.go:88: => <Total=2> <Endpoint:test-endpoint-dm/70:85:c2:81:d5:0e, Metric:camera0.interfram_avg, Type:GAUGE, Tags:cluster=detection-machine,cluster=detection-machine, Step:60, Time:1540813625, Value:336>
Oct 29 19:47:29 hypereal-test-10 falcon-agent[30171]: 2018/10/29 19:47:29 var.go:95: <= <Total=2, Invalid:0, Latency=0ms, Message:ok>
Oct 29 19:47:30 hypereal-test-10 falcon-agent[30171]: 2018/10/29 19:47:30 var.go:88: => <Total=2> <Endpoint:test-endpoint-dm/70:85:c2:81:d5:0e, Metric:camera0.interfram_avg, Type:GAUGE, Tags:cluster=detection-machine,cluster=detection-machine, Step:60, Time:1540813625, Value:336>
Oct 29 19:47:30 hypereal-test-10 falcon-agent[30171]: 2018/10/29 19:47:30 var.go:95: <= <Total=2, Invalid:0, Latency=0ms, Message:ok>     #Invaild:0   完全没问题了

```
#  错误2
##写了个脚本来push

```
#!/usr/bin/python
#!-*- coding:utf8 -*-
import requests
import time
import json

ts = int(time.time())
def kk():
    payload = [
        {   
            "endpoint": "test-endpoint-dm",
            "metric": "cam.interfram_avg",
            "timestamp": ts,
            "step": 60, 
            "value": 336,                                    
            "counterType": "GAUGE", 
            "tags": "cluster=detection-machine",
        },
    ]

    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))

    print(r.text)

while True:
    kk()
    time.sleep(1)
```
      #看日志是， invalid 0, 说明没问题啊， 但是大盘是就是没数据， 各方面的日志也没有报错。 

#再次请教大神

看了下各方面日志

```
Oct 30 17:34:57 hypereal-test-10 falcon-agent[30171]: 2018/10/30 17:34:57 var.go:88: => <Total=2> <Endpoint:test-endpoint-dm, Metric:camera0.interfram_avg, Type:GAUGE, Tags:cluster=detection-machine,cluster=detection-machine, Step:60, Time:1540885244, Value:336>
Oct 30 17:34:57 hypereal-test-10 falcon-agent[30171]: 2018/10/30 17:34:57 var.go:95: <= <Total=2, Invalid:0, Latency=0ms, Message:ok>
Oct 30 17:34:58 hypereal-test-10 falcon-agent[30171]: 2018/10/30 17:34:58 var.go:88: => <Total=2> <Endpoint:test-endpoint-dm, Metric:camera0.interfram_avg, Type:GAUGE, Tags:cluster=detection-machine,cluster=detection-machine, Step:60, Time:1540885244, Value:336>
Oct 30 17:34:58 hypereal-test-10 falcon-agent[30171]: 2018/10/30 17:34:58 var.go:95: <= <Total=2, Invalid:0, Latency=0ms, Message:ok>
Oct 30 17:34:59 hypereal-test-10 falcon-agent[30171]: 2018/10/30 17:34:59 var.go:88: => <Total=2> <Endpoint:test-endpoint-dm, Metric:camera0.interfram_avg, Type:GAUGE, Tags:cluster=detection-machine,cluster=detection-machine, Step:60, Time:1540885244, Value:336>
Oct 30 17:34:59 hypereal-test-10 falcon-agent[30171]: 2018/10/30 17:34:59 var.go:95: <= <Total=2, Invalid:0, Latency=0ms, Message:ok>
Oct 30 17:35:00 hypereal-test-10 falcon-agent[30171]: 2018/10/30 17:35:00 var.go:88: => <Total=2> <Endpoint:test-endpoint-dm, Metric:camera0.interfram_avg-, Type:GAUGE, Tags:cluster=detection-machine,cluster=detection-machine, Step:60, Time:1540885244, Value:336>
```
###Time:1540885244   Time一直都是这个数值，什么鬼，

Time应该是随时间变化的。
重写代码

```
#!/usr/bin/python
#!-*- coding:utf8 -*-
import requests
import time
import json

###之前时间在这里，不随函数改变，是个定值，所以dashboard看不到。
def kk():
	ts = int(time.time())   #把这一句移动进去。 这样时间就变化了
    payload = [
        {   
            "endpoint": "test-endpoint-dm",
            "metric": "cam.interfram_avg",
            "timestamp": ts,
            "step": 60, 
            "value": 336,                                    
            "counterType": "GAUGE", 
            "tags": "cluster=detection-machine",
        },
    ]

    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))

    print(r.text)

while True:
    kk()
    time.sleep(1)
```
####脚本有问题啊， 还是要老实写脚本。
 
#  错误3
配置了告警，
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181031115530921.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)


#接着设置触发， 故意弄个触发值
#但是， 没出现告警
![在这里插入图片描述](https://img-blog.csdnimg.cn/2018103111573282.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)

#很郁闷， 很受挫，怎么破？
#不着急，着急不解决问题
#让我们来看下架构， 整理下思路
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181031120021539.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)

1 确保数据从agent上传成功
2确保 transfer传数据到了judge
3确保judge传数据到了redis
4确保alarm收到了redis的数据
##以上 1234基本就是我排查的数据，从下至上， 你也可以从上至下，4321

##查看日志，终于在 alarm.err上看到了报错，（这个日志，默认是/alarm/log/alarm.log）
##6379 redis的端口，大家都知道，问题就出在这

![在这里插入图片描述](https://img-blog.csdnimg.cn/20181031120723780.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
##接下来，就是排错了，为什么连不上
1网络
2域名，地址
3权限
4防火墙
........

#修改好之后，  查看dashboard，可以了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181031121334970.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
