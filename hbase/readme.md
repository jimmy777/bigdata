
## 3.3 HBase 分布式数据库

> 大规模数据集，考虑数据存储的高可用性、高吞吐量、半结构化的数据、高效的查询性能等因素，一般的数据库很难满足需求。

### 3.3.1 背景概述

> HBase 拥有高可用性、高性能、面向列存储、可扩展等特性。

- 应用场景
    - 数据量大，并且访问需要满足随机、快速响应的需求；
    - 需要满足动态扩容的需求；
    - 不需要满足关系数据库的特性，如事务、连接、交叉表。
    - 写数据时，需要拥有高吐的能力。

### 3.3.2 存储架构介绍

> 节点都可以横向扩展。它依赖 Zookeeper 和 HDFS 服务。

- HMaster 节点
- HRegionServer 节点

### 3.3.3 安装与基本使用

- zookeeper-3.4.6
- hbase-1.2.6

```
# bin/start-hbase.sh start
# jps
7037 QuorumPeerMain
7284 HMaster
7421 HRegionServer

```

> http://node101:16010/master-status

注意：HA 高可用配置

### 3.3.4 HBase 操作

> HBase Shell 在日常工作中多用于排查问题，校验数据格式或数据记录完成与否；HBase Java API 多用于在实际业务开发中，实现业务需求功能。

1、HBase Shell

```
# 进入 shell
[root@node101 conf]# hbase shell

# 创建业务表 create
hbase(main):001:0> create 'game_x_tmp', '_x'
0 row(s) in 1.5810 seconds

=> Hbase::Table - game_x_tmp

# 添加数据 put
hbase(main):002:0> put 'game_x_tmp','rowkey1','_x','v1'
0 row(s) in 0.1640 seconds

# 查全表 scan
hbase(main):003:0> scan 'game_x_tmp'
ROW                                                         COLUMN+CELL
 rowkey1                                                    column=_x:, timestamp=1581060075702, value=v1
1 row(s) in 0.0490 seconds

# 根据 rowkey 进行查询 get
hbase(main):004:0> get 'game_x_tmp','rowkey1'
COLUMN                                                      CELL
 _x:                                                        timestamp=1581060075702, value=v1
1 row(s) in 0.0280 seconds

# 禁止业务表 disable
hbase(main):005:0> disable 'game_x_tmp'
0 row(s) in 2.3410 seconds

# 删除业务表 drop
hbase(main):006:0> drop 'game_x_tmp'
0 row(s) in 1.2850 seconds

```

2. HBase Java API
略！
