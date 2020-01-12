ports：
	8433	
	8080
	8081

dirs:
	/home/work/mysql-data	
/tmp




# Init MySQL
docker run -itd \
    --name falcon-mysql \
    -v /home/work/mysql-data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=xxxxx \
    -p 3306:3306 \
    mysql:5.7

# Init mysql table
cd /tmp && \
git clone https://github.com/open-falcon/falcon-plus --depth=1 && \
cd /tmp/falcon-plus/ && \
for x in `ls ./scripts/mysql/db_schema/*.sql`; do
    echo init mysql table $x ...;
    docker exec -i falcon-mysql mysql -ufalcon -pBapeXazw9.Lego -h falcon.cnwltt2bpgx5.rds.cn-north-1.amazonaws.com.cn < $x;
done

rm -rf /tmp/falcon-plus/

# Pull images from hub.docker.com/openfalcon
docker pull openfalcon/falcon-plus:v0.2.1

# Run falcon-plus container
docker run -itd --name falcon-plus \
    -p 8433:8433 \
    -p 8080:8080 \
    -e MYSQL_PORT=falcon:BapeXazw9.Lego@tcp\(falcon.cnwltt2bpgx5.rds.cn-north-1.amazonaws.com.cn:3306\) \
    -e REDIS_PORT=falcon-prod.1gzkge.0001.cnn1.cache.amazonaws.com.cn:6379  \
    -v /home/work/open-falcon/data:/open-falcon/data \
    -v /home/work/open-falcon/logs:/open-falcon/logs \
    openfalcon/falcon-plus:v0.2.1

# Start falcon backend modules, such as graph,api,etc.
docker exec falcon-plus sh ctrl.sh start \
    graph hbs judge transfer nodata aggregator agent gateway api alarm

# Start falcon-dashboard in container
docker run -itd --name falcon-dashboard \
    -p 8081:8081 \
    -e API_ADDR=http://xx.0.0.yy:8080/api/v1 \
    -e PORTAL_DB_HOST=falcon.cnwltt2bpgx5.rds.cn-north-1.amazonaws.com.cn \
    -e PORTAL_DB_PORT=3306 \
    -e PORTAL_DB_USER=falcon \
    -e PORTAL_DB_PASS=BapeXazw9.Lego \
    -e PORTAL_DB_NAME=falcon_portal \
    -e ALARM_DB_HOST=falcon.cnwltt2bpgx5.rds.cn-north-1.amazonaws.com.cn \
    -e ALARM_DB_PORT=3306 \
    -e ALARM_DB_USER=falcon \
    -e ALARM_DB_PASS=BapeXazw9.Lego \
    -e ALARM_DB_NAME=alarms \
    -w /open-falcon/dashboard openfalcon/falcon-dashboard:v0.2.1  \
    './control startfg'

Kube Confg



AWS MySQL
	Host: falcon.cnwltt2bpgx5.rds.cn-north-1.amazonaws.com.cn 
user: falcon
password: BapeXazw9.Lego

Redis
	falcon-prod.1gzkge.0001.cnn1.cache.amazonaws.com.cn:6379

