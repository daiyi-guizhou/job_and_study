参考链接(https://oomake.com/question/289923)


```
hypereal@hypereal-test-10:/home/work/open-falcon/push-scripts$ cat predate.sh 
#!/bin/bash
while read line ; do
	echo "$(date): ${line}"
done
```

```
root@hypereal-test-10:/home/work/open-falcon/push-scripts# (/usr/bin/python3 /home/work/open-falcon/push-scripts/GPU-temperture.py) &>> >( bash predate.sh >> gpu1.log )
不知道为什么我需要在(前面放置>，所以<(，但这就是有效的。
```

#
#

这是一个使用像pax一样的while read循环的版本，但不需要额外的文件描述符或单独的脚本(尽管你可以使用一个)。它使用进程替换：
```
myscript.sh 2> >( while read line; do echo "$(date): ${line}"; done > error.log )
补充一点，如果你想把它放在一个文件而不是STDOUT中，你需要在'done'和')'之间插入“>> filename”，如下所示：myscript.sh >>>(读取行;做echo“$(date)：$ {line}”; done >> logfile)
```
使用pax的predate.sh：

```
myscript.sh 2> >( predate.sh > error.log )
```
详细示例
示例
如果你在谈论每一行的最新时间戳，那么你可能想在你的实际脚本中做些事情(但如果你没有权力改变它，请参阅下面的一个漂亮的解决方案)。如果您只想在脚本开始编写之前在自己的行上标记日期，我会使用：

( date 1>&2 ; myscript.sh ) 2>error.log
你需要的是通过另一个程序管道stderr的技巧，该程序可以为每一行添加时间戳。您可以使用C程序执行此操作，但使用bash则更加狡猾。 首先，创建一个脚本，为每一行添加时间戳(称为predate.sh)：
#!/bin/bash
while read line ; do
    echo "$(date): ${line}"
done
例如：
( echo a ; sleep 5 ; echo b ; sleep 2 ; echo c ) | ./predate.sh
生产：
Fri Oct  2 12:31:39 WAST 2009: a
Fri Oct  2 12:31:44 WAST 2009: b
Fri Oct  2 12:31:46 WAST 2009: c
然后你需要另一个可以交换stdout和stderr的技巧，这个小怪物在这里：
( myscript.sh 3>&1 1>&2- 2>&3- )
然后通过时间戳stdout并将其重定向到您的文件来组合这两个技巧很简单：
( myscript.sh 3>&1 1>&2- 2>&3- ) | ./predate.sh >error.log
以下记录显示了这一点：
pax> cat predate.sh
    #!/bin/bash
    while read line ; do
        echo "$(date): ${line}"
    done
pax> cat tstdate.sh
    #!/bin/bash
    echo a to stderr then wait five seconds 1>&2
    sleep 5
    echo b to stderr then wait two seconds 1>&2
    sleep 2
    echo c to stderr 1>&2
    echo d to stdout
pax> ( ( ./tstdate.sh ) 3>&1 1>&2- 2>&3- ) | ./predate.sh >error.log
    d to stdout
pax> cat error.log
    Fri Oct  2 12:49:40 WAST 2009: a to stderr then wait five seconds
    Fri Oct  2 12:49:45 WAST 2009: b to stderr then wait two seconds
    Fri Oct  2 12:49:47 WAST 2009: c to stderr
如前所述，predate.sh将为每一行添加时间戳前缀，tstdate.sh只是一个测试程序，用于写入具有特定时间间隔的stdout和stderr。 当您运行该命令时，实际上将"d to stdout"写入stderr(但这是您的TTY设备或启动时可能出现的任何其他stdout)。带有时间戳的stderr行将写入所需的文件。

