转自 (https://www.cnblogs.com/klvchen/p/9098745.html)

## CentOS 版本 7.4，Docker 版本 docker-1.13 及以下

ll /var/run/docker.sock
srw-rw----. 1 root root 0 May 25 14:43 /var/run/docker.sock

#添加 docker 用户组
groupadd docker

#把需要执行的 docker 用户添加进该组，这里是 ibaboss
gpasswd -a ibaboss docker

#重启 docker
systemctl restart docker

su - ibaboss

#运行成功
docker ps -a 

## CentOS 版本 7.4，Docker 版本 docker-ce 17 及以上

ll /var/run/docker.sock

srw-rw----. 1 root docker 0 May 25 14:12 /var/run/docker.sock

#添加执行 docker 命令的用户，这里为 ibaboss
useradd ibaboss

#把 ibaboss 用户加入 docker 组
usermod -G docker ibaboss  

su - ibaboss

docker ps -a 

### 注意事项

如果之前是使用 root 用户拉取的镜像，ibaboss 用户启动镜像可能会出现问题，eg：
docker.elastic.co/elasticsearch/elasticsearch 6.2.4
会出现
mktemp: failed to create directory via template '/tmp/elasticsearch.XXXXXXXX': Permission denied
解决方案：
使用 ibaboss 用户重新拉取镜像

