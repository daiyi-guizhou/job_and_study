
#### nanomsg

nanomsg是ZeroMQ作者用C语言重写的一个Socket库，其用法和模式和ZeroMQ差不多，但是具有更好的性能和更完善的接口。

首先下载源码
```
wget https://github.com/nanomsg/nanomsg/archive/1.0.0.tar.gz -O nanomsg-1.0.0.tar.gz

首先确保你ubuntu上已经安装gcc gcc-c++ python-devel cmake ，如果没有执行
apt-get install gcc gcc-c++ python-devel cmake


编译安装nanomsg
tar -zxvf nanomsg-1.0.0.tar.gz
cd nanomsg-1.0.0
mkdir bulid
# 这一步如果出现问题，需要删除CMakeCache.txt重新cmake
cd build
cmake ..
cmake --build .
# 执行测试
ctest -C Debug .
# 安装
cmake --build . --target install
ldconfig

安装调试
pip3 install nnpy
```




安装测试

```
import nnpy
 
pub = nnpy.Socket(nnpy.AF_SP, nnpy.PUB)
pub.bind('inproc://foo')
 
sub = nnpy.Socket(nnpy.AF_SP, nnpy.SUB)
sub.connect('inproc://foo')
sub.setsockopt(nnpy.SUB, nnpy.SUB_SUBSCRIBE, '')
 
pub.send('hello, world')
print(sub.recv())
```
	



如果执行成功则大功告成

注意：如果需要安装nanomsg则需要安装，下载安装包，进入目录执行
```
python setup.py install
```
即可

转载来自(https://www.cnblogs.com/flash55/p/9129509.html)
