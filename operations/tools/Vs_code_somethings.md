## 在使用VScdoe时，无法切换输入法至中文。(在外面切换到中文再进去也无法输入中文)。
遇到这个问题，我的vscode是从ubuntu应用商店安装的snap版本，
后来卸载掉，从vscode官网 (https://code.visualstudio.com/)下载deb包安装的就可以正常输入中文


## VS Code 中文注释显示乱码
1.文件

2.首选项

3.设置

4.搜索

"files.autoGuessEncoding": flase   

改为

"files.autoGuessEncoding": true

## Visual Studio Code修改成中文
进入VS 

按住ctrl+shift+p  或者F1出现以下页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190123154618871.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
输入configure Language 按回车
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190123154725724.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
修改"locale":"en" 为"locale":"zh-CN"


按住Ctrl+shift+x

输入chinese
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190123154740518.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
点击进入 install  点击Yes,重启编辑器,显示
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190123154803781.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
#### 以root 启动
我的ubuntu. 
```
/usr/share/code/bin/code --unity-launch --user-data-dir
```

感谢：https://blog.csdn.net/localhostlucky123/article/details/83448054 


