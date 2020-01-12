#### 管道，批次，
```
def echo_in_log(metric,threshold):
    top1_info = subprocess.Popen(["top", "-n", "1","-b"],stdout=subprocess.PIPE)
    top_info = subprocess.Popen(["head","-n","30"],stdin=top1_info.stdout,stdout=subprocess.PIPE)
    out, err = top_info.communicate() 
    #output info get from console has many unicode escape character ,such as \x1b(B\x1b[m\x1b[39;49m\x1b[K\n\x1b(B\x1b[m
    #use decode('unicode-escape') to process 
    out_info = out.decode('unicode-escape') 

    topLogger.info("now this {metric} is lower than the threshold{threshold}, now top_info is {top_info}".format(metric=metric,threshold=threshold,top_info=out_info))
```
top 是　动态查看，
n 设置退出前屏幕刷新的次数
b 将top输出编排成适合输出到文件的格式，可以使用这个选项创建进程日志
这里用 top -n 1 -b, 
其中， 执行脚本报错　TERM environment variable not set.　用 top -b 就解决了

```
使用top命令报错的原因是：在Linux下使用top命令需要指定终端类型，也就是一个“TERM” 的环境变量。

可执行如下命令：

# top
TERM environment variable not set.
```
###### 日志格式
 out_info = out.decode('unicode-escape')   是因为得到的 top　信息里含有二进制格式，需要去除。　
 有的看起来正常，但是vim 查看就有问题，　有的直接用脚本执行的时候就报错，　有的cat查看就报错。
### 管道，
由于　top -n 1 -b 的信息太长，需要截取下，　所以使用了 PIPE,  
这里就曾走过很多弯路。

```
status,data = subprocess.getstatusoutput(" top -n 1 -b | head -n 30 ")  
这里得到的data格式错误，
data = subprocess.call(" top -n 1 -b | head -n 30 ") 
这里得到的data 不能保存，只能显示在屏幕上，
还有的subprocess　不接受 (" top -n 1 -b | head -n 30 ")  中的 "| " ,所以报错。
 
```
#### int把字符转数字，
  idle_mem = int(idle_mem)   ## 这里 用，long，float,　不知道为什么, python3 执行的时候，总是报错
```
def idles_mem_cpu():
    sta1,total_mem=subprocess.getstatusoutput("top -n 1 -b| grep 'Mem :' | awk '{print $4}'")
    sta2,idle_mem=subprocess.getstatusoutput("top -n 1 -b | grep 'Mem :' | awk '{print $6}'")
    #print("total_mem,idle_mem ",total_mem,sta1,sta2,idle_mem)


    idle_mem = int(idle_mem)   ## 这里 用，long，float,　不知道为什么, python3 执行的时候，总是报错
    total_mem = int(total_mem)
    mem_id=idle_mem*100/total_mem

    mem_id=float(mem_id)
    sta3,cpu_id=subprocess.getstatusoutput("top -n 1 -b| grep Cpu | awk -F' ' '{print $8}' ")
    #print(cpu_id)

    cpu_id=float(cpu_id)
    #print(mem_id,cpu_id)
    return mem_id,cpu_id
```

