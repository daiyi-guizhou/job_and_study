

#总核数 = 物理CPU个数 X 每颗物理CPU的核数 
#总逻辑CPU数 = 物理CPU个数 X 每颗物理CPU的核数 X 超线程数

#查看物理CPU个数
```
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l
```

#查看每个物理CPU中core的个数(即核数)
```
cat /proc/cpuinfo| grep "cpu cores"| uniq
```

查看逻辑CPU的个数
```
cat /proc/cpuinfo| grep "processor"| wc -l
```

 查看CPU信息（型号）
```
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
```

##### 另外，top命令中看到的CPU数目是逻辑CPU（输入top后再按1
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190308153807367.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
参考链接(https://www.cnblogs.com/emanlee/p/3587571.html)
(https://www.jianshu.com/p/fcc49d7a0073)

#### 基本概念

###### 物理CPU：
物理CPU就是插在主机上的真实的CPU硬件，在Linux下可以数不同的physical id 来确认主机的物理CPU个数。

###### 核心数：
物理CPU下一层概念就是核心数，我们常常会听说多核处理器，其中的核指的就是核心数。在Linux下可以通过cores来确认主机的物理CPU的核心数。

###### 逻辑CPU：
核心数下一层的概念是逻辑CPU，逻辑CPU跟超线程技术有联系，假如物理CPU不支持超线程的，那么逻辑CPU的数量等于核心数的数量；
如果物理CPU支持超线程，那么逻辑CPU的数目是核心数数目的两倍。在Linux下可以通过 processors 的数目来确认逻辑CPU的数量。

###### 超线程：
超线程是英特尔开发出来的一项技术，使得单个处理器可以象两个逻辑处理器那样运行，这样单个处理器以并行
执行线程。
这里的单个处理器也可以理解为CPU的一个核心；这样便可以理解为什么开启了超线程技术后，逻辑CPU的数目是核心数的两倍了。


