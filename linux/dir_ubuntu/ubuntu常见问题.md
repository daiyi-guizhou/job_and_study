# cpu温度查看
sensors命令
```
xxx@System-Product-Name:~$ sensors
coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +62.0°C  (high = +82.0°C, crit = +100.0°C)
Core 0:        +56.0°C  (high = +82.0°C, crit = +100.0°C)
Core 1:        +56.0°C  (high = +82.0°C, crit = +100.0°C)
Core 2:        +62.0°C  (high = +82.0°C, crit = +100.0°C)
Core 3:        +55.0°C  (high = +82.0°C, crit = +100.0°C)
Core 4:        +54.0°C  (high = +82.0°C, crit = +100.0°C)
Core 5:        +58.0°C  (high = +82.0°C, crit = +100.0°C)
```
＃没有的话需要安装下
CentOS系列:
```
1.yum install lm_sensors;
2.sensors-detect
3.sensors
```

Ubuntu系列:
```
1.apt-get install lm-sensors
2.sensors-detect
3.service kmod start
4.sensors
```
# cpu频率
cpufreq-info -m　命令
```
xxx@System-Product-Name:~$ cpufreq-info -m
cpufrequtils 008: cpufreq-info (C) Dominik Brodowski 2004-2009
Report errors and bugs to cpufreq@vger.kernel.org, please.
analyzing CPU 0:
  driver: intel_pstate
  CPUs which run at the same hardware frequency: 0
  CPUs which need to have their frequency coordinated by software: 0
  maximum transition latency: 0.97 ms.
  hardware limits: 800 MHz - 4.00 GHz
  available cpufreq governors: performance, powersave
  current policy: frequency should be within 800 MHz and 4.00 GHz.    ##额定频率
                  The governor "powersave" may decide which speed to use
                  within this range.
  current CPU frequency is 3.80 GHz.　　　　＃＃当前频率

```
＃没有的话，需要安装下

```
yes|sudo apt install cpufrequtils
```
## cpu降频
若当前频率小于 额定频率, 对半,或者更小时, 有可能是降频,
top看看cpu的使用率.  如果是你的程序把cpu占用很多,,吃的满满的. 导致的才是降频. 
如果你的程序没在用, 那它自然就恢复到一个较低的频率.

# CLI interface报错

```
WARNING: apt does not have a stable CLI interface. Use with caution in scripts.			
E: Internal Error, No file name for open-falcon-agent:amd64			
			
dpkg-preconfigure: 重新开启标准输入失败：			
E: Sub-process /usr/bin/dpkg returned an error code (1)			
```
＃解决方案

```
apt install -f
```
＃备用（要不运行 apt-get update 或者加上 --fix-missing）
# 安装xmind８报错
#报错　 tail -n 40 /xmind/workspace/.metadata/.log

