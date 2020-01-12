参看(http://www.googlinux.com/list-all-tags-of-docker-image/index.html)
参考链接(https://nickjanetakis.com/blog/docker-tip-81-searching-the-docker-hub-on-the-command-line)
例如，查找 python 关于2.7.15的所有tag.
```
$ image=python;curl https://registry.hub.docker.com/v1/repositories/$image/tags | sed -e 's/[][]//g' -e 's/"//g' -e 's/ //g' |tr '}' '\n'  | awk -F: '{print $3}'|grep 2.7.15
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 36373    0 36373    0     0  22747      0 --:--:--  0:00:01 --:--:-- 22904
2.7.15
2.7.15-alpine
2.7.15-alpine3.4
2.7.15-alpine3.6
2.7.15-alpine3.7
2.7.15-alpine3.8
2.7.15-alpine3.9
2.7.15-jessie
2.7.15-onbuild
2.7.15-slim
2.7.15-slim-jessie
2.7.15-slim-stretch
2.7.15-stretch
2.7.15-wheezy
2.7.15-windowsservercore
2.7.15-windowsservercore-1709
2.7.15-windowsservercore-1803
2.7.15-windowsservercore-1809
2.7.15-windowsservercore-ltsc2016
```
看看 python镜像一共有多少个tag 
```
$ image=python;curl https://registry.hub.docker.com/v1/repositories/$image/tags | sed -e 's/[][]//g' -e 's/"//g' -e 's/ //g' |tr '}' '\n'  | awk -F: '{print $3}'|wc -l
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 36373    0 36373    0     0  26167      0 --:--:--  0:00:01 --:--:-- 26205
856

```
这个地址能获得所有tags, (https://registry.hub.docker.com/v1/repositories/$image/tags)
$image换成你的镜像名字，如 python （https://registry.hub.docker.com/v1/repositories/python/tags）
