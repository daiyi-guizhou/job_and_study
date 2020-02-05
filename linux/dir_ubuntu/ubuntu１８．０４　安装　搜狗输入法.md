感谢　https://ywnz.com/linuxjc/1637.html
(https://www.jianshu.com/p/c936a8a2180e)
卸载ibus。

```
sudo apt-get remove ibus
```


清除ibus配置。

```
sudo apt-get purge ibus
```


卸载顶部面板任务栏上的键盘指示。

```
sudo  apt-get remove indicator-keyboard
```



安装fcitx输入法框架

```

sudo apt install fcitx-table-wbpy fcitx-config-gtk
```


切换为 Fcitx输入法

```
im-config -n fcitx
```



im-config 配置需要重启系统才能生效

```
sudo shutdown -r now
```



下载搜狗输入法

```
wget http://cdn2.ime.sogou.com/dl/index/1524572264/sogoupinyin_2.2.0.0108_amd64.deb  ?st=ryCwKkvb-0zXvtBlhw5q4Q&e=1529739124&fn=sogoupinyin_2.2.0.0108_amd64.deb

```


安装搜狗输入法

```
sudo dpkg -i sogoupinyin_2.2.0.0108_amd64.deb
```



修复损坏缺少的包

```
 sudo apt-get install -f
```



打开 Fcitx 输入法配置

```
fcitx-config-gtk3
```



问题:输入法皮肤透明

fcitx设置 >>附加组件>>勾选高级 >>取消经典界面

Configure>>  Addon  >>Advanced>>Classic






这里点，设置下，点击，不然是繁体字．

![simplified很恶心，设置下，点击，不然是繁体字．](https://img-blog.csdnimg.cn/20181119215304283.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
