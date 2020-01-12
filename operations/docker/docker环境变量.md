# docker中获取环境变量

### docker中的文件

##### 配置文件　(python 获取)　
API_ADDR = os.environ.get("API_ADDR","http://127.0.0.1:8080/api/v1"

cat rrd/config.py     
```
import os

API_ADDR = os.environ.get("API_ADDR","http://127.0.0.1:8080/api/v1")
API_USER = os.environ.get("API_USER","admin")
API_PASS = os.environ.get("API_PASS","password")

# portal database
# TODO: read from api instead of db
PORTAL_DB_HOST = os.environ.get("PORTAL_DB_HOST","127.0.0.1")
PORTAL_DB_PORT = int(os.environ.get("PORTAL_DB_PORT",3306))
PORTAL_DB_USER = os.environ.get("PORTAL_DB_USER","root")
PORTAL_DB_PASS = os.environ.get("PORTAL_DB_PASS","")
PORTAL_DB_NAME = os.environ.get("PORTAL_DB_NAME","falcon_portal")

# alarm database
# TODO: read from api instead of db
ALARM_DB_HOST = os.environ.get("ALARM_DB_HOST","127.0.0.1")
ALARM_DB_PORT = int(os.environ.get("ALARM_DB_PORT",3306))
ALARM_DB_USER = os.environ.get("ALARM_DB_USER","root")
ALARM_DB_PASS = os.environ.get("ALARM_DB_PASS","")
ALARM_DB_NAME = os.environ.get("ALARM_DB_NAME","alarms")
```
##### 获取配置文件中变量
cat rrd/store.py

```
import MySQLdb
from rrd import config
from rrd.utils.logger import logging

portal_db_cfg = {
        "DB_HOST": config.PORTAL_DB_HOST,
        "DB_PORT": config.PORTAL_DB_PORT,
        "DB_USER": config.PORTAL_DB_USER,
        "DB_PASS": config.PORTAL_DB_PASS,
        "DB_NAME": config.PORTAL_DB_NAME,
}

alarm_db_cfg = {
        "DB_HOST": config.ALARM_DB_HOST,
        "DB_PORT": config.ALARM_DB_PORT,
        "DB_USER": config.ALARM_DB_USER,
        "DB_PASS": config.ALARM_DB_PASS,
        "DB_NAME": config.ALARM_DB_NAME,
}

def connect_db(cfg):
    try:
        conn = MySQLdb.connect(
            host=cfg['DB_HOST'],
            port=cfg['DB_PORT'],
            user=cfg['DB_USER'],
            passwd=cfg['DB_PASS'],
            db=cfg['DB_NAME'],
            use_unicode=True,
            charset="utf8")
        return conn
```
### 用bash获取
cat config.sh
```
echo $PORTAL_DB_HOST
echo $API_ADDR
```
#输出

```
falcon.xxx.com.cn
http://falcon-api.xxx.com:8080/api/v1
```

# 在外面启动docker时设置环境变量

```
docker run --name falcon-dashboard-self -d \
    -p 8082:8081 \
    -e API_ADDR=http://falcon-api.xxx.com:8080/api/v1 \
    -e PORTAL_DB_HOST=falcon.xxx.com.cn \
    -e PORTAL_DB_PORT=3306 \
    -e PORTAL_DB_USER=falcon \
    -e PORTAL_DB_PASS=passwd \
    -e PORTAL_DB_NAME=falcon_portal \
    -e ALARM_DB_HOST=falcon.xxx.com.cn \
    -e ALARM_DB_PORT=3306 \
    -e ALARM_DB_USER=falcon \
    -e ALARM_DB_PASS=passwd \
    -e ALARM_DB_NAME=alarms \
    -w /open-falcon/dashboard \
    falcon-dashboard:local \
    './control startfg'

```

