uname -a 
查看系统信息。

检查ubuntu版本。
```
daiyi@hptf01-SYS-7048GR-TR:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 17.10
Release:	17.10
Codename:	artful

```
cuda 选择　下载。
(https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1704&target_type=debnetwork)

接着照着上面的操作做就是了。

官网上有 cudnn的安装指导。　

## 报错处理
unsupported GNU version! gcc versions later than 6 are not supported
```
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-6 10
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 10
```



