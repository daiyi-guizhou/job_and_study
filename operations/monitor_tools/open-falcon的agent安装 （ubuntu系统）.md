#redis与mysql的环境准备。

```
cd
apt-get update
apt-get install -y redis-server
ps -ef|grep redis
apt-get install -y mysql-server  #此处有设置你的 密码。 #本文以test 为例 
      
service mysql start
ps -ef|grep mysql     
mysql -uroot -ptest
```





#导入数据库资料 

```
cd /tmp
y|apt install git
git clone https://github.com/open-falcon/falcon-plus.git
cd /tmp/falcon-plus/scripts/mysql/db_schema/
mysql -h 127.0.0.1 -u root -ptest < 1_uic-db-schema.sql
mysql -h 127.0.0.1 -u root -ptest < 2_portal-db-schema.sql 
mysql -h 127.0.0.1 -u root -ptest < 3_dashboard-db-schema.sql 
mysql -h 127.0.0.1 -u root -ptest < 4_graph-db-schema.sql 
mysql -h 127.0.0.1 -u root -ptest < 5_alarms-db-schema.sql   #如无密码，就用 mysql-u root  < 5_alarms-db-schema.sql
```


    
#安装golang  环境。

```
cd 
mkdir software
cd software
wget https://storage.googleapis.com/golang/go1.8.1.linux-amd64.tar.gz
tar -zxvf go1.8.1.linux-amd64.tar.gz 
mkdir gopath
cd gopath/
mkdir src pkg bin

apt install -y vim 
vim .bashrc 
#添加一下内容。
#export GOROOT=/root/software/go
#export GOPATH=/root/software/gopath
#export GOBIN=$GOPATH/bin
#export PATH=$PATH:$GOBIN:$GOROOT/bin

source .bashrc 
go version
go env	
	
```






	
	
	
#下载open-falcon的tar包。

```
wget https://github.com/open-falcon/falcon-plus/releases/download/v0.2.0/open-falcon-v0.2.0.tar.gz
mv open-falcon-v0.2.0.tar.gz /tmp
```

    
#创建工作目录

```
export FALCON_HOME=/home/work
export WORKSPACE=$FALCON_HOME/open-falcon
mkdir -p $WORKSPACE
ls /home/work/open-falcon/
cd /tmp
tar -xzvf open-falcon-v0.2.0.tar.gz -C $WORKSPACE
cd /home/work/open-falcon/
cd $WORKSPACE
grep -Ilr 3306  ./ | xargs -n1 -- sed -i 's/root:/root:test/g'   #修改密码，test 为你的密码。
mkdir /root/software
cd /root/software/
```



   
   

   
 
#后端启动
cd $WORKSPACE
vim agent/config/cfg.json   #修改配置文件，AWS为transfer，
![在这里插入图片描述](https://img-blog.csdn.net/20181016113047992?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

./open-falcon start agent
ps -ef|grep open-falcon

