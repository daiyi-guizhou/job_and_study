


# 清理磁盘．

cd　/　　　＃到根目录 
df -h    #找到占用大的目录
du -sh *   #重复执行这一句，　把占用大的文件　结构，　找到具体的，占用大的，没用的文件，
rm -rf \`ls *|head -n 50 `   #删除前50个． 


##### 命令
df -h 			#这个命令用于查看服务器空间，
df -h [目录]　　	　看目录属于哪个磁盘分区
du -h --max-depth=1     	 #看当前最大文件．
du -sh *  		   # 这个命令也用于查看当前目录下各文件及文件夹占用大小
du -sh /var/log/* |grep M|sort -n   

```
root@test:/# du -sh /var/log/* |grep G
1.2G	/var/log/syslog.1
root@test:/# du -sh /var/log/* |grep M|sort -n|tail -n 9
501M	/var/log/buttonMonitor.log.2018-11-30
533M	/var/log/buttonMonitor.log
656M	/var/log/obsolete-flaw-checker-log
772M	/var/log/syslog
822M	/var/log/buttonMonitor.log.2018-12-01
822M	/var/log/buttonMonitor.log.2018-12-04
823M	/var/log/buttonMonitor.log.2018-12-05
824M	/var/log/buttonMonitor.log.2018-12-02
824M	/var/log/buttonMonitor.log.2018-12-03

```

# 清理内存
#### 说明
1 并不存在清理内存这一事实。只是清理一些不用的东西， 如果你写的 程序实在占用太多内存， 你首先应该考虑 怎么 减少你的程序的调用。 


每个 Linux 系统有三种选项来清除缓存而不需要中断任何进程或服务。

（Cache，译作“缓存”，指 CPU 和内存之间高速缓存。Buffer，译作“缓冲区”，指在写入磁盘前的存储再内存中的内容。在本文中，Buffer 和 Cache 有时候会通指。）

    仅清除页面缓存（PageCache）

        # sync; echo 1 > /proc/sys/vm/drop_caches       

    清除目录项和inode

        # sync; echo 2 > /proc/sys/vm/drop_caches       

    清除页面缓存，目录项和inode

        # sync; echo 3 > /proc/sys/vm/drop_caches 


如果你想清除掉的空间，你可以运行下面的命令：

    # swapoff -a && swapon -a
上述命令的说明：

sync 将刷新文件系统缓冲区（buffer），命令通过“;”分隔，顺序执行，shell在执行序列中的下一个命令之前会等待命令的终止。正如内核文档中提到的，写入到drop_cache将清空缓存而不会杀死任何应用程序/服务，echo命令做写入文件的工作。

如果你必须清除磁盘高速缓存，第一个命令在企业和生产环境中是最安全，"...echo 1> ..."只会清除页面缓存。 在生产环境中不建议使用上面的第三个选项"...echo 3 > ..." ，除非你明确自己在做什么，因为它会清除缓存页，目录项和inodes
参考链接(https://linux.cn/article-5627-1.html)


#### 还有 一些 小的清理
软件版本， 软件缓存，孤立文件，  多余的Ubuntu内核。
参考链接 https://blog.csdn.net/Ol_Jack/article/details/51347090
