
# bigdata

```
/etc/hosts
192.168.209.101         node101
192.168.209.102         node102
192.168.209.103         node103


安装目录
/bigdata

数据目录
/data


# cat /etc/security/limits.conf
...
* soft nofile 65536
* hard nofile 65536
* soft nproc  65536
* hard nproc  65536

```


# src
- apache-flume-1.8.0-bin.tar.gz
- hadoop-2.7.2.tar.gz
- spark-2.2.0-bin-hadoop2.7.tgz
- apache-hive-1.2.2-bin.tar.gz
- hbase-1.2.6-bin.tar.gz
- zookeeper-3.4.10.tar.gz
- apache-kylin-2.6.4-bin-hbase1x.tar.gz
- scala-2.11.8.tgz
- zookeeper-3.4.6.tar.gz

# Java

```
编辑 /etc/profile 文件，指定java路径。

```

# Hadoop

```
修改 /bigdata/hadoop/etc/hadoop 配置路径下的文件：

1. core-site.xml
2. hadoop-env.sh
3. hdfs-site.xml
4. mapred-site.xml
5. slaves
6. yarn-env.sh
7. yarn-site.xml


[root@node101 hadoop]# sbin/start-all.sh
......

hdfs-website
http://node101:50070

yarn-website
http://node101:8088


[root@node101 hadoop]# mr-jobhistory-daemon.sh start historyserver
......

jobhistory-website
http://node101:19888


```

# Spark


# Hive

```

server 192.168.209.10 install mysql-5.7.29.
---------------

[root@app01 bigdata]# ls /etc/yum.repos.d/
CentOS7-Base-163.repo  epel.repo  epel-testing.repo  mysql-community.repo  mysql-community-source.repo

[root@app01 bigdata]# rpm -qa|grep mysql
mysql-community-common-5.7.29-1.el7.x86_64
mysql-community-devel-5.7.29-1.el7.x86_64
mysql-community-libs-5.7.29-1.el7.x86_64
mysql-community-server-5.7.29-1.el7.x86_64
mysql57-community-release-el7-10.noarch
mysql-community-client-5.7.29-1.el7.x86_64
mysql-community-libs-compat-5.7.29-1.el7.x86_64

account info
---------------
root
@WSX3edc


mysqld service
---------------
# systemctl start mysqld


[root@node101 conf]# pwd
/bigdata/apache-hive-1.2.2-bin/conf


hive config files
---------------
hive-env.sh
hive-exec-log4j.properties
hive-log4j.properties
hive-site.xml


hive need mysql-connector
---------------
[root@node101 lib]# pwd
/bigdata/apache-hive-1.2.2-bin/lib
[root@node101 lib]# ls|grep mysql
mysql-connector-java-5.1.38.jar


```

# Zookeeper


# HBase