```
root@ＸＸＸ:/home/software/xmind/workspace/.metadata# pwd
/home/daiyi/software/xmind/workspace/.metadata
root@daiyi:/home/daiyi/software/xmind/workspace/.metadata# tail -n 40 .log 
	at org.eclipse.e4.core.internal.contexts.TrackableComputationExt.handleInvalid(TrackableComputationExt.java:74)
	at org.eclipse.e4.core.internal.contexts.EclipseContext.dispose(EclipseContext.java:176)
	at org.eclipse.e4.core.internal.contexts.osgi.EclipseContextOSGi.dispose(EclipseContextOSGi.java:106)
	at org.eclipse.e4.core.internal.contexts.osgi.EclipseContextOSGi.bundleChanged(EclipseContextOSGi.java:139)
	at org.eclipse.osgi.internal.framework.BundleContextImpl.dispatchEvent(BundleContextImpl.java:903)
	at org.eclipse.osgi.framework.eventmgr.EventManager.dispatchEvent(EventManager.java:230)
	at org.eclipse.osgi.framework.eventmgr.ListenerQueue.dispatchEventSynchronous(ListenerQueue.java:148)
	at org.eclipse.osgi.internal.framework.EquinoxEventPublisher.publishBundleEventPrivileged(EquinoxEventPublisher.java:213)
	at org.eclipse.osgi.internal.framework.EquinoxEventPublisher.publishBundleEvent(EquinoxEventPublisher.java:120)
	at org.eclipse.osgi.internal.framework.EquinoxEventPublisher.publishBundleEvent(EquinoxEventPublisher.java:112)
	at org.eclipse.osgi.internal.framework.EquinoxContainerAdaptor.publishModuleEvent(EquinoxContainerAdaptor.java:156)
	at org.eclipse.osgi.container.Module.publishEvent(Module.java:476)
	at org.eclipse.osgi.container.Module.doStop(Module.java:634)
	at org.eclipse.osgi.container.Module.stop(Module.java:498)
	at org.eclipse.osgi.container.SystemModule.stop(SystemModule.java:191)
	at org.eclipse.osgi.internal.framework.EquinoxBundle$SystemBundle$EquinoxSystemModule$1.run(EquinoxBundle.java:165)
	at java.base/java.lang.Thread.run(Thread.java:844)
Caused by: java.lang.ClassNotFoundException: javax.annotation.PreDestroy cannot be found by org.eclipse.e4.core.di_1.6.0.v20160319-0612
	at org.eclipse.osgi.internal.loader.BundleLoader.findClassInternal(BundleLoader.java:398)
	at org.eclipse.osgi.internal.loader.BundleLoader.findClass(BundleLoader.java:361)
	at org.eclipse.osgi.internal.loader.BundleLoader.findClass(BundleLoader.java:353)
	at org.eclipse.osgi.internal.loader.ModuleClassLoader.loadClass(ModuleClassLoader.java:161)
	at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:499)
	... 21 more

```

#看报错，需要java8的包

```
java --version
sudo apt-get install openjdk-8-jdk
```
#编辑XMind.ini 新增一下内容

```
vim xmind/XMind_amd64/XMind.ini
```

```
-vm
/usr/lib/jvm/java-8-openjdk-amd64/bin
```
#添加好之后，结果如下

```
root@XXX:/home/software/xmind/XMind_amd64# tail -n 20 XMind.ini 
-configuration
./configuration
-data
../workspace
-startup
../plugins/org.eclipse.equinox.launcher_1.3.200.v20160318-1642.jar
--launcher.library
../plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_1.1.400.v20160518-1444
--launcher.defaultAction
openFile
--launcher.GTK_version
2
-eclipse.keyring
@user.home/.xmind/secure_storage_linux
-vm
/usr/lib/jvm/java-8-openjdk-amd64/bin
-vmargs
-Dfile.encoding=UTF-8

```
#保存退出,打开软件使用吧。

```
sudo ./XMind
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181124110659124.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)感谢(https://segmentfault.com/a/1190000015338040)

# 指定GPU以及用量
１．在终端执行程序时指定GPU  

```
CUDA_VISIBLE_DEVICES=0    python  your_file.py  # 指定GPU集群中第一块GPU使用,其他的屏蔽掉
CUDA_VISIBLE_DEVICES=1           Only device 1 will be seen
CUDA_VISIBLE_DEVICES=0,1         Devices 0 and 1 will be visible
CUDA_VISIBLE_DEVICES="0,1"       Same as above, quotation marks are optional 多GPU一起使用
CUDA_VISIBLE_DEVICES=0,2,3       Devices 0, 2, 3 will be visible; device 1 is masked
CUDA_VISIBLE_DEVICES=""          No GPU will be visible
```

 




２．在Python代码中指定GPU

```
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  　#指定第一块gpu

```



３．设置定量的GPU使用量

```
config = tf.ConfigProto() 
config.gpu_options.per_process_gpu_memory_fraction = 0.9 # 占用GPU90%的显存 
session = tf.Session(config=config)

```
４设置最小的GPU使用量

```
config = tf.ConfigProto() 
config.gpu_options.allow_growth = True 
session = tf.Session(config=config)
```
感谢(https://blog.csdn.net/alxe_made/article/details/80471739)

