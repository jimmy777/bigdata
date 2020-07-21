# elasticsearch-6.3.1

```

// 注意：不能使用 root 账户来启动
> useradd es
> passwd es
> su es

// 启动
[es@node101 logs]$ bin/elasticsearch -d

// curl GET 测试
[es@node101 logs]$ curl -XGET 'http://node101:9200/_cluster/health?pretty'

// curl PUT 添加3条记录
[es@node101 es]$ curl -X PUT "node101:9200/library/book/_bulk?refresh" -H 'Content-Type: application/json' -d'
{"index":{"_id": "Leviathan Wakes"}}
{"name": "Leviathan Wakes", "author": "James S.A. Corey", "release_date": "2011-06-02", "page_count": 561}
{"index":{"_id": "Hyperion"}}
{"name": "Hyperion", "author": "Dan Simmons", "release_date": "1989-05-26", "page_count": 482}
{"index":{"_id": "Dune"}}
{"name": "Dune", "author": "Frank Herbert", "release_date": "1965-06-01", "page_count": 604}
'

// shell 启动 sql 查询
[es@node101 es]$ bin/elasticsearch-sql-cli node101:9200
sql> SELECT * FROM library WHERE release_date < '2000-01-01';

// curl POST 提交 sql 查询
[es@node101 es]$ curl -X POST "node101:9200/_xpack/sql?format=txt" -H 'Content-Type: application/json' -d'
{
    "query": "SELECT * FROM library ORDER BY page_count DESC LIMIT 5"
}
'

```
