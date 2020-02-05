##正常的安装流程
lspci -vnn|grep VGA -A 12     看GPU，


sudo /etc/init.d/lightdm stop切换命令或者sudo /etc/init.d/kdm stop，关闭相应的GUI服务即可

cat /proc/driver/*   #查看目前的驱动。
lspci|grep -i nvidia
lspci -vnn|grep VGA -A 12  #看看有哪些显卡。

```
daiyi@hptf01-SYS-7048GR-TR:~$ lspci |grep -i nvidia
02:00.0 VGA compatible controller: NVIDIA Corporation GP102 [TITAN Xp] (rev a1)
02:00.1 Audio device: NVIDIA Corporation GP102 HDMI Audio Controller (rev a1)
03:00.0 VGA compatible controller: NVIDIA Corporation GP102 [TITAN Xp] (rev a1)
03:00.1 Audio device: NVIDIA Corporation GP102 HDMI Audio Controller (rev a1)
83:00.0 VGA compatible controller: NVIDIA Corporation GP102 [TITAN Xp] (rev a1)
83:00.1 Audio device: NVIDIA Corporation GP102 HDMI Audio Controller (rev a1)
84:00.0 VGA compatible controller: NVIDIA Corporation GP102 [TITAN Xp] (rev a1)
84:00.1 Audio device: NVIDIA Corporation GP102 HDMI Audio Controller (rev a1)
`(查看显卡型号：lspci |grep VGA （lspci是linux查看硬件信息的命令），
屏幕会打印出主机的集显几独显信息
查看nvidia芯片信息：lspci |grep -i nvidia，
会打印出nvidia系列的硬件信息，如果主机安装了没有视频输出的GPU（如tesla系列），这个命令会很有用)
```


cat /proc/version
uname -a
getconf LONG_BIT  #看看系统是 32位的还是 64位的。
sudo wget http://cn.download.nvidia.com/XFree86/Linux-x86_64/390.87/NVIDIA-Linux-x86_64-390.87.run   
#在官网下载 https://www.geforce.cn/drivers 合适的版本。
##http://us.download.nvidia.com/XFree86/Linux-x86_64/361.93.03/NVIDIA-Linux-x86_64-361.93.03.run  ##361.93的版本。
##搜索版本，还是google来的快。

sudo ls -lh /etc/modprobe.d/blacklist.conf    #修改权限
sudo chmod  +x  /etc/modprobe.d/blacklist.conf 
sudo ls -lh /etc/modprobe.d/blacklist.conf 
  
yes|sudo apt install yum gcc make vim 
yes|sudo apt install gedit

   #修改文件。添加  下面两句。(避免循环登陆)
#sudo gedit /etc/modprobe.d/blacklist.conf 
sudo vim /etc/modprobe.d/blacklist.conf 

blacklist nouveau            
optionals nouveau modeset=0


   
   
sudo update-initramfs -u   #升级
sudo reboot   #重启机器


sudo /etc/init.d/lightdm stop   #将 X server停掉。
sudo sh NVIDIA-Linux-x86_64-390.87.run
cat /proc/driver/nvidia/version 
 
nvidia-smi    #看看驱动安装好没？

#######但是，坑总是猝不及防的。

 Error! Bad return status for module build on kernel: 4.15.0-36-generic (x86_64)                                                                                                                                                        
 ```
 ERROR: Failed to run `/usr/sbin/dkms build -m nvidia -v 367.57 -k 4.15.0-36-generic`:   
         Kernel preparation unnecessary for this kernel.  Skipping...                                                                                                                                                                               
            
         Building module:                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
         cleaning build area....                                                                                                                                                                                                                
 	   'make' -j32 NV_EXCLUDE_BUILD_MODULES='' KERNEL_UNAME=4.15.0-36-generic modules.....(bad exit status: 2)                                                                                                                                
 		ERROR (dkms apport): binary package for nvidia: 367.57 not found                                                                                                                                                                       
			Error! Bad return status for module build on kernel: 4.15.0-36-generic (x86_64)                                                                                                                                                        
			Consult /var/lib/dkms/nvidia/367.57/build/make.log for more information. 
```

```
ERROR: Failed to install the kernel module through DKMS. No kernel module was installed; please try installing again without DKMS, or check the DKMS logs for more information.

ERROR: Installation has failed.  Please see the file '/var/log/nvidia-installer.log' for details.  You may find suggestions on fixing installation problems in the README available on the Linux driver download page at www.nvidia.com. 
```
##接着你查看日志，/usr/sbin/dkms build -m nvidia -v 367.57 -k 4.15.0-36-generic
得到了关键报错` error: #error "This driver requires the ability to change memory types!"
#error "This driver requires the ability to change memory types!"`

#此处感谢前人踩过的坑，
https://forums.geforce.com/default/topic/1023640/can-t-build-linux-kmod-driver/
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181101180409893.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/20181101182338424.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)

##继续做， 还是会遇到坑，
再次借鉴学习
https://blog.csdn.net/Adam_liu94/article/details/79644282

https://jingluwang.blogspot.com/2017/10/nvidia-driver-version-mismatch-which.html

# 版本1
```
Failed to initialize NVML: Driver/library version mismatch.<br>
```
#Nvidia driver 的版本没有更新，一般情况下，重启机器就能够解决，如果因为某些原因不能够重启的话，也有办法reload kernel mod

sudo rmmod nvidia
sudo nvidia-smi
nvidia-smi 发现没有 kernel mod 会将其自动装载。

#下载失败
```
$ sudo rmmod nvidia
rmmod: ERROR: Module nvidia is in use by: nvidia_modeset nvidia_uvm
```
##查看下有哪些
```
$lsmod | grep nvidia
nvidia_uvm            647168  0
nvidia_drm             53248  0
nvidia_modeset        790528  1 nvidia_drm
nvidia              12144640  152 nvidia_modeset,nvidia_uvm            12144640  152 nvidia_modeset,nvidia_uvm
```
先查看下有哪些进程使用了 nvidia*

```
sudo lsof -n -w  /dev/nvidia*
```
这些进程有个了解，如果一会卸载失败，记得关闭相关进程。

卸载
```
sudo rmmod nvidia_uvm
sudo rmmod nvidia_modeset
```


再 lsof 一遍，如果 nvidia 的使用 Used by 还没有降到 0，kill 相关进程

最后。 这里应该据好了。
```
sudo rmmod nvidia
```

## 版本2

下载NVIDIA-Linux-x86_64-390.12.run文件安装之后(为了支持cuda 9.0),发现出现下面的错误：

```
Failed to initialize NVML: Driver/library version mismatch
```
因为之前安装了384.111版本的驱动，升级后可能存在不兼容等情况。解决办法是先卸载掉所有nvidia驱动。然后再安装。卸载办法为：

```
sudo nvidia-uninstall
```


如果卸载不掉的话，执行下面的命令，删掉所有的相关文件:
```
sudo apt-get purge nvidia-*
sudo apt-get remove --purge nvidia-\*
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
```

删除文件之前，可以先看看nvidia文件都在哪些地方
```
sudo find -iname nvidia
```
然后执行安装：
```
sudo apt-get install nvidia-390
```


注意：安装nvidia时最好不要下载官网上的run文件来安装，容易出错。直接执行apt-get安装即可

###最后，还是没能解决坑，算了，就先默认安装一个系统的驱动吧。


参考链接：https://blog.csdn.net/u012897374/article/details/79966794 
参考(https://blog.csdn.net/Adam_liu94/article/details/79644282)
参考链接(https://forums.geforce.com/default/topic/1023640/can-t-build-linux-kmod-driver/)
