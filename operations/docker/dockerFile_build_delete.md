详见链接(https://yeasy.gitbooks.io/docker_practice/image/dockerfile/entrypoint.html)

### Dockfile 文件制作
```
root@戴燚:/home/daiyi/Documents/study/docker/nginx-test# cat Dockerfile 
FROM python:2.7.15-alpine3.8            #以原来的python为镜像基础。
USER root												# 用户
ENV prefix=/daiyi_nginx						#环境变量
ENV workdir=$prefix/dashboard


RUN mkdir -p $prefix							#执行 shell 命令。

WORKDIR $workdir                           # 工作目录，相当于 cd $workdir 

COPY test.txt pip_requirements.txt       # 复制单个文件
ADD ./ ./													#复制当前的全部文件
ENTRYPOINT ["/bin/sh"]							# 设置 cmd 命令
```
2 生成一些文件，以便待会检验
```
root@戴燚:/home/daiyi/Documents/study/docker/nginx-test# ls
aa  bb  cc  Dockerfile  nginx  test.txt
```

docker build 生成镜像。
```
root@戴燚:/home/daiyi/Documents/study/docker/nginx-test# docker build . -t daiyi-nginx:text4
Sending build context to Docker daemon   5.12kB
Step 1/9 : FROM python:2.7.15-alpine3.8
 ---> 309337f1f167

```
查看效果。
```
root@戴燚:/home/daiyi/Documents/study/docker/nginx-test# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
daiyi-nginx         text4               b7d509aa7855        9 seconds ago       58.3MB
daiyi-nginx         text3               6805da1d86da        8 minutes ago       58.3MB
daiyi-nginx         text2               6febfbc0b3eb        13 minutes ago      58.3MB
falcon-dashboard    local               b05fa36213a4        3 weeks ago         353MB
python              2.7.15-alpine3.8    309337f1f167        7 weeks ago         58.3MB
root@戴燚:/home/daiyi/Documents/study/docker/nginx-test# docker run -it --name="daiyi4" daiyi-nginx:text4
/daiyi_nginx/dashboard # ls
Dockerfile            bb                    nginx                 test.txt
aa                    cc                    pip_requirements.txt
/daiyi_nginx/dashboard # pwd
/daiyi_nginx/dashboard
```

## 删除docker images
docker rmi -f 强制删除
```
 for i in `docker images|awk -F" " '{for(i=3;i<(NR-2);i++){print $3}}'`;do docker rmi -f $i;done
```
 删除docker images中为none的镜像
```
docker images|grep none|awk '{print $3 }'|xargs docker rmi

```
或者。
```
docker rmi -f $(docker images | grep <none> | awk '{print $3}')
```

```
强制删除镜像名称中包含“doss-api”的镜像
docker rmi --force $(docker images | grep doss-api | awk '{print $3}')

杀死所有正在运行的容器
docker kill $(docker ps -a -q)
删除所有已经停止的容器
docker rm $(docker ps -a -q)
删除所有未打 dangling 标签的镜像
docker rmi $(docker images -q -f dangling=true)
删除所有镜像
docker rmi $(docker images -q)

删除停止的容器
docker rm $(docker ps --all -q -f status=exited)
删除没有使用的镜像
docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}")

批量删除镜像
docker images | awk '{print $3}' | xargs docker rmi
批量删除容器
docker ps -a | awk '{print $1}' | xargs docker rm
如果需要根据具体的容器名或镜像名过滤的话，可以修改上面的awk表达式进行处理。
类似这样，删除test_开头的镜像：
docker rmi -f $(docker images --format "{{.Repository}}" |grep "^test_*")
```

后面参考：https://blog.csdn.net/xl_lx/article/details/81565910 

## entrypoint = /bin/bash 的使用
```
DOCKFILE 

FROM python:2.7.15-wheezy

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]
```


```

MacBook-Pro:sls-devops daiyi$ docker run -it --rm --entrypoint=/bin/sh reg.docker.www.com/sls-devops/kv_conf_checker 
# ls
after_check  kv_conf_checker.py  requirements.txt
# exit
MacBook-Pro:sls-devops daiyi$ ls
Makefile                docs                    generate_sign_url.py    src
README.md               downloader.py           requirements.txt        tests
```

## docker 网络
[参考文章](https://www.jianshu.com/p/19cd3654e4a4)
[参考文章2](https://github.com/johnnian/Blog/issues/16)
```

#docker network ls
NETWORK ID          NAME                DRIVER              SCOPE                     Up 3 weeks                                      cruiser.cruiserSR__.cruis
35ad4a345e60        bridge              bridge              local
92d132ed6e29        host                host                local                     Exited (0) 14 minutes ago                       cruiser.ServiceTest__.ser
30681a7be75e        none                null                local
6cdfe78708ee        nw_10.3.200.0_24    alinet              local                     Exited (0) 2 seconds ago                        repair.dbInit__.db-init.1
76e678ba568a        nw_10.3.4.0_23      alinet              local
                                                                                      Up 3 weeks                                      yamaService.yamaServerRol


[root@amtest73]
#docker network create --subnet=172.18.0.0/16 daiyi-network
ce25111825b4102498bd76f61780de1dcf75c12ab166c9a61c7d387183c5baa3

[root@amtest73]
#docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
35ad4a345e60        bridge              bridge              local
ce25111825b4        daiyi-network       bridge              local
92d132ed6e29        host                host                local
30681a7be75e        none                null                local
6cdfe78708ee        nw_10.3.200.0_24    alinet              local                        0.0.1
76e678ba568a        nw_10.3.4.0_23      alinet              local

[root@amtest73]
#docker run -it  --net daiyi-network --ip 172.18.0.6 daiyi-get-method:0.0.1 /bin/bash
root@b9eaf00d71a0:/#

## host  
docker run -it  --net daiyi-network daiyi-get-method:0.0.1 /bin/bash
root@o5rffo8u74dho:/#
```
