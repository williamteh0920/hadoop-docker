#!/bin/bash
#crlf to lf change

# start hadoop master container
sudo docker rm -f hadoop-master &> /dev/null
echo "start hadoop-master container..."
sudo docker run -itd \
                --net=hadoop \
                -p 50070:50070 \
                -p 8088:8088 \
                --name hadoop-master \
                --hostname hadoop-master \
                william/hadoop &> /dev/null

# get into hadoop master container
sudo docker exec -it hadoop-master bash