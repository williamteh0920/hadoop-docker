#!/bin/bash
#crlf to lf change

# start hadoop slave container
i=1
N=3
while [ $i -lt $N ]
do
	sudo docker rm -f hadoop-slave$i &> /dev/null
	echo "start hadoop-slave$i container..."
	sudo docker run -itd \
	                --net=hadoop \
	                --name hadoop-slave$i \
	                --hostname hadoop-slave$i \
	                william/hadoop &> /dev/null
	i=$(( $i + 1 ))
done 

# get into hadoop slave 3 container
sudo docker exec -it hadoop-slave1 bash