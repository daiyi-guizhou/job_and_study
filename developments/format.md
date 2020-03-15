<!-- TOC -->

- [格式化代码](#格式化代码)

<!-- /TOC -->

# 格式化代码
requirements.txt
```
yapf==0.28.0
isort==4.3.21
```
MakeFile
```
.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: fmt
fmt:
	yapf --exclude services/sls-backend-server/init_sls_cluster/conf.tmpl -p -i -r .
	isort --skip services/sls-backend-server/init_sls_cluster/conf.tmpl -rc .
```
```
yapf -p -i -r .
isort -rc .    

(如何忽略掉 某些 文件 或 目录.)
yapf --exclude services/conf.tmpl -p -i -r .
isort --skip services/conf.tmpl -rc .
```

(如果需要忽略多个文件)
yamf
Excluding files from formatting (.yapfignore)
In addition to exclude patterns provided on commandline, YAPF looks for additional patterns specified in a file named .yapfignore located in the working directory from which YAPF is invoked.

举例，添加一个 `.yapfignore`文件，内容如下，他就能忽略这两个文件了。
```
db_pre_handler/conf.tmpl
db_post_handler/conf.tmpl
```
`.yapfignore`也支持正则，  下面这个和上面等效。
```
*/conf.tmpl
```


_____________
isort 
 -s SKIP, --skip SKIP  Files that sort imports should skip over. If you want
                        to skip multiple files you should specify twice:
                        --skip file1 --skip file2.
			
			
sort 同样也可以用配置文件
Configuring isort
If you find the default isort settings do not work well for your project, isort provides several ways to adjust the behavior.

To configure isort for a single user create a ~/.isort.cfg or $XDG_CONFIG_HOME/isort.cfg file:
```
[settings]
line_length=120
force_to_top=file1.py,file2.py
skip=file3.py,file4.py
known_future_library=future,pies
known_standard_library=std,std2
known_third_party=randomthirdparty
known_first_party=mylib1,mylib2
indent='    '
multi_line_output=3
length_sort=1
forced_separate=django.contrib,django.utils
default_section=FIRSTPARTY
no_lines_before=LOCALFOLDER
```

Additionally, you can specify project level configuration simply by placing a .isort.cfg file at the root of your project. isort will look up to 25 directories up, from the file it is ran against, to find a project specific configuration.

在你的项目中， 需要执行 sort 的当前目录， 粗暴的来一个 .isort.cfg 文件。
```
[settings]
skip=src/common/tianji/tianji_clt.py,\
        src/scale_down_sls_cluster_ag/sls_deploy_common.py,\
        src/scale_down_sls_cluster_ag/sls_op_common.py,\
        src/scale_down_sls_cluster_ag/sls_worker_scaling_016.py,\
        src/scale_down_sls_cluster_ag/sls_worker_shutdown_machine.py,\
        src/scale_down_sls_cluster
```
***
***
class Name(object)  与 class Name()   有无 object 的差别
	https://my.oschina.net/zhengtong0898/blog/636468
	实际上在python 3 中已经默认就帮你加载了object了（即便你没有写上object）。
****
****
switchyomega  + chrome 插件代理.    ---- ip 代理
***
***
python
	`argparse  模块， 用来对你的函数 执行的参数 做封装的。 `
```
	try:
    import json
except:
```
```
    import simplejson as json
	unittest自动化测试的  模块。
		import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
	sys.path.append()  添加路径， 方便导入其它路径的模块。
		sys.path.append(FILE_PATH + "/data_sdk_v4")
```
```
	 hashlib.md5()
		import hashlib         #导入hashlib模块

md = hashlib.md5()     #获取一个md5加密算法对象
md.update('how to use md5 in hashlib?'.encode('utf-8'))                   #制定需要加密的字符串
print(md.hexdigest())  #获取加密后的16进制字符串
```
