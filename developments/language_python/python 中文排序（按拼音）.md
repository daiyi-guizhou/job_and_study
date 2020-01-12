### pypinyin
1 排序 仅按拼音首字母 排序
安装pypinyin
```
pip3 install pypinyin
```
代码
```
from pypinyin import lazy_pinyin

chars = ['鑫','鹭','榕','柘','珈','骅','孚','迦','瀚','濮','浔','沱','泸','恺','怡','岷','萃','兖']
chars.sort(key=lambda char: lazy_pinyin(char)[0][0])
print([lazy_pinyin(char) for char in chars])
print(chars)
```
结果
```

[['cui'], ['fu'], ['hua'], ['han'], ['jia'], ['jia'], ['kai'], ['lu'], ['lu'], ['min'], ['pu'], ['rong'], ['tuo'], ['xin'], ['xun'], ['yi'], ['yan'], ['zhe']]
['萃', '孚', '骅', '瀚', '珈', '迦', '恺', '鹭', '泸', '岷', '濮', '榕', '沱', '鑫', '浔', '怡', '兖', '柘']
```
### 按所有拼音排序

```
#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

# from __future__ import unicode_literals
from pypinyin import lazy_pinyin

def sort_pinyin(hanzi_list):        
    hanzi_list_pinyin=[]
    hanzi_list_pinyin_alias_dict={}
    for single_str in hanzi_list:
        py_r = lazy_pinyin(single_str)
        # print("整理下")
        single_str_py=''
        for py_list in py_r:
            single_str_py=single_str_py+py_list
        hanzi_list_pinyin.append(single_str_py)
        hanzi_list_pinyin_alias_dict[single_str_py]=single_str
    hanzi_list_pinyin.sort()
    sorted_hanzi_list=[]
    for single_str_py in hanzi_list_pinyin:
        sorted_hanzi_list.append(hanzi_list_pinyin_alias_dict[single_str_py])
    return sorted_hanzi_list

str=['床前', '明月', '光','疑是','地上霜','举头','望','明月','低头','思','故乡'] 
print(str)
str=sort_pinyin(str)
print(str)
```

```
['床前', '明月', '光', '疑是', '地上霜', '举头', '望', '明月', '低头', '思', '故乡']
['床前', '地上霜', '低头', '光', '故乡', '举头', '明月', '明月', '思', '望', '疑是']
```

### 使用pypinyin必须传入unicode字符串
##### 例子1

```
#!/usr/bin/python
# -*- coding: UTF-8 -*- 
from pypinyin import pinyin, lazy_pinyin
py_r = pinyin(u"学python,我在行")
print py_r
print("整理下")
for py in py_r:
    for p in py: 
        print p,"",
#发现上面的"行"字是多音字，本应念"han"
print("\n启动多音字")
py_r = pinyin(u"学python,我在行", heteronym=True)
print py_r
for py in py_r:
    for p in py: 
        print p,"",

```

```
(venv) allenwoo@~/renren$ python test.py 
[[u'xu\xe9'], [u'python,'], [u'w\u01d2'], [u'z\xe0i'], [u'x\xedng']]
整理下
xué  python,  wǒ  zài  xíng  
启动多音字
[[u'xu\xe9'], [u'python,'], [u'w\u01d2'], [u'z\xe0i'], [u'x\xedng', u'h\xe1ng', u'x\xecng', u'h\xe0ng', u'h\xe9ng']]
xué  python,  wǒ  zài  xíng  háng  xìng  hàng  héng
```



##### 例子2：

```
#!/usr/bin/python
# -*- coding: UTF-8 -*- 
from pypinyin import pinyin, lazy_pinyin
# 不需要声调
py_r = lazy_pinyin(u"没有了诗和远方")
print py_r
 
# 特殊字符
# 默认
py_r = lazy_pinyin(u"满天都是小☆☆")
print py_r
 
# 不理睬，忽略
py_r = lazy_pinyin(u"满天都是小☆☆", errors=u'ignore')
print py_r
 
# 替换
py_r = lazy_pinyin(u"满天都是小☆☆", errors=u'replace')
 
# 也可以使用回调函数处理
py_r = lazy_pinyin(u"满天都是小☆☆", errors=lambda x: 'star')
print py_r
```

```
(venv) allenwoo@~/renren$ python test.py 
[u'mei', u'you', u'le', u'shi', u'he', u'yuan', u'fang']
[u'man', u'tian', u'dou', u'shi', u'xiao', u'\u2606\u2606']
[u'man', u'tian', u'dou', u'shi', u'xiao']
[u'man', u'tian', u'dou', u'shi', u'xiao', 'star']
```




在第1个例子中，我们发现这个模块会简单分词，将"python"分为一个词
而且其他的中文词语并没有按词分开后再转拼音
##### 自定义库：####

```
** 使用load_phrases_dict,自定义拼音库**
#!/usr/bin/python
# -*- coding: UTF-8 -*- 
from pypinyin import lazy_pinyin, load_phrases_dict, TONE2
print lazy_pinyin(u"诗和远方", style=TONE2)
load_phrases_dict({u'远方':[['ju4'], ['keng1']]})
print lazy_pinyin(u"诗和远方", style=TONE2)

(venv) allenwoo@~/renren$ python test.py 
[u'shi1', u'he2', u'yua3n', u'fa1ng']
[u'shi1', u'he2', 'ju4', 'keng1']
```




后面部分转自
作者：HiWoo
链接：https://www.jianshu.com/p/f1b577c5465a
來源：简书

