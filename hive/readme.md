
# 4 Hive 编程

## 4.1 环境准备与Hive初识

> Hive建立在Hadoop之上的数据仓库，它提供了一些工具，可以用来查询和分析数据。Hive提供了执行SQL的接口，用于操作存储在HDFS中的数据。

### 4.1.1 背景介绍

> HQL语言。联机分析处理（OLAP）是一种数据的呈现和观察方式，其从多个维度去分析和理解数据。

- Hive将结构化的数据文件映射成为一张数据库表，提供SQL查询，转化为MR任务来执行。

### 4.1.2 基础环境准备

- hive
- mysql 存储Hive元数据或统计结果

### 4.1.3 Hive结构初识

- 元数据 MetaStore
- 驱动Driver（包含编译器Compiler、优化器Optimizer、执行器Executor）
- 用户接口（包含客户端client、UI、ThriftServer）

> Thrift Server支持多语言，如C++、Java、Python等。

> select * from table; 不会产生MR任务，带条件和聚合查询会启动MR任务。

### 4.1.4 Hive与关系数据库RDMS

。。。

## 4.2 安装与配置Hive

### 4.2.1 Hive集群基础架构

- 3个Hive节点，2个代理HAProxy+MySQL。

### 4.2.2 利用HAProxy实现Hive Server负载均衡

- HAProxy主备部署，实现故障转移（Failover）

```
# yum install gcc* openssl-devel pcre-devel

# make 。。。

# make install

# haproxy -vv

# vim config.cfg
......

# haproxy -f config.cfg

```

### 4.2.3 安装分布式Hive集群

> Hive使用HADOOP_HOME环境变量，指定Hadoop的所有依赖JAR包和配置文件。设置HIVE_HOME环境变量。

> Hive默认没有MySQL驱动包，所以要自己下载$HIVE_HOME/lib目录下面。

> hive脚本，无须登录账户和密码；另外beeline脚本，需要使用登录账户和密码。

```
初始化
# schemtatool -initSchema -dbType mysql

测试
# hive -e "show tables;"

启动ThriftServer，提供MetaStore服务。
# hive --service metastore &
或者
# hive --service hiveserver2 &

```

## 4.3 可编程方式

- Hive Shell方式。适合数据加载、数据验证、SQL脚本测试等场景；
- Hive Java API方式。适合数据导出、任务定时调度、数据可视化等场景。

### 4.3.1 数据类型

1. 值类型。tinyint(1)/smallint(2)/int(4)/bigint(8)/float(4)/double(8)
2. 日期类型。timestamp/date(0000-00-00)
3. 字符类型。string('XX',"XX")/varchar可变长度/char固定长度
4. 其他类型。boolean(TRUE|FALSE)/binary字节数组
5. 复杂类型。array(['A','B'])/map{"name":"hive"}/struct({"id"：1001，"name":"hive"})

### 4.3.2 存储格式

| 格式 | 存储方式 | 压缩比例 |
|--- | --- | --- |
| textfile | 按行存储。默认格式 | 原始大小 |
| rcfile | 行列存储相结合|10% |
| parquet | 按列存储。Impala默认格式 | 60% |
| orcfile | rcfile升级版 | 75% |

```
# 创建 orcfile 格式表
hive> create table ip_login(`stm` string comment 'timestamp',`uid` string comment 'user id',`ip` string comment 'login ip', `plat` string comment 'platform')  partitioned by (`tm` int comment 'date yyyyMMdd 20171101') clustered by (`uid`) sorted by (`uid`) into 2 buckets stored as orc;


# 创建 textfile 格式表

hive-site.xml
  <property>
    <name>hive.aux.jars.path</name>
    <value>file:///bigdata/hive/hcatalog/share/hcatalog/hive-hcatalog-core-1.2.2.jar</value>
    <description>The location of the plugin jars that contain implementations of user defined functions and serdes.</description>
  </property>

/etc/profile
export HIVE_AUX_JARS_PATH=$HCAT_HOME/share/hcatalog

hive> create table ip_login_text(`stm` string comment 'timestamp',`uid` string comment 'user id',`ip` string comment 'login ip', `plat` string comment 'platform')  row format serde "org.apache.hive.hcatalog.data.JsonSerDe" stored as textfile;

```

### 4.3.3 基础命令

