linux机器中， 某个服务， 启动脚本在/etc/init.d/ 目录下， 当我们 把 home的文件，配置等被覆盖更新后，    /etc/init.d/启动脚本没变，    这时，启动就会报错，如下
```
[admin@a34h11078.cloud.h11.amtest87 /cloud/app/sls-backend-server/SlsWeb#/sls_web/current]
$sudo /etc/init.d/sls-webd restart
Restarting sls-webd (via systemctl):  Job for sls-webd.service failed because the control process exited with error code. See "systemctl status sls-webd.service" and "journalctl -xe" for details.
                                                           [FAILED]

[admin@a34h11078.cloud.h11.amtest87 /cloud/app/sls-backend-server/SlsWeb#/sls_web/current]
```
短期解释是这样
解法：      
1  服务需要 reload  。 这样才能算是 重新的， 
2  更改启动脚本位置， 更改之后 不受linux 系统管控， 比如，把 启动脚本 和  sls-webd的配置文件等放在 它自己的home目录下，  这样更改时一起更改。  再次启动就不会有 这个问题了， 
