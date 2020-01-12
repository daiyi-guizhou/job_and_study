###  文件清理后，磁盘没及时同步。
事件： 发现  df 不足，  检查是某个日志太大， 于是删除日志， 再次 df -h 检查 磁盘。 发现没及时同步。  
```
root@远盛09-GPU号(70-85-C2-88-27-97):/# df -h
文件系统        容量  已用  可用 已用% 挂载点
udev            3.9G     0  3.9G    0% /dev
tmpfs           790M   70M  720M    9% /run
/dev/sda1        32G   20G   11G   64% /
tmpfs           3.9G  252K  3.9G    1% /dev/shm
tmpfs           5.0M  4.0K  5.0M    1% /run/lock
tmpfs           3.9G     0  3.9G    0% /sys/fs/cgroup
/dev/sda2       174G   46G  120G   28% /data
tmpfs          1000M  370M  631M   37% /data/tmp
tmpfs           790M  4.0K  790M    1% /run/user/112
tmpfs           790M     0  790M    0% /run/user/1000
root@远盛09-GPU号(70-85-C2-88-27-97):/# du -sh /var/log/obsolete-flaw-checker-log/* |grep G
5.7G	/var/log/obsolete-flaw-checker-log/flawChecker_2019-03-19.log
root@远盛09-GPU号(70-85-C2-88-27-97):/# rm -rf /var/log/obsolete-flaw-checker-log/flawChecker_2019-03-19.log
root@远盛09-GPU号(70-85-C2-88-27-97):/# du -sh /var/log/obsolete-flaw-checker-log/* |grep M
657M	/var/log/obsolete-flaw-checker-log/flawChecker_2019-03-19.log00000
root@远盛09-GPU号(70-85-C2-88-27-97):/# rm -rf /var/log/obsolete-flaw-checker-log/flawChecker_2019-03-19.log00000 
root@远盛09-GPU号(70-85-C2-88-27-97):/# df -h
文件系统        容量  已用  可用 已用% 挂载点
udev            3.9G     0  3.9G    0% /dev
tmpfs           790M   70M  720M    9% /run
/dev/sda1        32G   19G   12G   62% /
tmpfs           3.9G  252K  3.9G    1% /dev/shm
tmpfs           5.0M  4.0K  5.0M    1% /run/lock
tmpfs           3.9G     0  3.9G    0% /sys/fs/cgroup
/dev/sda2       174G   46G  120G   28% /data
tmpfs          1000M  370M  631M   37% /data/tmp
tmpfs           790M  4.0K  790M    1% /run/user/112
tmpfs           790M     0  790M    0% /run/user/1000

```

### 文件（你删除的）仍被进程占用，所以空间没释放
使用这个命令就可以查看。 
```
# lsof | grep 'deleted'
# ls -ld /proc/* | grep '(deleted)'
```

参考链接(https://ma.ttias.be/df-command-in-linux-not-updating-actual-diskspace-wrong-data/)
以下是原文， 
Caused by open file descriptors

If you delete files from the filesystem, the command "df -h" might not show the deleted space as being available. This is because the deleted files could still be held open by (defunct) processes, where the file descriptor handles still point to those files. As a result, the df command assumes the files are still there, and doesn't clear the space.
