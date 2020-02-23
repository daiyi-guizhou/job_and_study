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