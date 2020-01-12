
写多线程脚本，运行的时候报错

File "/usr/local/lib/python2.6/threading.py", line 465, in start
    raise RuntimeError("thread.__init__() not called")
RuntimeError: thread.__init__() not called

原因是线程类中构造函数__init__()中未调用父类的初始化方法，在__init__()函数里加入调用父类初始化方法的代码就OK了，

类似下边这样　threading.Thread.__init__(self)

```
class MyThread(threading.Thread):
    def __init__(self,ip_port_seg):
        threading.Thread.__init__(self)
        self.ip_port_seg = ip_port_seg
```
转自(https://www.cnblogs.com/evilloop/archive/2011/09/22/2184710.html)
