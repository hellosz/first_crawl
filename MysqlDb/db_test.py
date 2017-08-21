#-*-encoding=utf-8-*-

import MySQLdb

#链接数据库
conn = MySQLdb.connect('localhost', 'root', '', 'test', 'utf8')

#查询数据
cursor = conn.cursor()
sql = "select * from student"
#输出结果
cursor.execute(sql)

for student in cursor.fetchall():
    print student

#关闭链接
cursor.close()
conn.close()