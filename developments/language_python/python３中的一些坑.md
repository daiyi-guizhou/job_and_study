<!-- TOC -->

- [理解Python的UnboundLocalError（Python的作用域）](#理解python的unboundlocalerrorpython的作用域)
        - [解决方法](#解决方法)

<!-- /TOC -->

参考链接(https://www.kawabangga.com/posts/2245)
# 理解Python的UnboundLocalError（Python的作用域）
今天写代码碰到一个百思不得解为什么会出错的代码，简化如下：

```
x = 10
def func():
    if something_true():
        x = 20
    print(x)
 
func()
```
意图很明显，首先我定义了一个全局的x，在函数中，如果有特殊需要，就重新重新赋值一下x，否则就使用全局的x。

可以这段代码在运行的时候抛出这个Error：

    UnboundLocalError: local variable ‘a’ referenced before assignment

### 解决方法
显示地指定使用global就可以，这样即使出现赋值，也不会产生作为local的变量，而是去改变global的变量。
但是依然存在一个问题：

```

def external():
    x = 10
    def internal():
        global x
        x += 1
        print(x)
    internal()
 
external()
```
external的x既不是local，也不是global。这种情况应该使用Python3的nonlocal。这样Python不会在当前的作用域找x，会去上一层找。


在一个函数里写了这样一个代码，但是， 
```
count_alarm=0
        for value in valueslist:
            if value <= threshold:
                count_alarm =+ 1
            print(count_alarm)
```

```
1
1
1
```
很不解，由+=改为  count_alarm = count_alarm + 1  它就好了。 
```
count_alarm=0
        for value in valueslist:
            if value <= threshold:
                count_alarm = count_alarm + 1
            print(count_alarm)
```

```
1
2
3
```