```
1. 数据库操作
数据库仅表示一个目录或者命名空间（NameSpace），避免表明冲突。默认库名为DEFAULT。

hive> create database if not exists game;

HDFS 创建目录 /user/hive/warehouse/game.db

hive> drop database if exists game;

HDFS 中  /user/hive/warehouse/game.db 目录被删除！

注意：删除库是restrict，不允许用户删除一个含有表的数据库！要么先删除全部表，要么加上 cascade 强制删除。

2. 表操作

hive> use game;

# 创建表，灵活指定表数据存储位置、存储格式等。
hive> create table ip_login_text(`stm` string comment 'timestamp',`uid` string comment 'user id',`ip` string comment 'login ip', `plat` string comment 'platform')  row format serde "org.apache.hive.hcatalog.data.JsonSerDe" stored as textfile;

# 查看表结构
hive> desc ip_login_text;

# 清空表数据
hive> truncate table ip_login_text;

# 删除表
hive> drop table if exists ip_login_text;

3. 分区操作

# 按照业务逻辑进行分区存放。
hive> create table ip_login(`stm` string comment 'timestamp',`uid` string comment 'user id',`ip` string comment 'login ip', `plat` string comment 'platform')  partitioned by (`tm` int comment 'date yyyyMMdd 20171101') clustered by (`uid`) sorted by (`uid`) into 2 buckets stored as orc;

```

### 4.3.4 Java 编程语言操作数据仓库（Hive）

> Hive 的 ThriftServer 提供了 JDBC 和 ODBC 的编程接口服务。编写 Java 代码来操作 Hive。

## 4.4 运维和监控

> HQL 转为 MR，所以监控 Yarn。http://node101:8088/cluster

### 4.4.1 基础命令

```
1. application
# 不过滤，显示所有application
[root@node101 conf]# yarn application -list

# 按状态过滤
[root@node101 conf]# yarn application --list --appStates RUNNING

# 停止某个任务
[root@node101 conf]# yarn application --kill [application_xxx]

# 获取某个任务的状态
[root@node101 conf]# yarn application --status [application_xxx]

2. 日志

usage: yarn logs -applicationId <application ID> [OPTIONS]

3. 队列
# 调度策略，yarn 中会将资源按照各个用户队列进行分配。

[root@node101 conf]# yarn queue -status
20/02/05 16:38:38 INFO client.RMProxy: Connecting to ResourceManager at node101/192.168.209.101:8032
Missing argument for options
usage: queue
 -help                  Displays help for all commands.
 -status <Queue Name>   List queue information about given queue.

```

### 4.4.2 监控工具 Hive Cube

- [官网](https://hc.smartloli.org/)


NOTE
---
- Hive 的表类型分为内部表和外部表。在删除内部表时，Hive 元数据信息和存储在Hadoop分布式文件系统HDFS中的数据会一并删除；在删除外部表时，仅仅只是删除Hive元数据信息，而存储在HDFS中的数据不会被删除。

- 服务端metastore 启动方式：

```
 # hive --service metastore -p 9083 &
  或者
  在hive-site.xml中配置hive.metastore.uris，指定端口，然后直接 hive --service metastore

 总结：为什么集群要启用metastore，因为启用后，直接bin/hive启动进程，只会有hive交互式客户端一个服务，不会再有metastore同时存在在该进程中，资源占用率下降，查询速度更快。
```

- metastore服务实际上就是一种thrift服务，通过它我们可以获取到hive原数据，并且通过thrift获取原数据的方式，屏蔽了数据库访问需要驱动，url，用户名，密码等等细节。
- hive中对metastore的配置包含3部分，metastore database,metastore server,metastore client。

> HiveServer2 (HS2) is a server interface that enables remote clients to execute queries against Hive and retrieve the results (a more detailed intro here).
The current implementation, based on Thrift RPC, is an improved version of HiveServer and supports multi-client concurrency and authentication.HiveServer2（HS2）是一个服务端接口，使远程客户端可以执行对Hive的查询并返回结果。目前基于Thrift RPC的实现是HiveServer的改进版本，并支持多客户端并发和身份验证


- hiveServer2的启动方式有2种：

```
$HIVE_HOME/bin/hiveserver2 或者
$HIVE_HOME/bin/hive --service hiveserver2

```

REF
---

- [hive引入jar包--HIVE.AUX.JARS.PATH和hive.aux.jars.path](https://www.cnblogs.com/Dhouse/p/7986659.html)
