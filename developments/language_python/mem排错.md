docker run 一个容器（多个测试样例）。结果显示 有个测试样例被 killed 。
 
docker stats 查看 ，发现内存接近90G；而我实际运行时 只有 1G的内存。所以被killed。 
```
[root@a34h05007.cloud.h05.amtest87 /root]
#docker stats --no-stream|head -n 1;while [[ true ]];do echo time sleep 1 >/dev/null 2>&1;docker stats --no-stream|grep aedfae9724a8;done
CONTAINER CPU % MEM USAGE / LIMIT MEM % NET I/O BLOCK I/O PIDS
aedfae9724a8 119.02% 85.88 GiB / 94.28 GiB 91.08% 0 B / 0 B 12.29 kB / 33.52 MB 4
aedfae9724a8 126.96% 86.16 GiB / 94.28 GiB 91.39% 0 B / 0 B 12.29 kB / 33.52 MB 4
aedfae9724a8 72.66% 86.34 GiB / 94.28 GiB 91.58% 0 B / 0 B 12.29 kB / 33.52 MB 4
aedfae9724a8 54.95% 86.56 GiB / 94.28 GiB 91.81% 0 B / 0 B 12.29 kB / 33.52 MB 4
```
接着用 
在用 memory_profiler, meliae等工具分析， 
debug 一步步排查。
发现有个 dict , 
DEFAULT_QUERY_RETRY_COUNT =1000000 
for  _c in range(DEFAULT_QUERY_RETRY_COUNT):
而我的 python version 为 2.7 , 此时的range是展开一个dict,而不是生成器，所以占据了大量内存。 遂修改。用xrange.
```bash
sed -i 's/for _c in range(DEFAULT_QUERY_RETRY_COUNT/for _c in xrange(DEFAULT_QUERY_RETRY_COUNT/' logclient.py
```
修改之后。好了。 就这样。
