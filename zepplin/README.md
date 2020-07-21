1. Clone the Apache Zeppelin repository

```
git clone https://github.com/apache/zeppelin.git
```

2. Build source

```
mvn clean package -DskipTests [Options]

# update all pom.xml to use scala 2.11
./dev/change_scala_version.sh 2.11
# build zeppelin with all interpreters and include latest version of Apache spark support for local mode.
mvn clean package -DskipTests -Pspark-2.0 -Phadoop-2.4 -Pr -Pscala-2.11

```

3. Done

./bin/zeppelin-daemon.sh start


export MAVEN_OPTS="-Xmx2g -XX:ReservedCodeCacheSize=512m"
