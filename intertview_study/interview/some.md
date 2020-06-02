谷歌浏览区打开不同的窗口是进程还是线程？
	为了确保用户的安全性和稳定性，浏览器不得不改进浏览器的性能，其中之一就是向用户提供多进程浏览

GBK 编码代替 UTF-8 编码
	UTF-8是全球统一编码
	GBK 编码是中文编码

RPC
	什么是rpc
		RPC就是从一台机器（客户端）上通过参数传递的方式调用另一台机器（服务器）上的一个函数或方法（可以统称为服务）并得到返回的结果。RPC会隐藏底层的通讯细节（不需要直接处理Socket通讯或Http通讯）客户端发起请求，服务器返回响应（类似于Http的工作方式）RPC在使用形式上像调用本地函数（或方法）一样去调用远程的函数（或方法）
	原理
		总体思路都是服务提供方暴露服务，消费方通过服务方提供的接口使用动态代理获取代理对象，然后调用代理对象的方法，代理对象在内部进行远程调用，获得计算结果。

ping通反应很慢，调用远程服务反应时间很长的原因（远程服务端阻塞，本地TCP粘包）


为什么会出现4.0-3.6=0.40000001这种现象
	在二进制系统中无法精确地表示分数1/10，这就好像十进制无法精确地表示分数1/3一样


<!-- TOC -->

- [Python语言特性](#python%E8%AF%AD%E8%A8%80%E7%89%B9%E6%80%A7)
- [操作系统](#%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F)
- [数据库](#%E6%95%B0%E6%8D%AE%E5%BA%93)
- [网络](#%E7%BD%91%E7%BB%9C)
- [数据结构](#%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)
- [编程题](#%E7%BC%96%E7%A8%8B%E9%A2%98)

<!-- /TOC -->

在这给大家列出了最新的一些 Python 面试题，如果你看这些题，基本都能回答上来，那你肯定可以去面试找工作了。
如果有一些回答不上来也不要紧，我也给大家附上了答案，可以看看自己哪里有欠缺，学习一下就好了。
这些面试题来源于 GitHub 项目：https://github.com/taizilongxu/interview_python
Table of Contents

## Python语言特性
1 Python的函数参数传递
2 Python中的元类(metaclass)
3 @staticmethod和@classmethod
4 类变量和实例变量
5 Python自省
6 字典推导式
7 Python中单下划线和双下划线
8 字符串格式化:\x和.format
9 迭代器和生成器
10 *args and **kwargs
11 面向切面编程AOP和装饰器
12 鸭子类型
13 Python中重载
14 新式类和旧式类
15 __new__和init的区别
16 单例模式
1 使用__new__方法
2 共享属性
3 装饰器版本
4 import方法
17 Python中的作用域
18 GIL线程全局锁
19 协程
20 闭包
21 lambda函数
22 Python函数式编程
23 Python里的拷贝
24 Python垃圾回收机制
1 引用计数
2 标记-清除机制
3 分代技术
25 Python的List
26 Python的is
27 read,readline和readlines
28 Python2和3的区别
29 super init
30 range and xrange

## 操作系统
1 select,poll和epoll
2 调度算法
3 死锁
4 程序编译与链接
1 预处理
2 编译
3 汇编
4 链接
5 静态链接和动态链接
6 虚拟内存技术
7 分页和分段
分页与分段的主要区别
8 页面置换算法
9 边沿触发和水平触发

## 数据库
1 事务
2 数据库索引
3 Redis原理
Redis是什么？
Redis数据库
Redis缺点
4 乐观锁和悲观锁
5 MVCC
MySQL的innodb引擎是如何实现MVCC的
6 MyISAM和InnoDB

## 网络
1 三次握手
2 四次挥手
3 ARP协议
4 urllib和urllib2的区别
5 Post和Get
6 Cookie和Session
7 apache和nginx的区别
8 网站用户密码保存
9 HTTP和HTTPS
10 XSRF和XSS
11 幂等 Idempotence
12 RESTful架构(SOAP,RPC)
13 SOAP
14 RPC
15 CGI和WSGI
16 中间人攻击
17 c10k问题
18 socket
19 浏览器缓存
20 HTTP1.0和HTTP1.1
21 Ajax
*NIX
unix进程间通信方式(IPC)

## 数据结构
1 红黑树

## 编程题
1 台阶问题/斐波那契
2 变态台阶问题
3 矩形覆盖
4 杨氏矩阵查找
5 去除列表中的重复元素
6 链表成对调换
7 创建字典的方法
1 直接创建
2 工厂方法
3 fromkeys()方法
8 合并两个有序列表
9 交叉链表求交点
10 二分查找
11 快排
12 找零问题
13 广度遍历和深度遍历二叉树
17 前中后序遍历
18 求最大树深
19 求两棵树是否相同
20 前序中序求后序
21 单链表逆置
22 两个字符串是否是变位词
23 动态规划问题

详细题目和答案请见：
taizilongxu/interview_python