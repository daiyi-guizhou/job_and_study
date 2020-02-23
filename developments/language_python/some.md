<!-- TOC -->

- [线程池](#线程池)
- [python 算法与数据结构](#python-算法与数据结构)
- [log   有  输出到 控制台。](#log---有--输出到-控制台)
- [把 一些常用的  处理  写成 标准函数，  以后直接引用 就可以了，](#把-一些常用的--处理--写成-标准函数--以后直接引用-就可以了)
- [类库地址](#类库地址)
- [装饰器](#装饰器)
- [parser.parseargs()](#parserparseargs)

<!-- /TOC -->

## 线程池
	 python 线程池 https://juejin.im/post/5cf913cfe51d45105d63a4d0
	 python  传参 传入的是 地址。 
		 https://dasuda.top/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2018/09/22/Python%E4%B8%AD%E5%87%BD%E6%95%B0%E4%BC%A0%E5%85%A5%E7%9A%84%E5%8F%82%E6%95%B0%E5%88%B0%E5%BA%95%E6%98%AF%E5%80%BC%E8%BF%98%E6%98%AF%E5%9C%B0%E5%9D%80/
```
def test1(val):
    val[1]=0
    print('test1:'+str(id(val)))

b1=[0,1,2,3]
print('b1:'+str(id(b1)))
test1(b1)
print(b1)

Output：
	b1:2232273138760
	test1:2232273138760
	[0, 0, 2, 3]
	
def test2(val):
    val=[0,2,5]
    print('test2:'+str(id(val)))

b2=[0,1,2,3]
print('b2:'+str(id(b2)))
test2(b2)
print(b2)

Output：
	b2:2232273138824
	test2:2232273139144
	[0, 1, 2, 3]
```

## python 算法与数据结构      
		https://www.ranxiaolang.com/static/python_algorithm/chapter2/section2.html
		 https://runestone.academy/runestone/books/published/pythonds/index.html
	mysqldiff   python中用来diff 数据库的    

https://docs.oracle.com/cd/E17952_01/mysql-utilities-1.5-en/mysqldiff.html
		1 单向循环链表     使用上的示例？？？

## log   有  输出到 控制台。
		子主题
```
[loggers]
keys=root

[handlers]
keys=rootFileHandler, consoleHandler

[formatters]
keys=completeFormatter

[logger_root]
level=INFO
handlers=rootFileHandler, consoleHandler

[handler_rootFileHandler]
class=logging.handlers.RotatingFileHandler
level=INFO
formatter=completeFormatter
args=('log/start.log','a',2000000,10,)

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=completeFormatter
args=(sys.stdout,)

[formatter_completeFormatter]
format=%(asctime)s - %(process)s - %(name)s - %(module)s.%(funcName)s:%(lineno)s - %(levelname)s - %(message)s
```

```			
# !/home/tops/bin/python
# -*- coding:utf-8 -*-

import logging.config
import os

def get_logger(name=None, save_dir="log"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    conf_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             "config", "logging.conf")
    logging.config.fileConfig(conf_path)
    return logging.getLogger(name)
			 self._logger = get_logger(os.path.join(sys.path[0],self.__class__.__name__))

self._logger.error('MakeResource error: %s' % e.get_error_message())
```

## 把 一些常用的  处理  写成 标准函数，  以后直接引用 就可以了， 
			
```            
# !/home/tops/bin/python
# -*- coding:utf-8 -*-

import hashlib
import json
import os

from command_executor import exec_cmd


def check_path(path):
    if not os.path.exists(path):
        raise Exception("the path is not exist, path=%s" % path)


def cal_md5(file_path):
    with open(file_path) as f:
        content = f.read()
        return hashlib.md5(content).hexdigest()


def chkconfig_del(name):
    exec_cmd("sudo chkconfig --del %s" % name)


def load_json_from_file(filename):
    with open(filename, "r") as f:
        content = f.read()
        return json.loads(content)

def dump_json_to_file(dest, rootJson={}):
    with open(dest, "w") as f:
        f.write(json.dumps(rootJson, indent=4))

def get_os_info():
    with open("/etc/issue", "r") as f:
        content = f.read()
        return content.split("\n")[0]
```

```
# !/home/tops/bin/python
# -*- coding:utf-8 -*-
import subprocess
from logging_helper import get_logger

logger = get_logger()


def exec_cmd(cmd, throw=True):
    logger.info("Prepare to execute cmd, cmd=[%s]" % cmd)
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    stdout = stdout.strip("\n")
    stderr = stderr.strip("\n")
    if p.returncode:
        if throw:
            raise ExecCmdException(cmd, p.returncode, stdout, stderr)
    return p.returncode, stdout, stderr


def exec_rpc_cmd(cmd, throw=True):
    """
    exec apsara rpc command
    :param cmd:
    :param throw
    :return:
    """
    return exec_cmd("{} {}".format("/apsara/deploy/rpc_wrapper/rpc.sh", cmd),
                    throw)


class ExecCmdException(Exception):
    def __init__(self, cmd, status, stdout, stderr):
        self.cmd = cmd
        self.status = status
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        return "execute cmd failed, cmd=[%s], status=[%s], stdout=[%s], stderr=[%s]" % (
            self.cmd, self.status, self.stdout, self.stderr)
```

## 类库地址
首先使用 sys 下的 path 变量查看所有的 python 路径：

import sys
sys.path
1
2
标准库

lib 目录下（home 目录/pythonXX.XX/lib）
第三方库

在 lib 下的 site-packages 目录下
home 目录/pythonXX.XX/lin/site-packages/
>> import moudle
>> module.__file__
1
2
如：

>> import theano
>> theano.__file__
/home/bigdata/anaconda2/lib/python2.7/site-packages/theano/__init__.pyc

————————————————

版权声明：本文为CSDN博主「Inside_Zhang」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。

原文链接：https://blog.csdn.net/lanchunhui/article/details/70160039
	 
## 装饰器
```
def log(func):
    def wrapper(self, *args, **kw):
        self._logger.info("Prepare to test %s,project=%s, _logstore=%s " %
                          (func.__name__, self._project, self._logstore))
        func(self, *args, **kw)
        self._logger.info("Test of %s is over,project=%s, _logstore=%s " %
                          (func.__name__, self._project, self._logstore))

    return wrapper
		 https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
		 https://www.runoob.com/w3cnote/python-func-decorators.html
```	 

## parser.parse_args()
一、介绍
argparse是python用于解析命令行参数和选项的标准模块，用于代替已经过时的optparse模块。argparse模块的作用是用于解析命令行参数。

我们很多时候，需要用到解析命令行参数的程序。



二、使用步骤
我们常常可以把argparse的使用简化成下面四个步骤

1：import argparse

2：parser = argparse.ArgumentParser()

3：parser.add_argument()

4：parser.parse_args()

上面四个步骤解释如下：首先导入该模块；然后创建一个解析对象；然后向该对象中添加你要关注的命令行参数和选项，每一个add_argument方法对应一个你要关注的参数或选项；最后调用parse_args()方法进行解析；解析成功之后即可使用。

三、例子讲解
下面我们通过一个例子来进行讲解说明

我们可以看到上面的第二个步骤，parser = argparse.ArgumentParser()

它的作用就是：当调用parser.print_help()或者运行程序时由于参数不正确(此时python解释器其实也是调用了pring_help()方法)时，会打印这些描述信息，一般只需要传递description参数。

下面会有例子输出，首先给出代码：
```
#-*- coding: UTF-8 -*-
import argparse   #步骤一

def parse_args():
    """
    :return:进行参数的解析
    """
    description = "you should add those parameter"                   # 步骤二
    parser = argparse.ArgumentParser(description=description)        # 这些参数都有默认值，当调用parser.print_help()或者运行程序时由于参数不正确(此时python解释器其实也是调用了pring_help()方法)时，
                                                                     # 会打印这些描述信息，一般只需要传递description参数，如上。
    help = "The path of address"
    parser.add_argument('--addresses',help = help)                   # 步骤三，后面的help是我的描述
    args = parser.parse_args()                                       # 步骤四          
    return args

if __name__ == '__main__':
    args = parse_args()
    print(args.addresses)            #直接这么获取即可。
```
上面四个步骤已经分别对应上了，当我们在命令行敲入：

python arg.py -h 
输出提示为：


如何获得命令参数值。
我们可以直接通过args.addresses获得它的参数值。

当我们敲入python arg.py --addresses this-is-parameter-of-addresses 命令时

会输出this-is-parameter-of-addresses

到这里就总结了argparse模块常见的一些常见的用法。

参考：
http://blog.xiayf.cn/2013/03/30/argparse/

编辑于 2017-08-29
		https://zhuanlan.zhihu.com/p/28871131