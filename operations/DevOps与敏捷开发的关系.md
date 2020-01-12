devOps 流程
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191101213855228.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
programming_process
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191101213932126.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)
```
#encoding:UTF-8  
def yield_test(n):  
    for i in range(n):  
        yield call(i)  
        print("i=",i)  
    #做一些其它的事情      
    print("do something.")      
    print("end.")  
  
def call(i):  
    return i*2  
  
#使用for循环  
def kk(jj):
    for i in yield_test(jj):  
        print(i,",####") 
 ```
        
"""
阅读别人的python源码时碰到了这个yield这个关键字，各种搜索终于搞懂了，在此做一下总结：

通常的for...in...循环中，in后面是一个数组，这个数组就是一个可迭代对象，类似的还有链表，字符串，文件。它可以是mylist = [1, 2, 3]，也可以是mylist = [x*x for x in range(3)]。
它的缺陷是所有数据都在内存中，如果有海量数据的话将会非常耗内存。
生成器是可以迭代的，但只可以读取它一次。因为用的时候才生成。比如 mygenerator = (x*x for x in range(3))，注意这里用到了()，它就不是数组，而上面的例子是[]。
我理解的生成器(generator)能够迭代的关键是它有一个next()方法，工作原理就是通过重复调用next()方法，直到捕获一个异常。可以用上面的mygenerator测试。
带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代，工作原理同上。
yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
带有yield的函数不仅仅只用于for循环中，而且可用于某个函数的参数，只要这个函数的参数允许迭代参数。比如array.extend函数，它的原型是array.extend(iterable)。
send(msg)与next()的区别在于send可以传递参数给yield表达式，这时传递的参数会作为yield表达式的值，而yield的参数是返回给调用者的值。——换句话说，就是send可以强行修改上一个yield表达式值。比如函数中有一个yield赋值，a = yield 5，第一次迭代到这里会返回5，a还没有赋值。第二次迭代时，使用.send(10)，那么，就是强行修改yield 5表达式的值为10，本来是5的，那么a=10
send(msg)与next()都有返回值，它们的返回值是当前迭代遇到yield时，yield后面表达式的值，其实就是当前迭代中yield后面的参数。
第一次调用时必须先next()或send(None)，否则会报错，send后之所以为None是因为这时候没有上一个yield(根据第8条)。可以认为，next()等同于send(None)

作者：千若逸
链接：https://www.jianshu.com/p/d09778f4e055
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
```
# 理解的关键在于：下次迭代时，代码从yield的下一跳语句开始执行。
kk(1)
# (0, ',####')
# ('i=', 0)
# do something.
# end.

kk(2)
# (0, ',####')
# ('i=', 0)
# (2, ',####')
# ('i=', 1)
# do something.
# end.

kk(5)
# (0, ',####')
# ('i=', 0)
# (2, ',####')
# ('i=', 1)
# (4, ',####')
# ('i=', 2)
# (6, ',####')
# ('i=', 3)
# (8, ',####')
# ('i=', 4)
# do something.
# end.



# >>> 
# >>> def g():
# ...     print "1"
# ...     x = yield "hello"
# ...     print "2","x =",x
# ...     y=5 + (yield x)
# ...     print "3","y = ",y
# ... 
# >>> f=g()
# >>> 
# >>> f.next()
# 1
# 'hello'
# >>> f.send(5)
# 2 x = 5
# 5
# >>> f.send(2)
# 3 y =  7
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> 
```

"""
#生成器
l=(i for i in range(10) if i%2 == 0)

#<generator object <genexpr> at 0x028E1CD8>
#协程
'''
子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，
C执行完毕返回，B执行完毕返回，最后是A执行完毕。
所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，
在适当的时候再返回来接着执行。
但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？
最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，
没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，
又充分发挥协程的高效率，可获得极高的性能。
Python对协程的支持还非常有限，用在generator中的yield可以一定程度上实现协程。虽然支持不完全，但已经可以发挥相当大的威力了
传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，
但一不小心就可能死锁。
如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后
切换回生产者继续生产，效率极高：


“子程序就是协程的一种特例。”

函数内使用yield变成生成器，func.next(),遇到yield就返回yield后面跟的值，
下次调用直接从yield的位置开始
如果c=func(),c.send(i)，那么yield的位置会获取i这个值，生成器函数不会返回，会继续运行yield下面的操作
'''
```
def consumer():
    r=''
    while True:
        n=yield r
        print('吃货:包子[%s]来了，吃包子' %n)
        time.sleep(1)
        r='200 ok'

def producer(c):
    c.next()
    for i in range(5):
        print('厨师:包子[%s]做好了' %i)
        r=c.send(i)
        print('厨师:包子被取走了，状态码为%s' %r)
    c.close()
producer(consumer())
```


#运行结果


厨师:包子[0]做好了
吃货:包子[0]来了，吃包子
厨师:包子被取走了，状态码为200 ok
厨师:包子[1]做好了
吃货:包子[1]来了，吃包子
厨师:包子被取走了，状态码为200 ok
厨师:包子[2]做好了
吃货:包子[2]来了，吃包子
厨师:包子被取走了，状态码为200 ok
厨师:包子[3]做好了
吃货:包子[3]来了，吃包子
厨师:包子被取走了，状态码为200 ok
厨师:包子[4]做好了
吃货:包子[4]来了，吃包子
厨师:包子被取走了，状态码为200 ok

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，
而非线程的抢占式多任务。
"""
