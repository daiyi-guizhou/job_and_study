首先感谢各位前辈踩过的坑，总结的经验，贡献的力量。
Gitlab CI yaml官方配置文件翻译  (https://segmentfault.com/a/1190000010442764)
参考资料汇总(https://github.com/Fennay/gitlab-ci-cn)

#话不多说，先看代码

```
image: ubuntu:latest             #由于我用 ubuntu的deb打包，所以需要ubuntu的环境，#若不加容器镜像，它默认是一个linux的。那就不能打包了。

variables:                             #变量是用来 容器和缓存之间交互的。
  filename: "falcon_agent-*.deb"

stages:
  - build

build:falcon-agent:
  stage: build
  script: 
   - sh build_dpkg.sh     #此处执行脚本， 他默认会把你提交到git 上的代码都pull下来。 之前报错，没找到build_dpkg.sh，后来用image 和  sh build_dpkg.sh 后就好了。

  artifacts:             #一开始我没有这个，所以ci文件能pass，却没有包。这个就是用来生成包。留在gitlab上，给人下载的。
    paths:
     - $filename         #此处 一开始我用  *.deb.希望能匹配，结果报错。 用.deb可以，但是zip文件里是空的，看来是需要指定。
     					#此处。我的deb在当前路径，所以直接用

```
#关于build_dpkg.sh。如下
```
#!/bin/bash
rm *.deb
DATE=`date '+%Y%m%d_%H%M%S'`
FILENAME=falcon_agent-${DATE}.deb

chmod -R 755 deb
chmod -R 755 deb/DEBIAN       #这两句 chmod之间没加，结果ci就报错 dpkg-deb: error: control directory has bad permissions 777 (must be >=0755 and <=0775),加上之后就完事。
dpkg-deb -b deb $FILENAME

```
ci叫持续集成。方便你的 代码做测试的。还能生成文件。  给开发，测试用的。 
1 在你的gitlab下注册安装ci。 重点 .gitlab-ci.yml文件。
2 注册安装 gitlab-runner，他就是一个服务器，用来执行 .gitlab-ci.yml文件。

感谢前人
参考资料
(https://www.jianshu.com/p/2b43151fb92e)
(https://rpadovani.com/introduction-gitlab-ci)
(https://www.imooc.com/article/27950)
