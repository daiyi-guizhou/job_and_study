```
[gpuautoReboot]
www.yy.com:13673
www.yy.com:17817
www.yy.com:10138
www.yy.com:16444
www.yy.com:12918
```
这时只能执行一个，

```
root@test:/etc/ansible# ansible -i ./hosts gpuReboot -m shell -a "head -n 2 /home/work/open-falcon/push-scripts/gpuReboot/gpuReboot.log" --private-key=~/.ssh/id_rsa
www.yy.com | CHANGED | rc=0 >>
```

```
[gpuReboot]
aa ansible_ssh_port=10907 ansible_ssh_host=www.yy.com
bb ansible_ssh_port=17817 ansible_ssh_host=www.yy.com
cc ansible_ssh_port=11762 ansible_ssh_host=www.yy.com
dd ansible_ssh_port=19775 ansible_ssh_host=www.yy.com
ee ansible_ssh_port=14421 ansible_ssh_host=www.yy.com
ff ansible_ssh_port=19567 ansible_ssh_host=www.yy.com
gg ansible_ssh_port=11741 ansible_ssh_host=www.yy.com
hh ansible_ssh_port=19567 ansible_ssh_host=www.yy.com

```
改用别名的时候，这个时候就能执行了，　　不知道是为什么？？

```
root@test:/etc/ansible# ansible -i ./hosts gpuReboot_alias -m shell -a "head -n 2 /home/work/open-falcon/push-scripts/gpuReboot/gpuReboot.log" --private-key=~/.ssh/id_rsa
aa | CHANGED | rc=0 >>


bb | CHANGED | rc=0 >>


cc | CHANGED | rc=0 >>


dd | CHANGED | rc=0 >>


ee | CHANGED | rc=0 >>


gg | CHANGED | rc=0 >>


ff | CHANGED | rc=0 >>


hh | CHANGED | rc=0 >>


```
## 好像公司的端口是　随机变化的，　这个代理可以的．
