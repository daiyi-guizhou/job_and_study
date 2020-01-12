 ### ssh登录时在参数中加入密码的解决方案
转载(https://www.cnblogs.com/senlinyang/p/7833249.html)
　　在使用ssh登录远程服务器的时候，在执行完ssh user@ip后，要输入登录密码，有时候登录密码记不住，这样以来Ian带来的很多的麻烦，有没有一种在ssh的参数中直接加入密码的方法呢？查看ssh的帮助我们发现ssh命令并不能在参数中制定密码。
复制代码

usage: ssh [-1246AaCfGgKkMNnqsTtVvXxYy] [-b bind_address] [-c cipher_spec]
           [-D [bind_address:]port] [-E log_file] [-e escape_char]
           [-F configfile] [-I pkcs11] [-i identity_file] [-L address]
           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
           [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
           [-w local_tun[:remote_tun]] [user@]hostname [command]

复制代码

于是各种google,找到sshpass

sshpass:用于非交互的ssh 密码验证，允许你用 -p 参数指定明文密码，然后直接登录远程服务器。 它支持密码从命令行,文件,环境变量中读取。

首先在机器上安装sshpass

对于debian/ubuntu系统来说，安装方式很简单：

sudo apt-get install sshpass

对于其他的linux,可以编译sshpass的源码安装：

 wget http://sourceforge.net/projects/sshpass/files/sshpass/1.05/sshpass-1.05.tar.gz  
tar xvzf sshpass-1.05.tar.gz  
./configure 
make  
sudo make install

安装好之后，使用sshpass命令，得到如下：
复制代码

Usage: sshpass [-f|-d|-p|-e] [-hV] command parameters
   -f filename   Take password to use from file
   -d number     Use number as file descriptor for getting password
   -p password   Provide password as argument (security unwise)
   -e            Password is passed as env-var "SSHPASS"
   With no parameters - password will be taken from stdin

   -h            Show help (this screen)
   -V            Print version information
At most one of -f, -d, -p or -e should be used

复制代码

于是把sshpass和ssh命令集合就能实现ssh登录的时候加入密码了，这样把登录某台计算机的命令写成shell脚本，后面就十分的方便了

#!/bin/bash
sshpass -p "XXX" ssh user@IP

转载(https://www.cnblogs.com/senlinyang/p/7833249.html)
