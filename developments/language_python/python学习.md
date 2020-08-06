<!-- TOC -->

- [给函数参数增加元信息](#给函数参数增加元信息)
- [断点](#断点)
- [断言](#断言)
- [log](#log)
- [whl 安装](#whl-安装)
- [把函数当参数传递](#把函数当参数传递)

<!-- /TOC -->

官方文档(https://docs.python.org/zh-cn/3/library/typing.html)
cookbook(https://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p03_attach_informatinal_matadata_to_function_arguments.html)

### 给函数参数增加元信息

你写好了一个函数，然后想为这个函数的参数增加一些额外的信息，这样的话其他使用者就能清楚的知道这个函数应该怎么使用。
解决方案

使用函数参数注解是一个很好的办法，它能提示程序员应该怎样正确使用这个函数。 例如，下面有一个被注解了的函数：

```
def add(x:int, y:int) -> int:
    return x + y
```
python解释器不会对这些注解添加任何的语义。它们不会被类型检查，运行时跟没有加注解之前的效果也没有任何差距。 然而，对于那些阅读源码的人来讲就很有帮助啦。第三方工具和框架可能会对这些注解添加语义。同时它们也会出现在文档中。
```
Help on function add in module __main__:
add(x: int, y: int) -> int
```

尽管你可以使用任意类型的对象给函数添加注解(例如数字，字符串，对象实例等等)，不过通常来讲使用类或者字符串会比较好点

```
函数接受并返回一个字符串，注释像下面这样:

def greeting(name: str) -> str:
    return 'Hello ' + name
    
  在函数 greeting 中，参数 name 预期是 str 类型，并且返回 str 类型。子类型允许作为参数。
```

###  断点
    # 此处为断点
    # sys.exit(0)

### 断言
assert




assert condition
assert condition,'str'

用来让程序测试这个condition，true,就忽略，　如果condition为false，那么raise一个AssertionError出来。逻辑上等同于：

```
if not condition:
    raise AssertionError()
```
例子如下
```
>>> assert 1==1

>>> assert 1==0
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    assert 1==0
AssertionError

>>> assert True

>>> assert False
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    assert False
AssertionError

>>> assert len(lists) >=5,'列表元素个数小于5'
Traceback (most recent call last):
File "D:/Data/Python/helloworld/helloworld.py", line 1, in <module>
assert 2>=5,'列表元素个数小于5'
AssertionError: 列表元素个数小于5

>>> assert 2==1,'2不等于1'
Traceback (most recent call last):
File "D:/Data/Python/helloworld/helloworld.py", line 1, in <module>
assert 2==1,'2不等于1'
AssertionError: 2不等于1
```
```
assert r.status_code == HTTPStatus.OK, '{}, {}'.format(
            r.status_code, r.text)
        ## 如果不等于，就报错，并输出　r.status_code, r.text．
```
参考链接(https://www.cnblogs.com/hezhiyao/p/7805278.html)
### log

```
def get_logger(loggerName):
    logfilePath = "/var/log/{}.log".format(loggerName)
    myLogger = logging.getLogger(loggerName)
    myLogger.setLevel(logging.INFO)
   mylog_logHandler = TimedRotatingFileHandler(logfilePath, when='midnight', interval=1, backupCount=7)
    logFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
   mylog_logHandler.setFormatter(logFormatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(logFormatter)
    streamHandler.setLevel(logging.WARNING)
    myLogger.propagate = False
    myLogger.addHandler(streamHandler)
    myLogger.addHandler(mylog_logHandler)
    return myLogger
```

```
prometheus_send_webserverLogger = get_logger("prometheus_send_webserverLogger")
prometheus_agentLogger = get_logger("prometheus_agentLogger")

def main():
	while True:
        try:
            metrics = json.loads(rawData)
            if len(metrics) > 0:
                name = metrics[0]['name']
                if name not in ignore_metrics:
                    prometheus_agentLogger.info(
                        'Received metrics: {0}'.format(metrics))
                jsonschema.validate(metrics, metricsSchema)
        except Exception as e:
            prometheus_agentLogger.warning(
                "Can not parse to json: {}, err: {}".format(rawData, e))
            continue
  
```
最后来个例子  logging.getLogger()

```
import logging
 
# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/temp/myapp.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
 
# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')
 
# Now, define a couple of other loggers which might represent areas in your
# application:
 
logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')
 
logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')

运行后，在终端看到的结果

root        : INFO     Jackdaws love my big sphinx of quartz.
myapp.area1 : INFO     How quickly daft jumping zebras vex.
myapp.area2 : WARNING  Jail zesty vixen who grabbed pay from quack.
myapp.area2 : ERROR    The five boxing wizards jump quickly.

 
在日志文件中的结果

10-22 22:19 root         INFO     Jackdaws love my big sphinx of quartz.
10-22 22:19 myapp.area1  DEBUG    Quick zephyrs blow, vexing daft Jim.
10-22 22:19 myapp.area1  INFO     How quickly daft jumping zebras vex.
10-22 22:19 myapp.area2  WARNING  Jail zesty vixen who grabbed pay from quack.
10-22 22:19 myapp.area2  ERROR    The five boxing wizards jump quickly.
```
发现DEBUG信息只有在文件中出现，这是因为StreamHandler中setLevel是INFO，可以看出Logger.setLevel()和handler.setLevel()的区别    
参考链接(https://www.cnblogs.com/captain_jack/archive/2011/01/21/1941453.html)



### whl 安装
whl格式本质上是一个压缩包，里面包含了py文件，以及经过编译的pyd文件。使得可以在不具备编译环境的情况下，选择合适自己的python环境进行安装。
安装方法很简单，进入命令行输入
pip install xxxx.whl

或者如果是升级
pip install -U xxxx.whl

即可。

### 把函数当参数传递
```
from optparse import OptionParser


def get_options():
    parser = OptionParser()
    parser.add_option("--debug_flag",
                      dest="debug_flag",
                      default="False",
                      help="It is for debug.the value is 'True' or 'Flase'")
    (options, args) = parser.parse_args()
    return options

DEBUG_FLAG = options.debug_flag

def try_debug(debug_flag,func,mode="order",*args,**kwargs):
    if mode == "order" :
        if debug_flag == "True":
            func(*args,**kwargs)
    elif mode == "reverse" :
        if debug_flag != "True":
            func(*args,**kwargs)
    else:
        pass


save_path = str(time.strftime(
        "%Y.%m.%d.%H.%M.%S", time.localtime())) + "_diff"
save_path = os.path.join(PUBLIC_SERVICENAME, save_path)
save_diff(content_diff_file_list,PUBLIC_SERVICENAME, save_path)
_to_debug(DEBUG_FLAG,logger.info,'order',"Successed ,writing the content of diffing into files is done.")
_to_debug(DEBUG_FLAG,logger.info,'order',"Prepared to diff the %s and already_known_diff" % save_path )
diff_new_and_already(save_path,os.path.join(PUBLIC_SERVICENAME,"already_known_diff"))
_to_debug(DEBUG_FLAG,logger.info,'order',"Successed ,diff the %s and already_known_diff is done." % save_path)

    
_to_debug(DEBUG_FLAG,exec_cmd,'reverse',"rm -rf %s %s " % (LOCAL_APSARA_PATH, LOCAL_PUBLIC_PATH))
_to_debug(DEBUG_FLAG,exec_cmd,'reverse',"rm -rf %s/src/common_file_list %s/fixed/common_file_list" % (save_path,save_path))
  ```
