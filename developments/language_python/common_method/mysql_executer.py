#!/home/tops/bin/python
# -*- coding:utf-8 -*-
import mysql.connector
from command_executor import ExecCmdException, exec_cmd
from logging_helper import get_logger
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
    def execute_read_sql(self, sql, dictionary=None):
        conn = self.build_conn()
        try:
            return self.execute_read_sql_with_conn(conn, sql, dictionary)
        finally:
            conn.close()
    @classmethod
    def execute_read_sql_with_conn(cls, conn, sql, dictionary=None):
        cursor = conn.cursor(dictionary=dictionary)
        cursor.execute(sql)
        return cursor.fetchall()
    def execute_write_sql(self, sql):
        conn = self.build_conn()
        try:
            self.execute_write_sql_with_conn(conn, sql)
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
        return mysql.connector.connect(host=self.host,
                                       port=int(self.port),
                                       user=self.user,
                                       passwd=self.pwd,
                                       db=self.database)