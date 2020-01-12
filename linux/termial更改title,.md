  通过查询，找到一种简单的处理方式，就是讲如下代码加到~/.bashrc的最后位置。
 ## （一）修改title名字 
#### 1 title 通过添加来实现
vim ~/.bashrc
```
    function set-title() {
      if [[ -z "$ORIG" ]]; then
        ORIG=$PS1
      fi
      TITLE="\[\e]2;title的名字\a\]"
      PS1=${ORIG}${TITLE}
    }
     set-title
```
#### 2 直接改～/.bashrc文件。

```
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@title的名字: \w\a\]$PS1"
    ;;
*)
    ;;
esac

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190107130758502.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
## （二）修改命令行的名字
vim  ~/.bashrc
```
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\命令行的名字\[033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi

```
source ~/.bashrc

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190107142647128.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
