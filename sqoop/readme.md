
## 3.1 Sqoop 数据传输工具

### 3.1.1 背景概述

> 关系数据库数据导入到 HDFS 中。使用 MR，并行操作。

```
MySQL -（Load）->  Sqoop  -（Import）->  HDFS
HDFS  -（Load）-> Sqoop  -（Export）->  MySQL

```

### 3.1.2 安装及基本使用

> Sqoop 1 和 Sqoop 2 两个版本，二者截然不同、互不兼容！

sqoop-1.4.7

```
# cp mysql-connector-java-5.1.38.jar $SQOOP_HOME/lib

```

### 3.1.3 MySQL 与 HDFS

```
mysql> desc student;
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| s_id      | int(11)      | NO   | PRI | NULL    | auto_increment |
| sno       | int(11)      | YES  | UNI | NULL    |                |
| sname     | varchar(50)  | YES  |     | NULL    |                |
| sage      | int(11)      | YES  |     | NULL    |                |
| ssex      | varchar(8)   | YES  |     | NULL    |                |
| father_id | int(11)      | YES  |     | NULL    |                |
| mather_id | int(11)      | YES  |     | NULL    |                |
| note      | varchar(500) | YES  | MUL | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)


## import 命令

# sqoop import --connect jdbc:mysql://192.168.209.10:3306/stu?useSSL=false --username root -P --table student --fields-terminated-by ',' --null-string '**' -m 1 --append --target-dir '/data/sqoop/student.db'

注意：
-m 1，表示 map 任务数为 1；
--null-string '**'，表示数据库中 NULL 用 “**” 来替换；

# 查看结果
[root@node101 code]# hdfs dfs -cat /data/sqoop/student.db/*



mysql> desc teacher;
+-----------+------------------+------+-----+---------+----------------+
| Field     | Type             | Null | Key | Default | Extra          |
+-----------+------------------+------+-----+---------+----------------+
| tid       | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name      | varchar(20)      | NO   |     | NULL    |                |
| classtype | varchar(20)      | NO   |     | NULL    |                |
+-----------+------------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)



[root@node101 code]# sqoop import --connect jdbc:mysql://192.168.209.10:3306/stu?useSSL=false --username root -P --table teacher --fields-terminated-by ',' --null-string '**' -m 2 --append --target-dir '/data/sqoop/teacher.db'

## export 命令

# sqoop export -D sqoop.export.records.per.statement=100 --connect jdbc:mysql://192.168.209.10:3306/stu?useSSL=false --username root -P --table teacher_orc --fields-terminated-by ',' --export-dir '/data/sqoop/teacher.db' --batch --update-key tid --update-mode allowinsert;

注意：
-D sqoop.export.records.per.statement=100，表示批处理，每100条数据提交一次；
--batch，表示使用批量导出；
--update-key tid，表示数据库中表的主键；
--update-mode，表示如何更新数据库表中的数据。

```
