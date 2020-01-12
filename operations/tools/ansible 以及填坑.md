首先感谢(https://blog.csdn.net/pushiqiang/article/details/78126063)
(https://blog.csdn.net/aaa978464597/article/details/82859904)
(http://blog.51cto.com/changfei/1657233)
# 1 安装

当然我们需要先安装Ansible。任务可以从任何可安装的机器上运行。
## 1.1 Ubuntu
在Ubuntu 16.04上安装Ansible的方法。
```
sudo apt-get install -y ansible
```
# 2 配置

ansible的默认配置文件路径为 /etc/ansible，然而，一个常见的用途是将其安装在一个virtualenv中，在这种情况下，我们一般不会使用这些默认文件。我们可以根据需要在本地目录中创建配置文件。
## 2.1 管理服务器：Inventory文件
您可以创建一个inventory文件，用于定义将要管理的服务器。这个文件可以命名为任何名字，但我们通常会命名为hosts或者项目的名称。
在hosts文件中，我们可以定义一些要管理的服务器。这里我们将定义我们可能要在“remote”标签下管理的两个服务器。标签是任意的。
```
[remote]
192.168.22.10
192.168.22.11
```

现在已经够好了，如果需要，我们可以定义主机范围，多个组，可重用变量，并使用其他花哨的设置，包括创建动态的inventory。
当我们在本地机器运行ansible时，我们不需要关心inventory文件中的内容，我将告诉您在本地和远程服务器上运行ansible。现在，让我们将hosts文件设置为指向本地主机local和remote虚拟远程主机。
hosts文件：

```
[local]
127.0.0.1

[remote]
192.168.1.2
```
与本地主机和远程服务器连接的命令。
## 2.2 基础：运行命令
#首先你的机器要能ssh 到你的远程主机,
#此处, 我把我都当前用户test 以及在root都配置了 能 免密登录远程主机,  但是只有test用户成功了. (is_rsa.pub的字符都放到了远程主机的authorized_keys里)

我们开始对服务器运行任务。ansible会假定你的服务器具有SSH访问权限，通常基于SSH-Key。因为Ansible使用SSH，所以它需要能够SSH连接到服务器。但是，ansible将尝试以正在运行的当前用户身份进行连接。如果我正在运行ansible的用户是ubuntu，它将尝试以ubuntu连接其他服务器。

```
#Run against localhost
$ ansible -i ./hosts --connection=local local -m ping

#Run against remote server
$ ansible -i ./hosts remote -m ping
127.0.0.1 | success >> {
    "changed": false,
    "ping": "pong"
}
```
如果你是在cygwin下运行，遇到了“Failed to connect to the host via ssh: mux_client_request_session: read from master failed”的错误，可以执行:


    ansible -i ./hosts remote -v -m ping -u root --private-key=~/.ssh/id_rsa

使用–connection=local告诉ansible不尝试通过SSH运行命令，因为我们只是影响本地主机。但是，我们仍然需要一个hosts文件，告诉我们连接到哪里。
在任何情况下，我们可以看到从ansible得到的输出是一些JSON，它告诉我们Task（我们对ping模块的调用）是否进行了任何更改和结果。

命令说明：
```
i ./hosts - 设置库存文件，命名为 hosts
remote，local，all-使用这个标签的下定义的服务器hosts清单文件。“all”是针对文件中定义的每个服务器运行的特殊关键字
-m ping- 使用“ping”模块，它只是运行ping命令并返回结果
-c local| --connection=local - 在本地服务器上运行命令，而不是SSH

一些常用命令：
-i PATH --inventory=PATH 指定host文件的路径，默认是在/etc/ansible/hosts
--private-key=PRIVATE_KEY_FILE_PATH 使用指定路径的秘钥建立认证连接
-m DIRECTORY --module-path=DIRECTORY 指定module的目录来加载module，默认是/usr/share/ansible
-c CONNECTION --connection=CONNECTION 指定建立连接的类型，一般有ssh ，local
```
#此处,我遇到的问题是, 只能在test用户下执行, 而且必须加上 ` -u root  --private-key=~/.ssh/id_rsa`

#如下例子
```
root@test:/etc/ansible# ansible -i ./hosts remote -u root -b --become-user=root -m shell -a "mkdir -p /tmp/test/root" --private-key=~/.ssh/id_rsa
10.0.10.59 | UNREACHABLE! => {
    "changed": false, 
    "msg": "Failed to connect to the host via ssh: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\r\n@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @\r\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\r\nPermissions 0711 for '/root/.ssh/id_rsa' are too open.\r\nIt is required that your private key files are NOT accessible by others.\r\nThis private key will be ignored.\r\nLoad key \"/root/.ssh/id_rsa\": bad permissions\r\nroot@10.0.10.59: Permission denied (publickey,password).\r\n", 
    "unreachable": true
}
10.0.18.73 | UNREACHABLE! => {
    "changed": false, 
    "msg": "Failed to connect to the host via ssh: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\r\n@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @\r\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\r\nPermissions 0711 for '/root/.ssh/id_rsa' are too open.\r\nIt is required that your private key files are NOT accessible by others.\r\nThis private key will be ignored.\r\nLoad key \"/root/.ssh/id_rsa\": bad permissions\r\nroot@10.0.18.73: Permission denied (publickey,password).\r\n", 
    "unreachable": true
}
root@test:/etc/ansible# exit
exit
test@test:/etc/ansible$ ansible -i ./hosts remote -u root -b --become-user=root -m shell -a "mkdir -p /tmp/test/root" --private-key=~/.ssh/id_rsa
 [WARNING]: Consider using the file module with state=directory rather than running mkdir.  If you need to
use command because file is insufficient you can add warn=False to this command task or set
command_warnings=False in ansible.cfg to get rid of this message.

10.0.10.59 | CHANGED | rc=0 >>


10.0.18.73 | CHANGED | rc=0 >>

```
这里的报错是因为权限太大, 修改就好`chmod 600 /root/.ssh/*`
##之前root不能免密登录也是因为权限太大,修改后就好了.
```
root@test:/etc/ansible# chmod 600 /root/.ssh/*
root@test:/etc/ansible# ansible -i ./hosts remote -u root -b --become-user=root -m shell -a "mkdir -p /tmp/test/rot1" --private-key=~/.ssh/id_rsa
 [WARNING]: Consider using the file module with state=directory rather than running mkdir.  If you need to use command because
file is insufficient you can add warn=False to this command task or set command_warnings=False in ansible.cfg to get rid of this
message.

10.0.10.59 | CHANGED | rc=0 >>


10.0.18.73 | CHANGED | rc=0 >>

```
####  host's fingerprint报错

```
www.yyy.com | FAILED! => {
    "msg": "Using a SSH password instead of a key is not possible because Host Key checking is enabled and sshpass does not support this.  Please add this host's fingerprint to your known_hosts file to manage this host."
}

```
 从上面的输出提示上基本可以了解到由于在本机的~/.ssh/known_hosts文件中并有fingerprint key串，ssh第一次连接的时候一般会提示输入yes 进行确认为将key字符串加入到  ~/.ssh/known_hosts 文件中。
###### 方法1：

了解到问题原因为，我们了解到进行ssh连接时，可以使用-o参数将StrictHostKeyChecking设置为no，使用ssh连接时避免首次连接时让输入yes/no部分的提示。通过查看ansible.cfg配置文件，发现如下行：

    [ssh_connection]
    # ssh arguments to use
    # Leaving off ControlPersist will result in poor performance, so use
    # paramiko on older platforms rather than removing it
    #ssh_args = -o ControlMaster=auto -o ControlPersist=60s

所以这里我们可以启用ssh_args 部分，使用下面的配置，避免上面出现的错误：

    ssh_args = -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking＝no 

###### 方法2：

在ansible.cfg配置文件中，也会找到如下部分：

    # uncomment this to disable SSH key host checking
    host_key_checking = False  

默认host_key_checking部分是注释的，通过找开该行的注释，同样也可以实现跳过 ssh 首次连接提示验证部分。由于配置文件中直接有该选项，所以推荐用方法2 。


### 执行shell 命令

```
ansible -i ./hosts remote -m shell -a 'yes|sudo apt install nginx'
```
#这里yes|sudo  避免麻烦.
```
root@:/etc/ansible# ansible -i ./hosts remote -m shell -a 'yes|sudo apt install nginx'
10.0.10.59 | CHANGED | rc=0 >>
正在读取软件包列表...
正在分析软件包的依赖关系树...
正在读取状态信息...
下列软件包是自动安装的并且现在不需要了：
  amd64-microcode linux-headers-4.13.0-36 linux-headers-4.13.0-36-generic
  linux-headers-4.13.0-39 linux-headers-4.13.0-39-generic
  linux-headers-4.13.0-43 linux-headers-4.13.0-43-generic
```

## 使用模块
#使用apt模块.
```
root@:/etc/ansible# ansible -i ./hosts remote -b --become-user=root -m apt -a 'name=nginx state=installed update_cache=true'
[DEPRECATION WARNING]: State 'installed' is deprecated. Using state 'present' instead.. This feature will be removed in 
version 2.9. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
10.0.18.73 | SUCCESS => {
    "cache_update_time": 1543563224, 
    "cache_updated": true, 
    "changed": false
}
10.0.10.59 | SUCCESS => {
    "cache_update_time": 1543563230, 
    "cache_updated": true, 
    "changed": false
}

```
命令说明:

```

-i ./hosts - 设置inventory文件，命名为 hosts
-b - “成”，告诉可以成为另一个用户来运行命令
--become-user=root - 以用户“root”运行以下命令（例如，使用“sudo”命令）
local| remote - 从库存文件中的本地或远程定义的主机上运行
-m apt- 使用apt模块
-a 'name=nginx state=installed update_cache=true' - 提供apt模块的参数，包括软件包名称，所需的结束状态以及是否更新软件包存储库缓存

常用命令：
-u USERNAME --user=USERNAME 指定移动端的执行用户
-U SUDO_USERNAME --sudo-user=USERNAME
-s --sudo -u指定用户的时候，使用sudo获得root权限
-k --ask-pass  提示输入ssh的密码，而不是使用基于ssh的密钥认证
-K --ask-sudo-pass 提示输入sudo密码，与--sudo一起使用
```
# 使用palybook
#此任务与我们的ad-hoc命令完全相同，包括设置本地连接的使用。
这将使用inventory文件中[local]标签下的服务器hosts。
如果我们没有使用本地连接，我们会这样做：

```
root@test:/etc/ansible# cat nginx.yml 
---
- hosts: remote
  connection: local
  become: yes
  become_user: root
  tasks:
   - name: Install Nginx
     apt:
       name: nginx
       state: installed
       update_cache: true

```
这将使用inventory文件中[remote]标签下的服务器hosts。

在我们的Tasks文件中使用become并become_user再次使用Ansible来sudo以root用户身份运行命令，然后传递Playbook文件。

```
root@test:/etc/ansible# vim nginx.yml
root@test:/etc/ansible# ansible-playbook -i ./hosts nginx.yml 

PLAY [remote] *************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************
ok: [10.0.18.73]
ok: [10.0.10.59]

TASK [Install Nginx] ******************************************************************************************************************************************
fatal: [10.0.18.73]: FAILED! => {"changed": false, "cmd": "apt-get update", "msg": "E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)\nE: Unable to lock directory /var/lib/apt/lists/", "rc": 100, "stderr": "E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)\nE: Unable to lock directory /var/lib/apt/lists/\n", "stderr_lines": ["E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)", "E: Unable to lock directory /var/lib/apt/lists/"], "stdout": "Reading package lists...\n", "stdout_lines": ["Reading package lists..."]}
fatal: [10.0.10.59]: FAILED! => {"changed": false, "cmd": "apt-get update", "msg": "E: The repository 'http://ppa.launchpad.net/fcitx-team/nightly/ubuntu bionic Release' does not have a Release file.", "rc": 100, "stderr": "E: The repository 'http://ppa.launchpad.net/fcitx-team/nightly/ubuntu bionic Release' does not have a Release file.\n", "stderr_lines": ["E: The repository 'http://ppa.launchpad.net/fcitx-team/nightly/ubuntu bionic Release' does not have a Release file."], "stdout": "Get:1 file:/var/cuda-repo-9-0-176-local-patch-4  InRelease\nIgn:1 file:/var/cuda-repo-9-0-176-local-patch-4  InRelease\nGet:2 file:/var/cuda-repo-9-0-local-cublas-performance-update-2  InRelease\nIgn:2 file:/var/cuda-repo-9-0-local-cublas-performance-update-2  InRelease\nGet:3 file:/var/cuda-repo-9-0-local-cublas-performance-update-3  InRelease\nIgn:3 file:/var/cuda-repo-9-0-local-cublas-performance-update-3  InRelease\nGet:4 file:/var/cuda-repo-9-0-local-cublas-performance-update  InRelease\nIgn:4 file:/var/cuda-repo-9-0-local-cublas-performance-update  InRelease\nGet:5 file:/var/cuda-repo-9-0-local  InRelease\nIgn:5 file:/var/cuda-repo-9-0-local  InRelease\nGet:6 file:/var/cuda-repo-9-0-176-local-patch-4  Release [574 B]\nGet:7 file:/var/cuda-repo-9-0-local-cublas-performance-update-2  Release [574 B]\nGet:8 file:/var/cuda-repo-9-0-local-cublas-performance-update-3  Release [574 B]\nGet:9 file:/var/cuda-repo-9-0-local-cublas-performance-update  Release [574 B]\nGet:10 file:/var/cuda-repo-9-0-local  Release [574 B]\nGet:6 file:/var/cuda-repo-9-0-176-local-patch-4  Release [574 B]\nGet:7 file:/var/cuda-repo-9-0-local-cublas-performance-update-2  Release [574 B]\nGet:8 file:/var/cuda-repo-9-0-local-cublas-performance-update-3  Release [574 B]\nGet:9 file:/var/cuda-repo-9-0-local-cublas-performance-update  Release [574 B]\nGet:10 file:/var/cuda-repo-9-0-local  Release [574 B]\nHit:13 http://archive.ubuntukylin.com:10006/ubuntukylin xenial InRelease\nHit:17 http://packages.microsoft.com/repos/vscode stable InRelease\nHit:18 http://security.ubuntu.com/ubuntu bionic-security InRelease\nHit:19 http://archive.ubuntu.com/ubuntu bionic InRelease\nHit:20 http://cn.archive.ubuntu.com/ubuntu bionic InRelease\nIgn:21 http://ppa.launchpad.net/fcitx-team/nightly/ubuntu bionic InRelease\nHit:22 http://archive.canonical.com bionic InRelease\nHit:23 http://cn.archive.ubuntu.com/ubuntu bionic-updates InRelease\nHit:24 http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu bionic InRelease\nHit:25 http://cn.archive.ubuntu.com/ubuntu bionic-backports InRelease\nErr:26 http://ppa.launchpad.net/fcitx-team/nightly/ubuntu bionic Release\n  404  Not Found [IP: 91.189.95.83 80]\nReading package lists...\n", "stdout_lines": ["Get:1 file:/var/cuda-repo-9-0-176-local-patch-4  InRelease", "Ign:1 file:/var/cuda-repo-9-0-176-local-patch-4  InRelease", "Get:2 file:/var/cuda-repo-9-0-local-cublas-performance-update-2  InRelease", "Ign:2 file:/var/cuda-repo-9-0-local-cublas-performance-update-2  InRelease", "Get:3 file:/var/cuda-repo-9-0-local-cublas-performance-update-3  InRelease", "Ign:3 file:/var/cuda-repo-9-0-local-cublas-performance-update-3  InRelease", "Get:4 file:/var/cuda-repo-9-0-local-cublas-performance-update  InRelease", "Ign:4 file:/var/cuda-repo-9-0-local-cublas-performance-update  InRelease", "Get:5 file:/var/cuda-repo-9-0-local  InRelease", "Ign:5 file:/var/cuda-repo-9-0-local  InRelease", "Get:6 file:/var/cuda-repo-9-0-176-local-patch-4  Release [574 B]", "Get:7 file:/var/cuda-repo-9-0-local-cublas-performance-update-2  Release [574 B]", "Get:8 file:/var/cuda-repo-9-0-local-cublas-performance-update-3  Release [574 B]", "Get:9 file:/var/cuda-repo-9-0-local-cublas-performance-update  Release [574 B]", "Get:10 file:/var/cuda-repo-9-0-local  Release [574 B]", "Get:6 file:/var/cuda-repo-9-0-176-local-patch-4  Release [574 B]", "Get:7 file:/var/cuda-repo-9-0-local-cublas-performance-update-2  Release [574 B]", "Get:8 file:/var/cuda-repo-9-0-local-cublas-performance-update-3  Release [574 B]", "Get:9 file:/var/cuda-repo-9-0-local-cublas-performance-update  Release [574 B]", "Get:10 file:/var/cuda-repo-9-0-local  Release [574 B]", "Hit:13 http://archive.ubuntukylin.com:10006/ubuntukylin xenial InRelease", "Hit:17 http://packages.microsoft.com/repos/vscode stable InRelease", "Hit:18 http://security.ubuntu.com/ubuntu bionic-security InRelease", "Hit:19 http://archive.ubuntu.com/ubuntu bionic InRelease", "Hit:20 http://cn.archive.ubuntu.com/ubuntu bionic InRelease", "Ign:21 http://ppa.launchpad.net/fcitx-team/nightly/ubuntu bionic InRelease", "Hit:22 http://archive.canonical.com bionic InRelease", "Hit:23 http://cn.archive.ubuntu.com/ubuntu bionic-updates InRelease", "Hit:24 http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu bionic InRelease", "Hit:25 http://cn.archive.ubuntu.com/ubuntu bionic-backports InRelease", "Err:26 http://ppa.launchpad.net/fcitx-team/nightly/ubuntu bionic Release", "  404  Not Found [IP: 91.189.95.83 80]", "Reading package lists..."]}
	to retry, use: --limit @/etc/ansible/nginx.retry

PLAY RECAP ****************************************************************************************************************************************************
10.0.10.59                 : ok=1    changed=0    unreachable=0    failed=1   
10.0.18.73                 : ok=1    changed=0    unreachable=0    failed=1   
```
#很明显,它给我们返回了相应的信息
## 2.3.1 处理程序（Handlers）
这个handlers跟&&有点像，意思是先执行完前面然后执行后面的意思：

```
root@test:/etc/ansible# cat touch.yaml 
---
- hosts: remote
  user: root
  tasks:
   - name: tests
     shell: touch /tmp/test/abc.txt
     notify: echo  		 #//这个命令就是类似跳转到handlers这里执行，名字要跟下面定义的一样

  handlers:
   - name: echo
     shell: echo "a b c  echo:" >> /tmp/test/abc.txt
```

```
root@test:/etc/ansible# ansible-playbook -i ./hosts touch.yaml 

PLAY [remote] *************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************
ok: [10.0.10.59]
ok: [10.0.18.73]

TASK [tests] **************************************************************************************************************************************************
 [WARNING]: Consider using the file module with state=touch rather than running touch.  If you need to use command because file is insufficient you can add
warn=False to this command task or set command_warnings=False in ansible.cfg to get rid of this message.

changed: [10.0.10.59]
changed: [10.0.18.73]

RUNNING HANDLER [echo] ****************************************************************************************************************************************
changed: [10.0.10.59]
changed: [10.0.18.73]

PLAY RECAP ****************************************************************************************************************************************************
10.0.10.59                 : ok=3    changed=2    unreachable=0    failed=0   
10.0.18.73                 : ok=3    changed=2    unreachable=0    failed=0 
```

处理程序与任务完全相同（它可以做task可以做的任何事），但只有当另一个任务调用它时才会运行。您可以将其视为事件系统的一部分; 处理程序将通过其侦听的事件调用进行操作。
这对于运行任务后可能需要的“辅助”操作非常有用，例如在配置更改后安装或重新加载服务后启动新服务

```
root@test:/etc/ansible# cat nginx.yml 
---
- hosts: remote
  connection: local
  become: yes
  become_user: root
  handlers:
   - name: Start Nginx
     service:
       name: nginx
       state: stopped

```
然后我们可以创建名为“Start Nginx”的处理程序。此处理程序是通知“Start Nginx”时调用的任务。
这个特定的处理程序使用服务模块，它可以启动，停止，重启，重新加载（等等）系统服务。在这种情况下，我们告诉Ansible，我们要启动Nginx。
让我们再次运行这本Playbook：
```
root@test:/etc/ansible# ansible-playbook -i ./hosts nginx.yml 

PLAY [remote] *************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************
ok: [10.0.10.59]
ok: [10.0.18.73]

PLAY RECAP ****************************************************************************************************************************************************
10.0.10.59                 : ok=1    changed=0    unreachable=0    failed=0   
10.0.18.73                 : ok=1    changed=0    unreachable=0    failed=0   


root@test:/etc/ansible# 
```
## 利用playbook批量创建用户 & 变量
vars就是传递变量
```
root@test:/etc/ansible# cat user.yaml 
---
- hosts: remote
  user: root
  gather_facts: false   
  vars:
   - a: "etc-test"    
  tasks:
   - name: create user 
     user: name="{{a}}"
```

```
root@test:/etc/ansible# ansible-playbook -i ./hosts user.yaml 

PLAY [remote] *************************************************************************************************************************************************

TASK [create user] ********************************************************************************************************************************************
changed: [10.0.10.59]
changed: [10.0.18.73]

PLAY RECAP ****************************************************************************************************************************************************
10.0.10.59                 : ok=1    changed=1    unreachable=0    failed=0   
10.0.18.73                 : ok=1    changed=1    unreachable=0    failed=0 
```
### items 固定用法
### 批量添加

```
root@test:/etc/ansible# cat user.yaml 
---
- hosts: remote
  user: root
  gather_facts: false   
  tasks:
   - name: create user
     user: name="{{item}}"   #固定用法
     with_items:             #固定用法
      - aa
      - bb
      - cc
      - dd
```

```
root@test:/etc/ansible# ansible-playbook -i ./hosts user.yaml 

PLAY [remote] *************************************************************************************************************************************************

TASK [create user] ********************************************************************************************************************************************
changed: [10.0.10.59] => (item=aa)
changed: [10.0.10.59] => (item=bb)
changed: [10.0.10.59] => (item=cc)
changed: [10.0.10.59] => (item=dd)
changed: [10.0.18.73] => (item=aa)
changed: [10.0.18.73] => (item=bb)
changed: [10.0.18.73] => (item=cc)
changed: [10.0.18.73] => (item=dd)

PLAY RECAP ****************************************************************************************************************************************************
10.0.10.59                 : ok=1    changed=1    unreachable=0    failed=0   
10.0.18.73                 : ok=1    changed=1    unreachable=0    failed=0
```
# 传输文件
文件,当前的/etc/ansible/cccc.txt   传到 ./hosts文件里[remote] 主机组里,所有机器的  /tmp/test/david的目录下
```
root@test:/etc/ansible# ansible -i ./hosts remote -m copy -a "src=/etc/ansible/cccc.txt dest=/tmp/test/david
10.0.10.59 | CHANGED => {
    "changed": true, 
    "checksum": "c51a4df5bea8d7ae96a947cb568ceeedcda3831f", 
    "dest": "/tmp/test/david/cccc.txt", 
    "gid": 0, 
    "group": "root", 
    "md5sum": "60359cd46b90a7bebd1396ce7bf0cb7e", 
    "mode": "0644", 
    "owner": "root", 
    "size": 14, 
    "src": "/root/.ansible/tmp/ansible-tmp-1543569645.03-272115409086335/source", 
    "state": "file", 
    "uid": 0
}
10.0.18.73 | CHANGED => {
    "changed": true, 
    "checksum": "c51a4df5bea8d7ae96a947cb568ceeedcda3831f", 
    "dest": "/tmp/test/david/cccc.txt", 
    "gid": 0, 
    "group": "root", 
    "md5sum": "60359cd46b90a7bebd1396ce7bf0cb7e", 
    "mode": "0644", 
    "owner": "root", 
    "size": 14, 
    "src": "/root/.ansible/tmp/ansible-tmp-1543569645.04-29610811603612/source", 
    "state": "file", 
    "uid": 0
}

```
##参考资料
```

#拷贝本地的/etc/hosts 文件到myserver主机组所有主机的/tmp/hosts（空目录除外）,如果使用playbooks 则可以充分利用template 模块
ansible myserver -m copy -a "src=/etc/hosts dest=/tmp/hosts mode=600 owner=ju group=ju"
#file 模块允许更改文件的用户及权限
ansible webservers -m file -a "dest=/srv/foo/a.txt mode=600"
ansible webservers -m file -a "dest=/srv/foo/b.txt mode=600 owner=ju group=ju"
#使用file 模块创建目录，类似mkdir -p
ansible webservers -m file -a "dest=/path/to/c mode=755 owner=ju group=ju state=directory"
#使用file 模块删除文件或者目录
ansible webservers -m file -a "dest=/path/to/c state=absent"

获取远程文件信息stat

ansible webservers -m stat -a "path=/etc/password"
```

