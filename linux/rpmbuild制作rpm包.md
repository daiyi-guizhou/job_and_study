 
 
# rpmbuild

## 安装 rpmbuild 工具
[rpm-build的安装，创建目录等](https://blog.51cto.com/13689359/2165975)

## 资源下载
[mysql-connector-python源码包](https://yuque.antfin-inc.com/sls/private_cloud/tilsa0#6N5qk)
[dns_python 源码包](http://www.dnspython.org/kits/1.2.0/)
[protobuf源码包](https://github.com/protocolbuffers/protobuf/releases)
[非root用户安装protobuf的python依赖到指定目录](https://blog.csdn.net/thumbcs/article/details/80946171)



## 编写 spec 文件
https://cloud.tencent.com/developer/article/1444873
https://blog.csdn.net/wf1982/article/details/6636157
https://blog.csdn.net/wf1982/article/details/6626694
示例 
```
#cat /home/rpmbuild/rpmbuild/SPECS/daiyi_mysql_three.spec
Summary: Mysql.connector_python
Name: mysql-connector-python
Version: 8.0.19
Release: 1%{?dist}
License: GNU GPLv2 (with FOSS License Exception)
Group: Development/Languages
Packager: daiyi <847210821@qq.com>
URL: https://pypi.tuna.tsinghua.edu.cn/simple/mysql-connector-python/
AutoReqProv: no

Source0: mysql-connector-python-%{version}.tar.gz
Source1: dnspython-1.2.0.tar.gz
Source2: protobuf-python-3.11.4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: x86_64

#Requires: protobuf>=3.6.1, dnspython>=1.16.0

%description
MySQL driver written in Python which does not depend on MySQL C client
libraries and implements the DB API v2.0 specification (PEP-249).

%setup
%prep
cat << \EOF > ./%{name}-%{version}/%{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(Net::SNMP)/d'
EOF
%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
chmod 755 %{__perl_requires}
#%prep
%setup -b 0
%setup -b 1
%setup -b 2

%build
python setup.py build
cd ..
cd dnspython-1.2.0/
python setup.py build
export PYTHONPATH=$RPM_BUILD_ROOT/home/tops/lib/python2.7/site-packages/
mkdir -p $RPM_BUILD_ROOT/home/tops/lib/python2.7/site-packages
cd ..
cd protobuf-3.11.4
./configure --prefix=$RPM_BUILD_ROOT/home/tops
make && make install
#export PATH=$RPM_BUILD_ROOT/home/tops/bin:$PATH
cd ./python
python setup.py build


%install
export PYTHONPATH=$RPM_BUILD_ROOT/home/tops/lib/python2.7/site-packages/
mkdir -p $RPM_BUILD_ROOT/home/tops/lib/python2.7/site-packages
cd ..
cd protobuf-3.11.4/python
python setup.py install --prefix=$RPM_BUILD_ROOT/home/tops
cd ../../mysql-connector-python-8.0.19
python setup.py install --prefix=$RPM_BUILD_ROOT/home/tops
cd ..
cd dnspython-1.2.0/
python setup.py install --prefix=$RPM_BUILD_ROOT/home/tops

%files
%defattr(-,root,root)
%define debug_package %{nil}
/home/tops/lib/python2.7/site-packages/mysql_connector_python-8.0.19-py2.7.egg-info/*
/home/tops/lib/python2.7/site-packages/mysql/*
/home/tops/lib/python2.7/site-packages/mysqlx/*
/home/tops/lib/python2.7/site-packages/dns/*
/home/tops/lib/python2.7/site-packages/dnspython-1.2.0-py2.7.egg-info
/home/tops/bin/easy_install
/home/tops/bin/easy_install-3.6
/home/tops/lib/python2.7/site-packages/easy-install.pth
/home/tops/lib/python2.7/site-packages/protobuf-3.11.4-py2.7.egg/
/home/tops/lib/python2.7/site-packages/setuptools.pth
/home/tops/lib/python2.7/site-packages/site.py
/home/tops/lib/python2.7/site-packages/site.pyc
/home/tops/lib/python2.7/site-packages/site.pyo
```
## 使用

/home/rpmbuild/rpmbuild 是工作目录，  
把源码包放在  /home/rpmbuild/rpmbuild/SOURCES/ 下，
spec 的文件放在 /home/rpmbuild/rpmbuild/SPECS/ 目录下
接着执行  rpmbuild -ba /home/rpmbuild/rpmbuild/SPECS/*.spec  
原则上这样就可以了， 但是如果有报错的话，需要解。
```
## /home/rpmbuild/rpmbuild 是工作目录，  把源码包放在  /home/rpmbuild/rpmbuild/SOURCES/ 下，spec 的文件放在 /home/rpmbuild/rpmbuild/SPECS/ 目录下 

[root@a34h05001.cloud.h05.amtest87 /home/rpmbuild/rpmbuild] 25E_ops1,请不要把文件放在root目录下
#ls
BUILD  BUILDROOT  RPMS  SOURCES  SPECS  SRPMS

[root@a34h05001.cloud.h05.amtest87 /home/rpmbuild/rpmbuild] 25E_ops1,请不要把文件放在root目录下
#ls SOURCES/
dnspython-1.2.0.tar.gz  mysql-connector-python-8.0.19.tar.gz  protobuf-python-3.11.4.tar.gz

[root@a34h05001.cloud.h05.amtest87 /home/rpmbuild/rpmbuild] 25E_ops1,请不要把文件放在root目录下
#ls SPECS/
daiyi_mysql_three.spec

[root@a34h05001.cloud.h05.amtest87 /home/rpmbuild/rpmbuild] 25E_ops1,请不要把文件放在root目录下
#ls RPMS/x86_64/mysql-connector-python-8.0.19-1.alios7.x86_64.rpm
RPMS/x86_64/mysql-connector-python-8.0.19-1.alios7.x86_64.rpm

[root@a34h05001.cloud.h05.amtest87 /home/rpmbuild/rpmbuild] 25E_ops1,请不要把文件放在root目录下
#rpmbuild  -ba SPECS/daiyi_mysql_three.spec
```


## 解决报错

[error: Empty %files file /home/rpmbuild/rpmbuild/BUILD/ debugfile.llis](https://blog.csdn.net/qq_41922018/article/details/103905243)
[rpmbuild打包遇到问题汇总](https://blog.csdn.net/u014007037/article/details/78727526)
/usr/lib/rpm/macros中添加%debug_package %{nil}


[Found ‘${BUILDROOT}’ in installed files; aborting](http://adam.younglogic.com/2010/05/found-buildroot-in-installed-files-aborting/)

[does NOT support .pth files](https://blog.csdn.net/yuan_lo/article/details/48289317)

[rpmbuild  PYTHONPATH environment variable currently contains: ''](https://segmentfault.com/q/1010000010587830)
[libtool: error: error: cannot install 'libprotoc.la' to a directory not endi](https://blog.csdn.net/qq_25147897/article/details/78544395)





# 特别需要注意的是：%install部分使用的是绝对路径，而%file部分使用则是相对路径，虽然其描述的是同一个地方。千万不要写错。

## 解决依赖

### 依赖项  
`rpm -qpR *.rpm `抽出依赖
```
[root@vm010138025241 /tmp/xtermupload]
#rpm -qpR mysql-connector-python-8.0.19-1.alios7.x86_64.rpm
/usr/local/bin/python

rpmlib(CompressedFileNames) <= 3.0.4-1
rpmlib(FileDigests) <= 4.6.0-1
rpmlib(PartialHardlinkSets) <= 4.0.4-1
rpmlib(PayloadFilesHavePrefix) <= 4.0-1
rpmlib(PayloadIsXz) <= 5.2-1
```

### 解决
* 1 假如需要在 rpmbuild 生成软件包, 在安装时候忽略依赖关系，请在 spec 文件中添加下面参数 ----- # 解决了/usr/local/bin/python
    `AutoReqProv: no`

* 2 在 宏 里添加  ----- # 解决了 rpmlib 的依赖
```
    %_binary_payload    w9.gzdio
    %_binary_filedigest_algorithm   1
```

例子如下
```
#cat ~/.rpmmacros
%_topdir        /home/rpmbuild/rpmbuild
%debug_package %{nil}
%_binary_payload w9.gzdio
%_binary_filedigest_algorithm 1
```

## 备注一些
* Linux下yum命令安装.rpm文件时提示“ is not signed ”的解决办法
   yum命令安装rpm包时提示"Package filename.rpm is not signed"，只需编辑
    /etc/yum.conf中的"gpgcheck=1"这一行改为"gpgcheck=0"即可
    yum --nogpgcheck 即可。


* 把spec里的BuildRequires:去掉！

* yum localinstall *.rpm -nogpgcheck
    rpm -qpR file.rpm　　　　　　　＃[查看包]依赖关系
    rpm2cpio file.rpm |cpio -div    ＃[抽出文件]