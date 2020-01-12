
unittest.Testcase : https://docs.python.org/zh-cn/3/library/unittest.html
[测试样例， 文档](https://docs.python.org/zh-cn/3/library/unittest.html)
## 函数名需要 “test” 开头，才能被应用
`Ran 0 tests in 0.000s` 这个测试样例 没有 被应用
```python
import unittest

class test_myClass(unittest.TestCase):
    # def testgetNameEmpty(self): ## 函数名需要 “test” 开头，才能被应用
    def getNameEmpty(self):
        self.assertEqual("love","peace")
        # self.assertEqual("love","love")

if __name__ == "__main__":
    unittest.main()

daiyi:daiyi$ python ./daiyi-b.py 

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```
**函数名需要 “test” 开头**
`Ran 1 tests in 0.000s` 有一个测试样例被应用
```python
import unittest

class test_myClass(unittest.TestCase):
    def testgetNameEmpty(self): ## 函数名需要 “test” 开头，才能被应用
    # def getNameEmpty(self):
        self.assertEqual("love","peace")
        # self.assertEqual("love","love")

if __name__ == "__main__":
    unittest.main()

daiyi:daiyi$ python ./daiyi-b.py 

F
======================================================================
FAIL: testgetNameEmpty (__main__.test_myClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./daiyi-b.py", line 9, in testgetNameEmpty
    self.assertEqual("love","peace")
AssertionError: 'love' != 'peace'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

## python2 assertRaises 需要封装下
[参考文章](https://ongspxm.github.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/)
```
import unittest

def func():
    raise Exception('lets see if this works')

class ExampleTest(unittest.TestCase):
    def test_error(self):
        # self.assertRaises(Exception,func())  ## 这个没有封装， assertRaise 不能抓取到这个 异常。
        # self.assertRaises(Exception,lambda:func())  ## lambda 封装后，能抓取到
        # with self.assertRaises(Exception): ## 封装后， 能抓取到
        #     func()

if __name__=='__main__':
    unittest.main()
```

