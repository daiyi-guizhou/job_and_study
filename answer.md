[]()
[]()
[]()
[]()
[]()
[]()


[How To Ask Questions The Smart Way](http://www.catb.org/~esr/faqs/smart-questions.html)
[How To Ask Questions The Smart Way-zh_CN](https://github.com/ruby-china/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)

[简析Linux中 /proc/[pid] 目录的各文件](https://www.linuxprobe.com/linux-proc-pid.html)


[如何查询一个进程下面的线程数（进程和线程区别）](https://www.cnblogs.com/kevingrace/p/5252919.html)

[Shell是什么？1分钟理解Shell的概念！](http://c.biancheng.net/view/706.html)


[怎么在一台电脑上配置两个git账号](https://www.zhihu.com/question/268617758/answer/649794531)




《HelloGitHub》  月刊



## 开源文档软件 ：--mindoc
[amWiki](https://blog.csdn.net/cjmqas/article/details/78363116?utm_source=blogxgwz0)
[改进的 amWiki](http://weyo.me/pages/techs/wikis-by-amwiki/)
[githug 搭建 附属的wiki--amWiki](http://amwiki.org/doc/?file=020-%E6%95%99%E7%A8%8B%E5%AD%A6%E4%B9%A0%E7%AF%87/007-%E4%BD%BF%E7%94%A8%E5%AF%BC%E5%87%BA%E5%88%9B%E5%BB%BA%E9%99%84%E5%B1%9Ewiki#Github%20Pages%EF%BC%9A)
[如何把 GitHub 用作个人 wiki 知识库？](https://www.zhihu.com/question/27027157)
[wiki 托管到 github](https://doc.iminho.me/docs/mindoc/mindoc-1cme3u1tc2p8r)

[some_details](https://www.v2ex.com/t/601277)
```md
最近部门内部想搞知识管理，原本用文件服务器（ word、execl 之类）的，很不方便。尝试了一些开源的 wiki、在线文档方案，都不太理想。最理想的应该是语雀，但只有在线的，没有开源私有部署，不知道大家的公司内部是怎么管理日常沉淀的知识经验

需求：Markdown 编辑、权限控制、LDAP、内容组织管理（文档树、专栏、全文搜索）

PS：试过 mindoc、showdoc、Requarks、raneto、docify、语雀、腾讯乐享、NodeBB、Xiuno

目前就 mindoc 比较接近，但比较简陋，每篇文档都是一个项目形式，不好管理和展示，希望能类似语雀那种文档管理方式

```
* [wikijs](https://github.com/Requarks/wiki)  适合一系列的文档，或者 API 之类，不适合部门的知识积累，因为有些内容是零散的或者不同类型的，所以希望有文档树的形式，也要有专栏（一篇篇文章）的形式
* 语雀    不是开源的，公司只能使用私有部署的方案（线上数据安全避不开）
* confluences    收费，是中型公司必备； confluence 偏向 wiki 形式，试过的很多都是类似 wiki 的单一组织形式，想找的是 wiki+文章的形式。因为部门知识管理，除了业务这种组织性比较强外，也还有零碎的经验分享知识
* BookStack
* taiga  可以支持 LDAP 权限，但是不支持树形结构，基本上涉及到权限的就会有定制
* Notion   呢？你说的功能应该都有，不过 ldap 好像是跟着 gsuite 的
* documize,
* armwiki

