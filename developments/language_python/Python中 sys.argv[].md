参考链接(https://www.cnblogs.com/aland-1415/p/6613449.html)
 sys.argv[] 就是用来执行脚本时，向脚本里传入参数的 
  python XX.py   kkkk   #就是给XX.py 传入了kkkk的参数。也可以是多个， 详见例子。
  
直接传入，
```
import sys

print(sys.argv) 

G:\python\day2>python argv.py
['argv.py']
G:\python\day2>python argv.py ii
['argv.py', 'ii']
G:\python\day2>python argv.py ii ll kkd
['argv.py', 'ii', 'll', 'kkd']
'''
```
传入0个，输出本身， 就是 脚本名字，
  

```
a=sys.argv[0]
print(a)

G:\python\day2>python argv.py ii ll kkd
argv.py
G:\python\day2>python argv.py
argv.py
```

传入1个

```
a=sys.argv[1]
print(a)

G:\python\day2>python argv.py yity
yity
G:\python\day2>python argv.py yity 78798
yity
```
传入多个

```
a=sys.argv[2:]
print(a)

G:\python\day2>python argv.py a b c d e f
['b', 'c', 'd', 'e', 'f']
G:\python\day2>python argv.py yity 78798 ueeit eiwet
['78798', 'ueeit', 'eiwet']
```




