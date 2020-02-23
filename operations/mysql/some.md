<!-- TOC -->

- [escapestring 过滤， 防止sql注入](#escapestring-过滤-防止sql注入)
- [日常操作](#日常操作)
- [sql 单引号](#sql-单引号)
- [清空表](#清空表)
- [mysql 容器](#mysql-容器)
- [python-mysql-connector](#python-mysql-connector)
- [dict返回](#dict返回)

<!-- /TOC -->

mysql\
	select  column_name, column_comment from information_schema.columns where table_name='project';
select deleted_flag from project  where project_name='sls-smoke-test-e09242b2e465bfc11c3f9f0e6214d2b4';

## escape_string 过滤， 防止sql注入
```
def escape_sql_str(self, sql_str):
    try:
        import MySQLdb
        return MySQLdb.escape_string(sql_str)
    except ImportError:
        # import mysql.connector，you do not need to escape the data yourself, it does it automatically for you
        return sql_str
		 s = simplejson.loads(old)
    new_sched = {
        'interval': '%sm' % s['interval'],
        'type': 'FixedRate',
    }
    return MySQLdb.escape_string(simplejson.dumps(new_sched))
```
		这是用来过滤的
		https://stackoverflow.com/questions/7540803/escaping-strings-with-python-mysql-connector

## 日常操作
		添加 key   https://blog.csdn.net/arkblue/article/details/9070797
		 https://blog.csdn.net/zm_bingxindan/article/details/23893391
		 修改表名，列名，类型
			https://blog.csdn.net/mouday/article/details/89447263

## sql 单引号
当有 双引号 容易引发 插入格式错误 时， 用 单引号。 
```	
INSERT INTO trigger_conf ( project_id, trigger_name, display_name, saved_search, search_detail, trigger_detail, operator_detail, action_detail, deleted_flag, update_time) VALUES (303,"savedsearch-1577963577214-14726"," ","savedsearch-1577963577214-14726", '{"from":"-120s","rolearn":"acs:ram::1857938651531441:role/aliyunlogreadrole","to":"now"}','{"count":2,"interval":5}','{"key":"c","opt":">","value":20}','{"detail":{"message":"110.249.208.* 网段爬虫卷土重来","webhook":"https://oapi.dingtalk.com/robot/send?access_token=70512313c87bf292a4f07f5212577262247306438a505c856f001dc7f984c102"},"type":"dingtalk"}',0 ,"2018-09-06 10:39:32");
```
三引号 造成 dict 外面 也有 单引号，这个  simplejson.load() 就出错
```
			[{u'update_time': datetime.datetime(2018, 9, 6, 10, 39, 32), u'operator_detail': u'\'{"key":"c","opt":">","value":"20"}\'', u'display_name': u' ', u'trigger_detail': u'\'{"count":"2","interval":"5"}\'',u'project_name':u'sls-smoke-test-e09242b2e465bfc11c3f9f0e6214d2b41577298610', u'create_time': datetime.datetime(2020, 1, 2, 19, 9, 10), u'search_detail': u'\'{"from":"-120s","rolearn":"acs:ram::1857938651531441:role/aliyunlogreadrole","to":"now"}\'', u'action_detail': u'\'{"detail":{"message":"110.249.208.* \u7f51\u6bb5\u722c\u866b\u5377\u571f\u91cd\u6765","webhook":"https://oapi.dingtalk.com/robot/send?access_token=70512313c87bf292a4f07f5212577262247306438a505c856f001dc7f984c102"},"type":"dingtalk"}\'', u'trigger_name': u'savedsearch-1577963577214-14726', u'project_id': 303, u'query_detail': u'\'{"displayName":"hdhahsa","topic":"","logstore":"test-o","searchQuery":"* | select status, COUNT(*) as c GROUP BY status","tokenQuery":"* | select status, COUNT(*) as c GROUP BY status","tokens":[],"savedsearchName":"savedsearch-1577963577214-14726"}\''}] u'\'{"count":"2","interval":"5"}\''
```

## 清空表
		delete from 表名;
truncate table 表名;
不带where参数的delete语句可以删除mysql表中所有内容，使用truncate table也可以清空mysql表中所有内容。效率上truncate比delete快，但truncate删除后不记录mysql日志，不可以恢复数据。
delete的效果有点像将mysql表中所有记录一条一条删除到删完，而truncate相当于保留mysql表的结构，重新创建了这个表，所有的状态都相当于新表

## mysql 容器
通常使用
```
root@vm010025018250 /cloud/app/sls-backend-server/ToolService#/init_db/current]
#cat init_scmc_mysql.config
{
    "db_host": "slsscmc.mysql.minirds.intra.env25.shuguang.com",
    "db_port": "3017",
    "db_user": "slsscmc",
    "db_pwd": "yoqiviksNAuesp01",
    "db_database": "slsscmc"
}
[root@vm010025018250 /cloud/app/sls-backend-server/ToolService#/init_db/current]
#mysql -P 3017 -h slsscmc.mysql.minirds.intra.env25.shuguang.com -u slsscmc slsscmc -pyoqiviksNAuesp01
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5514557
Server version: 5.6.46-log Source distribution

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
		 容器
			## bash create db
docker run -d --rm -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 mysql:5.7
docker run -i --rm mysql mysql -h 30.43.72.6 -P 3306 -u root -p123456 -e 'show databases;'
mysql -h 30.43.72.6 -P 3306 -u root -p123456 -e 'create database if not exists test_db;'


mysql -u root -h 30.43.72.6 test_db -p123456
		 https://segmentfault.com/a/1190000007025543
	 sql   update-on-duplicate-key-update
		https://www.mysqltutorial.org/mysql-insert-or-update-on-duplicate-key-update/
		 SELECT t.project_id as project_id,
t.trigger_name as trigger_name,
t.display_name as display_name,
t.search_detail as search_detail,
t.trigger_detail as trigger_detail,
t.operator_detail as operator_detail,
t.action_detail as action_detail,
t.update_time as update_time,
s.search_detail as query_detail,
s.ctime as create_time,
p.project_name as project_name
 FROM trigger_conf AS t, savedsearch AS s, project AS p 
  WHERE t.deleted_flag=0 AND s.deleted_flag=0 AND t.saved_search=s.search_name AND p.deleted_flag=0
  AND t.project_id=s.project_id and t.project_id=p.project_id;
```

## python-mysql-connector
		https://www.runoob.com/python3/python-mysql-connector.html
		
```
#!/home/tops/bin/python
# -*- coding:utf-8 -*-

from ..command_executor import ExecCmdException, exec_cmd
from ..logging_helper import get_logger


class MySQLExecutor(object):
    DOCKER_PREFIX = "docker run -i --rm mysql"

    CREATE_DATABASE_TMPL = "mysql -h {host} -P {port} -u {user} -p{pwd} -e " \
                           "'create database if not exists {database};'"

    CREATE_DATABASE_USING_DOCKER_TMPL = "%s %s" % (DOCKER_PREFIX,
                                                   CREATE_DATABASE_TMPL)

    EXECUTE_SQL_FILE_TMPL = "mysql -h {host} -P {port} -u {user} -p{pwd} {database} < {sql_file}"

    EXECUTE_SQL_FILE_USING_DOCKER_TMPL = "%s %s" % (DOCKER_PREFIX,
                                                    EXECUTE_SQL_FILE_TMPL)

    def __init__(self,
                 host,
                 port,
                 user,
                 pwd,
                 database,
                 using_docker_flag=False):
        self.logger = get_logger()
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.database = database
        self.using_docker_flag = using_docker_flag

    def create_database_if_not_exists(self):
        if not self.using_docker_flag:
            cmd = self.CREATE_DATABASE_TMPL.format(
                host=self.host,
                port=self.port,
                user=self.user,
                pwd=self.pwd,
                database=self.database,
            )
        else:
            cmd = self.CREATE_DATABASE_USING_DOCKER_TMPL.format(
                host=self.host,
                port=self.port,
                user=self.user,
                pwd=self.pwd,
                database=self.database,
            )
        exec_cmd(cmd)

    def execute_sql_file(self, sql_file):
        if not self.using_docker_flag:
            cmd = self.EXECUTE_SQL_FILE_TMPL.format(host=self.host,
                                                    port=self.port,
                                                    user=self.user,
                                                    pwd=self.pwd,
                                                    database=self.database,
                                                    sql_file=sql_file)
        else:
            cmd = self.EXECUTE_SQL_FILE_USING_DOCKER_TMPL.format(
                host=self.host,
                port=self.port,
                user=self.user,
                pwd=self.pwd,
                database=self.database,
                sql_file=sql_file)
        try:
            exec_cmd(cmd)
        except ExecCmdException as e:
            # Table already exists
            if "ERROR 1050" in e.stderr:
                self.logger.warning(e.stderr)
            else:
                raise e

    def execute_read_sql(self, sql):
        conn = self.build_conn()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conn.close()
    
    def escape_sql_str(self, sql_str):
        try:
            import MySQLdb
            return MySQLdb.escape_string(sql_str)
        except ImportError:
            # import mysql.connectorï¼Œyou do not need to escape the data yourself, it does it automatically for you
            return sql_str

    def execute_read_sql_dict(self, sql):
        try:
            import MySQLdb
            conn = MySQLdb.connect(host=self.host,
                                   port=int(self.port),
                                   user=self.user,
                                   passwd=self.pwd,
                                   db=self.database)
            try:
                cursor = conn.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute(sql)
                return cursor.fetchall()
            finally:
                conn.close()
        except ImportError:
            import mysql.connector
            conn = mysql.connector.connect(host=self.host,
                                           port=int(self.port),
                                           user=self.user,
                                           passwd=self.pwd,
                                           db=self.database)
            try:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(sql)
                return cursor.fetchall()
            finally:
                conn.close()

    @classmethod
    def execute_read_sql_with_conn(cls, conn, sql):
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def execute_write_sql(self, sql):
        conn = self.build_conn()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    @classmethod
    def execute_write_sql_with_conn(cls, conn, sql):
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def build_conn(self):
        try:
            import MySQLdb
            return MySQLdb.connect(host=self.host,
                                   port=int(self.port),
                                   user=self.user,
                                   passwd=self.pwd,
                                   db=self.database)
        except ImportError:
            import mysql.connector
            return mysql.connector.connect(host=self.host,
                                           port=int(self.port),
                                           user=self.user,
                                           passwd=self.pwd,
                                           db=self.database)
		 for mac
	 MySQLDB 
		for linux 
		 https://www.runoob.com/python/python-mysql.html
		import MySQLdb
 
mysql_conn = MySQLdb.connect(host=mysql_host,
                                 user=mysql_user,
                                 passwd=mysql_passwd,
                                 db=mysql_db,
                                 port=mysql_port,
                                 charset='utf8') # 打开数据库连接
    mysql_cursor = mysql_conn.cursor(MySQLdb.cursors.DictCursor) 
mysql_cursor.execute(sql)# 使用execute方法执行SQL语句
results = mysql_cursor.fetchall()# 使用 fetchone() 方法获all数据 （execute 执行后的结果。）
mysql_conn.commit()# 提交到数据库执行
mysql_cursor.close()
mysql_conn.close() # 关闭数据库连接
```

## dict_返回
		http://cn.voidcc.com/question/p-hkaldovs-bdu.html
		 https://stackoverflow.com/questions/22769873/python-mysql-connector-dictcursor