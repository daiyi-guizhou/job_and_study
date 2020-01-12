# 逗号转义
```
#!/usr/bin/python
import os

JETTY_SCRIPT_PATH=/etc/jetty.conf
JETTY_ALIAS="/etc/kk/yy/dd/mm"
JETTY_ALIAS2 = JETTY_ALIAS.replace("/", "\/")
os.system("sudo sed -i '/jetty\ start/ s/su/nohup\ su/g' %s " %
JETTY_SCRIPT_PATH)
os.system("""sudo  sed -i "/su\ -\ www\ -c/ s/jetty\ start'/%s\ start'\ >\ myout.file\ 2>\&1\ \&/g" %s """ % (JETTY_ALIAS2,JETTY_SCRIPT_PATH))
 ```
 `'` 单引号其实无所谓，外面用`"` 双引号就行。当你还有其它时。第三层外面用`"""` 三引号。
 这里有 后台执行的命令 `nohup cmd  &"` , 接收它的输出用 ` > myout.file 2>&1`.

# 转行 和 tab
`\n` 转行
`\t` tab； 但是 在sed命令符后时为 `\\t`
如`sed -i '1 a\\thello world ' ./test.sh`
举例如下
```
[root@vm010099101015 /cloud/app/sls-common]
#cat ./overwrite.sh

#!/bin/sh

[root@vm010099101015 /cloud/app/sls-common]
#sudo sed -i '2 ai\n\ti\n\t\ti\n\t\t\ti' ./overwrite.sh

[root@vm010099101015 /cloud/app/sls-common]
#cat ./overwrite.sh

#!/bin/sh
i
        i
                i
                        i

### 这里的 tab 是 ‘\\t’
[root@vm010099101015 /cloud/app/sls-common]
#sudo sed -i '2 a\\t\t\ti\n\t\ti\n\ti\ni' ./overwrite.sh

[root@vm010099101015 /cloud/app/sls-common]
#cat ./overwrite.sh

#!/bin/sh
                        i
                i
        i
i
i
        i
                i
                        i

```
