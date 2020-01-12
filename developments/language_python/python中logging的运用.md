参考链接(https://segmentfault.com/a/1190000003008066)
(https://blog.csdn.net/z_johnny/article/details/50812878)
# 快速应用

```
import logging
from logging.handlers import TimedRotatingFileHandler          #加载模块

gpuRebootLogFilePath = "/home/work/open-falcon/push-scripts/gpuReboot/gpuReboot.log"　　＃文件具体路径，
gpuRebootLogger = logging.getLogger("gpuReboot")　　＃名字
gpuRebootLogger.setLevel(logging.INFO)　　　　　　　　　　　　＃设置级别
gpuReboothandler = TimedRotatingFileHandler(gpuRebootLogFilePath, when='W5', interval=1, backupCount=6)　　＃设置handler
gpuRebootformatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')    		#时间格式
gpuReboothandler.setFormatter(gpuRebootformatter)
gpuRebootLogger.addHandler(gpuReboothandler)

if ts >= time_math:
            try:
                gpuRebootLogger.info("gpu is not alive,now ts is {}".format(ts))　　　　　＃INFO 的输入
                print("it is time to reboot")
                system('reboot')
            except Exception as e:
                gpuRebootLogger.error(str(e))　　　　			＃ＥＲＲＯＲ的输入
```
＃输出样式

```
root@hypereal-test-10:/home/work/open-falcon/push-scripts/gpuReboot# cat gpuReboot.log 
2018-12-04 18:32:43,046 - INFO - gpu is not alive,now ts is 1543919563
2018-12-04 18:32:46,115 - INFO - gpu is not alive,now ts is 1543919566
2018-12-04 18:32:49,189 - INFO - gpu is not alive,now ts is 1543919569
```


# 说明

1.基本元素说明：

    Logger：用于输出的日志的总对象
    Handlers：用来指定log的输出方式
    Formatters：设置日志信息的结构和内容格式，默认的时间格式为%Y-%m-%d %H:%M:%S
    Filter：过滤器，用来过滤的输出内容（如：只输出debug以上的内容）

Logger
### 常用函数

    LOG=logging.getLogger(”chat.gui”)
    Logger.setLevel(lel):指定最低的日志级别，低于lel的级别将被忽略。debug是最低的内置级别，critical为最高
    Logger.addFilter(filt)、Logger.removeFilter(filt):添加或删除指定的filter
    Logger.addHandler(hdlr)、Logger.removeHandler(hdlr)：增加或删除指定的handler
    Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()：可以设置的日志级别
    Logger.log("debug","This is a bug"):可以通过这个函数直接输出内容并选择对应的告警级别

内置级别
```
名称 	对应数字级别
NOTSET 	0
DEBUG 	10
INFO 	20
WARNING 	30
ERROR 	40
CRITICAL 	50
```

## Handlers
### 1.常用函数

    Handler.setLevel(lel):指定被处理的信息级别，低于lel级别的信息将被忽略
    Handler.setFormatter()：给这个handler选择一个格式
    Handler.addFilter(filt)、Handler.removeFilter(filt)：新增或删除一个filter对象

### 2.Handler种类

名字	说明	构造函数	其他
logging.StreamHandler	使用这个Handler可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息。	它的构造函数是：StreamHandler([strm])	其中strm参数是一个文件对象。默认是sys.stderr
logging.FileHandler	和StreamHandler类似，用于向一个文件输出日志信息。不过FileHandler会帮你打开这个文件	FileHandler(filename[,mode])	filename是文件名，必须指定一个文件名。mode是文件的打开方式。默认是’a'，即添加到文件末尾

|名字|说明|构造函数||
|:--|----|---|--|---|--|
|logging.StreamHandler|使用这个Handler可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息。|它的构造函数是：StreamHandler([strm])其中strm参数是一个文件对象。  默认是sys.stderr|||  
|logging.FileHandler|和StreamHandler类似，用于向一个文件输出日志信息。不过FileHandler会帮你打开这个文件。|它的构造函数是：FileHandler(filename[,mode])   filename是文件名，必须指定一个文件名。mode是文件的打开方式。默认是’a'，即添加到文件末尾。||
| logging.handlers.RotatingFileHandler|这个Handler类似于上面的FileHandler，但是它可以管理文件大小。当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建一个新的同名日志文件继续输出。比如日志文件是chat.log。当chat.log达到指定的大小之后，RotatingFileHandler自动把 文件改名为chat.log.1。不过，如果chat.log.1已经存在，会先把chat.log.1重命名为chat.log.2。。。最后重新创建 chat.log，继续输出日志信息。|RotatingFileHandler( filename[, mode[, maxBytes[, backupCount]]]).  其中filename和mode两个参数和FileHandler一样。maxBytes用于指定日志文件的最大文件大小。如果maxBytes为0，意味着日志文件可以无限大，这时上面描述的重命名过程就不会发生。backupCount用于指定保留的备份文件的个数。比如，如果指定为2，当上面描述的重命名过程发生时，原有的chat.log.2并不会被更名，而是被删除。||
| logging.handlers.TimedRotatingFileHandler|这个Handler和RotatingFileHandler类似,不过,它没有通过判断文件大小来决定何时重新创建日志文件，而是间隔一定时间就 自动创建新的日志文件。重命名的过程与RotatingFileHandler类似，不过新的文件不是附加数字，而是当前时间|TimedRotatingFileHandler( filename [,when [,interval [,backupCount]]])其中filename参数和backupCount参数和RotatingFileHandler具有相同的意义。interval是时间间隔。when参数是一个字符串。表示时间间隔的单位，不区分大小写。它有以下取值：S 秒 M 分   H 小时  D 天  W 每星期（interval==0时代表星期一） midnight 每天凌晨||
| logging.handlers.SocketHandler||||
| logging.handlers.DatagramHandler|以上两个Handler类似，都是将日志信息发送到网络。不同的是前者使用TCP协议，后者使用UDP协议。它们的构造函数是： Handler(host, port)  其中host是主机名，port是端口名|||
|logging.handlers.SysLogHandler||
|logging.handlers.NTEventLogHandler|
|logging.handlers.SMTPHandler||
|ogging.handlers.MemoryHandler|
|logging.handlers.HTTPHandler|

    

Formatters
参数 	含义
%(name)s 	Logger的名字
%(levelno)s 	数字形式的日志级别
%(levelname)s 	文本形式的日志级别
%(pathname)s 	调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 	调用日志输出函数的模块的文件名
%(module)s 	调用日志输出函数的模块名
%(funcName)s 	调用日志输出函数的函数名
%(lineno)d 	调用日志输出函数的语句所在的代码行
%(created)f 	当前时间，用UNIX标准的表示时间的浮点数表示
%(relativeCreated)d 	输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 	字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 	线程ID。可能没有
%(threadName)s 	线程名。可能没有
%(process)d 	进程ID。可能没有
%(message)s 	用户输出的消息

## 示例

```

    #coding:utf-8
     
    # =======================================================================
    # FuncName: console_out.py
    # Desc: output log to console and file
    # Date: 2016-02-19 17:32
    # Author: johnny
    # =======================================================================
     
    import logging
     
    def console_out(logFilename):
        ''' Output log to file and console '''
        # Define a Handler and set a format which output to file
        logging.basicConfig(
                        level    = logging.DEBUG,              # 定义输出到文件的log级别，                                                            
                        format   = '%(asctime)s  %(filename)s : %(levelname)s  %(message)s',    # 定义输出log的格式
                        datefmt  = '%Y-%m-%d %A %H:%M:%S',                                     # 时间
                        filename = logFilename,                # log文件名
                        filemode = 'w')                        # 写入模式“w”或“a”
        # Define a Handler and set a format which output to console
        console = logging.StreamHandler()                  # 定义console handler
        console.setLevel(logging.INFO)                     # 定义该handler级别
        formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  #定义该handler格式
        console.setFormatter(formatter)
        # Create an instance
        logging.getLogger().addHandler(console)           # 实例化添加handler
     
        # Print information              # 输出日志级别
        logging.debug('logger debug message')     
        logging.info('logger info message')
        logging.warning('logger warning message')
        logging.error('logger error message')
        logging.critical('logger critical message')
     
    if __name__ == "__main__":
        console_out('logging.log')
```


控制台：

    2016-03-06 14:38:49,714  console_out.py : INFO  logger info message
    2016-03-06 14:38:49,714  console_out.py : WARNING  logger warning message
    2016-03-06 14:38:49,714  console_out.py : ERROR  logger error message
    2016-03-06 14:38:49,714  console_out.py : CRITICAL  logger critical message


文件： logging.log

    2016-03-06 Sunday 14:38:49  console_out.py : DEBUG  logger debug message
    2016-03-06 Sunday 14:38:49  console_out.py : INFO  logger info message
    2016-03-06 Sunday 14:38:49  console_out.py : WARNING  logger warning message
    2016-03-06 Sunday 14:38:49  console_out.py : ERROR  logger error message
    2016-03-06 Sunday 14:38:49  console_out.py : CRITICAL  logger critical message

