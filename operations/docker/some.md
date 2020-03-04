<!-- TOC -->

- [--net  host  网络连通](#--net--host--网络连通)
- [docker stats  [containID]  查看容器的 运行消耗资源](#docker-stats--containid--查看容器的-运行消耗资源)
- [moby、docker-ce与docker-ee](#mobydocker-ce与docker-ee)
- [查询容器的日志](#查询容器的日志)

<!-- /TOC -->

docker
`docker run -it --net host --rm reg.docker.alibaba-inc.com/aliyun-sls/aliyun-log-cli:{{LOG_CLI_IMAGES_TAG}} --version`

## --net  host  网络连通
`docker run -it --net=host -v /cloud/app/sls-common/ServiceTest#/service_test2:/home/admin/sls/smoke_test2 --entrypoint=/bin/sh --name daiyi_test bigdata_sls_test:0b7d2b`
docker.ori: Error response from daemon: -e RequestedIP or --ip not set.
See 'docker.ori run --help'.
	 while [[ true ]];do echo time sleep 1 >/dev/null 2>&1;docker stats --no-stream|grep aedfae9724a8;done

## docker stats  [containID]  查看容器的 运行消耗资源
		
```
[root@a34h05007.cloud.h05.amtest87 /root]
#docker stats --no-stream|head -n 1;while [[ true ]];do echo time sleep 1 >/dev/null 2>&1;docker stats --no-stream|grep aedfae9724a8;done
CONTAINER           CPU %               MEM USAGE / LIMIT       MEM %               NET I/O               BLOCK I/O             PIDS
aedfae9724a8        119.02%             85.88 GiB / 94.28 GiB   91.08%              0 B / 0 B             12.29 kB / 33.52 MB   4
aedfae9724a8        126.96%             86.16 GiB / 94.28 GiB   91.39%              0 B / 0 B             12.29 kB / 33.52 MB   4
aedfae9724a8        72.66%              86.34 GiB / 94.28 GiB   91.58%              0 B / 0 B             12.29 kB / 33.52 MB   4
aedfae9724a8        54.95%              86.56 GiB / 94.28 GiB   91.81%              0 B / 0 B             12.29 kB / 33.52 MB   4
```

## moby、docker-ce与docker-ee
最早的时候docker就是一个开源项目，主要由docker公司维护。

2017年年初，docker公司将原先的docker项目改名为moby，并创建了docker-ce和docker-ee。

这三者的关系是：

moby是继承了原先的docker的项目，是社区维护的的开源项目，谁都可以在moby的基础打造自己的容器产品

docker-ce是docker公司维护的开源项目，是一个基于moby项目的免费的容器产品
docker-ee是docker公司维护的闭源产品，是docker公司的商业产品。

moby project由社区维护，docker-ce project是docker公司维护，docker-ee是闭源的。
要使用免费的docker，从网页docker-ce上获取。

要使用收费的docker，从网页docker-ee上获取。

docker-ce的发布计划
v1.13.1之后，发布计划更改为:

Edge:   月版本，每月发布一次，命名格式为YY.MM，维护到下个月的版本发布
Stable: 季度版本，每季度发布一次，命名格式为YY.MM，维护4个月
docker-ce的release计划跟随moby的release计划，可以使用下面的命令直接安装最新的docker-ce:

curl -fsSL https://get.docker.com/ | sh

## 查询容器的日志
docker logs 9cde82398064