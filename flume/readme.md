
## 3.2 Flume 日志收集 工具

> Flume 采集文件到 HDFS中。目标是文件，而不是数据库。

### 3.2.1 背景概述

> Flume 是一个分布式、高可用、高可靠的系统，采集存储到 HDFS 或者 Kafka 中。支持故障转移（Failover）和负载均衡（LoadBalance）。

- 三层架构：
    - Agent 层，负责采集，多个 Agent 同时传输到 Collector 中；
    - Collector 层，汇总多个 Agent 上报的数据，并加载到 Storage 中。多个 Collector 实现负载均衡；
    - Storage 层，多个存储类型，如：File、HDFS、HBase、Kafka等。

- Flume 核心组件：
    - Source，收集器，并传数据给 Channel；
    - Channel，管道，临时存储 Source 上报的数据；
    - Sink，槽，从 Channel 中读取数据（若读取成功将删除 Channel 中的临时！），并转发给下游如：HDFS、HBase、Kafka等。

### 3.2.2 安装与基本使用

>  apache-flume-1.8.0-bin.tar.gz

1. 单点部署

[root@node101 conf]# pwd
/bigdata/flume/conf
[root@node101 conf]# bin/flume-ng agent -n agent1 -c conf -f conf/flume-hdfs.conf -Dflume.root.logger=DEBUG
