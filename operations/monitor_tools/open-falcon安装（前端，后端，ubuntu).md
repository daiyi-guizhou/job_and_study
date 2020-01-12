#  环境准备
#redis与mysql的环境准备

```
cd
apt-get update
apt-get install -y redis-server
ps -ef|grep redis
apt-get install -y mysql-server  #此处有设置你的 密码（ mysqladmin -u root password 'test'）。 #本文以test 为例 
      
service mysql start
ps -ef|grep mysql     
mysql -uroot -ptest
```
#导入数据库资料

```
cd /tmp
yes|apt install git
git clone https://github.com/open-falcon/falcon-plus.git
cd /tmp/falcon-plus/scripts/mysql/db_schema/
mysql -h 127.0.0.1 -u root -ptest < 1_uic-db-schema.sql
mysql -h 127.0.0.1 -u root -ptest < 2_portal-db-schema.sql 
mysql -h 127.0.0.1 -u root -ptest < 3_dashboard-db-schema.sql 
mysql -h 127.0.0.1 -u root -ptest < 4_graph-db-schema.sql 
mysql -h 127.0.0.1 -u root -ptest < 5_alarms-db-schema.sql   #如无密码，就用 mysql-u root  < 5_alarms-db-schema.sql
```
#安装golang  环境。(yes | apt install golang-go)

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
```
#配置go环境变量

```
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
#下载open-falcon的tar包

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
#  后端-agent开启

```
 #修改配置文件，transfer的ip，#此处为xx.222.228.yy  
sed -i '/ip/ s/\"ip\"\:\ /\"ip\"\:\ \"xx\.222\.228\.yy/g' /home/work/open-falcon/agent/config/cfg.json
sed -i '/127\.0\.0\.1/ s/127\.0\.0\.1/xx\.222\.228\.yy/g'  /home/work/open-falcon/agent/config/cfg.json 
```
#启动

```
cd $WORKSPACE
./open-falcon start agent    #只开启 agent端。
ps -ef|grep open-falcon

```
 
 #   前端 
 #环境准备如上“环境准备”


 #创建工作目录    
```
export FALCON_HOME=/home/work
     export WORKSPACE=$FALCON_HOME/open-falcon
     mkdir -p $WORKSPACE
     ls work/open-falcon/
   cd $WORKSPACE
    ls
```
#克隆前端组件代码

```
cd open-falcon/
git clone https://github.com/open-falcon/dashboard.git 
```

 

#安装依赖包

```
apt-get update
apt install python-virtualenv -y  
yes|apt-get install python-pip
yes|apt-get install python-dev 
apt-get install ldap-utils
yes|apt-get install libmysqld-dev
```


#启动试试

```
cd dashboard/
ls
virtualenv ./env
./env/bin/pip install -r pip_requirements.txt -i https://pypi.douban.com/simple  #会有报错，
```



#再安装一些包。

```
apt-get install python-dev
apt-get install libldap2-dev
apt-get install libsasl2-dev
./env/bin/pip install python-ldap
./env/bin/pip install -r pip_requirements.txt -i https://pypi.douban.com/simple  #好了
```



#启动

```
./env/bin/python wsgi.py  ##以开发者模式启动
bash control start     #以在生产环境启动
```

  #open http://127.0.0.1:8081 in your browser.  注册，登陆。
  




有时候，一切都配置好了，但是界面上还是什么都没有， 
![在这里插入图片描述](https://img-blog.csdn.net/20181015181337677?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

这个时候， 需要用数据搜索下， 
![在这里插入图片描述](https://img-blog.csdn.net/20181015181751741?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)![在这里插入图片描述](https://img-blog.csdn.net/20181015181634635?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

接着就可以查看数据了
![在这里插入图片描述](https://img-blog.csdn.net/20181015181904271?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![在这里插入图片描述](https://img-blog.csdn.net/20181015182010504?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
![在这里插入图片描述](https://img-blog.csdn.net/20181018112027405?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
