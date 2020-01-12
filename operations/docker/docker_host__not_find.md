

#docker ps   查看， 所有端口都 做了映射，

```root@ubuntu-10:/home/work/open-falcon# docker ps
CONTAINER ID        IMAGE                            COMMAND             CREATED             STATUS              PORTS                                                                                                                                                                                                                                                                                                    NAMES
764b158ba491        open-falcon-plus-02:v-daiyi-01   "/bin/bash"         2 days ago          Up 3 hours          0.0.0.0:4444->4444/tcp, 0.0.0.0:6030-6031->6030-6031/tcp, 0.0.0.0:6070-6071->6070-6071/tcp, 0.0.0.0:6080-6081->6080-6081/tcp, 0.0.0.0:8080-8081->8080-8081/tcp, 0.0.0.0:8433->8433/tcp, 0.0.0.0:9912->9912/tcp, 0.0.0.0:14444->14444/tcp, 0.0.0.0:16060->16060/tcp, 0.0.0.0:18433->18433/tcp, 8082/tcp   open-falcon-plus-daiyi-01
```



#但是查看日志 
tail -40 /home/work/open-falcon/agent/logs/agent.log

```
test@ubuntu-10:/tmp/bak$ tail -40 /home/work/open-falcon/agent/logs/agent.log
2018/10/14 20:27:09 transfer.go:48: call Transfer.Update fail: &{{2 1} <nil> 10.0.10.103:8433 1s} dial tcp 10.0.10.103:8433: getsockopt: connection refused
2018/10/14 20:27:09 var.go:95: <= <Total=0, Invalid:0, Latency=0ms, Message:>
2018/10/14 20:27:09 rpc.go:41: dial 10.0.10.103:8433 fail: dial tcp 10.0.10.103:8433: getsockopt: connection refused
2018/10/14 20:27:11 rpc.go:41: dial 10.0.10.103:8433 fail: dial tcp 10.0.10.103:8433: getsockopt: connection refused
2018/10/14 20:27:15 rpc.go:41: dial 10.0.10.103:8433 fail: dial tcp 10.0.10.103:8433: getsockopt: connection refused
2018/10/14 20:27:23 rpc.go:41: dial 10.0.10.103:8433 fail: dial tcp 10.0.10.103:8433: getsockopt: connection refused
2018/10/14 20:27:23 transfer.go:48: call Transfer.Update fail: &{{0 0} <nil> 10.0.10.103:8433 1s} dial tcp 10.0.10.103:8433: getsockopt: connection refused
2018/10/14 20:27:23 var.go:95: <= <Total=0, Invalid:0, Latency=0ms, Message:>
2018/10/14 20:27:41 var.go:88: => <Total=92> <Endpoint:ubuntu, Metric:agent.alive, Type:GAUGE, Tags:, Step:60, Time:1539574061, Value:1>
2018/10/14 20:27:41 var.go:88: => <Total=5> <Endpoint:ubuntu, Metric:df.bytes.free.percent, Type:GAUGE, Tags:mount=/,fstype=ext4, Step:60, Time:1539574061, Value:67.01861018345224>
```

但是无法访问 
原因： **docker里面的host不能配置127.0.0.1 或者192.168.0.1 或则宿主机器将无法访问端口**

修改配置文件---（涉及到的，需要外部访问的都需要修改）
```
[root@ubuntu-10 open-falcon]# vim transfer/config/cfg.json
{
    "debug": true,
    "minStep": 30,
    "http": {
        "enabled": true,
        "listen": "0.0.0.0:6060"
    },
    "rpc": {
        "enabled": true,
        "listen": "0.0.0.0:8433"  **#此处监听外面8433. 改成0.0.0.0**
    },
    "socket": {
        "enabled": true,
        "listen": "0.0.0.0:4444",
        "timeout": 3600
    },
    "judge": {
        "enabled": true,
        "batch": 200,
        "connTimeout": 1000,
        "callTimeout": 5000,
        "maxConns": 32,
        "maxIdle": 32,
        "replicas": 500,
        "cluster": {
            "judge-00" : "127.0.0.1:6080"
        }
    },
    "graph": {
        "enabled": true,
        "batch": 200,
        "connTimeout": 1000,
        "callTimeout": 5000,
        "maxConns": 32,
        "maxIdle": 32,
        "replicas": 500,
        "cluster": {
            "graph-00" : "127.0.0.1:6070"

        }
    },
    "tsdb": {
        "enabled": false,
        "batch": 200,
        "connTimeout": 1000,
        "callTimeout": 5000,
        "maxConns": 32,
        "maxIdle": 32,
        "retry": 3,
        "address": "127.0.0.1:8088"
    }

```

修改好之后重启 docker里的服务，
[root@ubuntu-10 open-falcon]# ./open-falcon restart transfer

再次查看日志，

```
test@ubuntu-10:/tmp/bak$ tail -40 /home/work/open-falcon/agent/logs/agent.log 
2018/10/15 02:52:48 var.go:88: => <Total=1> <Endpoint:test-endpoint, Metric:test-metric-97, Type:GAUGE, Tags:idc=lgi-test,loc=beijing-test, Step:20, Time:1539597168, Value:33>
2018/10/15 02:52:48 var.go:95: <= <Total=1, Invalid:0, Latency=0ms, Message:ok>
2018/10/15 02:52:48 var.go:88: => <Total=1> <Endpoint:test-endpoint, Metric:test-metric-97, Type:GAUGE, Tags:idc=lgi-test,loc=beijing-test, Step:20, Time:1539597168, Value:33>
2018/10/15 02:52:48 var.go:95: <= <Total=1, Invalid:0, Latency=0ms, Message:ok>
2018/10/15 02:52:48 var.go:88: => <Total=1> <Endpoint:test-endpoint, Metric:test-metric-97, Type:GAUGE, Tags:idc=lgi-test,loc=beijing-test, Step:20, Time:1539597168, Value:33>
2018/10/15 02:52:48 var.go:95: <= <Total=1, Invalid:0, Latency=0ms, Message:ok>  #连接成功，数据传入。

```
查看端口的连接性

```
test@ubuntu-10:/tmp/bak$ telnet 10.0.10.103 8433
Trying 10.0.10.103...
Connected to 10.0.10.103.
Escape character is '^]'.      #这就是ok的
```

能连接成功，






