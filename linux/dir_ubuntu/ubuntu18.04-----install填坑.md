# 問題１
incorrect permissions on /usr/lib/policykit-1/polkit-agent-helper-1
#sudo chmod +s /usr/lib/policykit-1/polkit-agent-helper-1

#	問題２
安装了Ubuntu18.04.  
下载了 GPU driver,结果各种报错。 
1安装了 driver，但是nvidia-smi不能用。 
2 在此基础上， 安装cuda,cudnn, 也是都不行。 
放弃了修改 、
直接使用 apt install nvidia-390
安装上了， 但是  nvidia-smi  又报错， 不能commiunicate、 
于是下载资源， 写在driver,再次安装。 還是不行，最後，借鑑前人．

主要参考资料：
https://blog.csdn.net/u011668104/article/details/79560381
https://devtalk.nvidia.com/default/topic/1000340/cuda-setup-and-installation/-quot-nvidia-smi-has-failed-because-it-couldn-t-communicate-with-the-nvidia-driver-quot-ubuntu-16-04/post/5233711/#5233711

解决方案：更新Ubuntu内核（我们服务器从Linux 3.13.0-24-generic更新至Linux 4.12.9-041209-generic），然后按照正常流程安装最新的驱动nvidia-390具体操作如下#系统内核更新
下载3个内核deb安装文件
```
wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.12.9/linux-headers-4.12.9-041209_4.12.9-041209.201708242344_all.deb
wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.12.9/linux-headers-4.12.9-041209-generic_4.12.9-041209.201708242344_amd64.deb
wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.12.9/linux-image-4.12.9-041209-generic_4.12.9-041209.201708242344_amd64.deb
```
安装内核文件
```
sudo dpkg -i *.deb
```

安装完成以后，重新启动系统，验证内核的版本
```
uname -sr
```
#重装nVidia驱动
```
sudo apt-get purge nvidia*
sudo add-apt-repository ppa:graphics-drivers
sudo apt-get update
sudo apt-get install nvidia-390
sudo reboot
```


重启后

```
lsmod | grep nvidia
```


 



#	問題３
Install Adobe Flash Player on Ubuntu 18.04 LTS Desktop
##
 解決方案
```
sudo add-apt-repository "deb http://archive.canonical.com/ $(lsb_release -sc) partner"
sudo apt update
sudo apt install adobe-flashplugin browser-plugin-freshplayer-pepperflash
```

