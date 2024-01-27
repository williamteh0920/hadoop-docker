# hadoop-docker

### 3 Nodes Hadoop Cluster

##### 1. clone github repository


##### 2. change crlf to lf for all .sh file if using wsl/ubuntu


##### 3. Copy the files into wsl (run this cmd in wsl) (this is only example)

```
cp -r /mnt/c/Users/<location of project> ~/hadoopdocker
```

##### 4. build image (in wsl after cd into hadoopdocker)

```
./build-image.sh
```

##### 5. create hadoop network

```
sudo docker network create --driver=bridge hadoop
```

##### 6. start container [(ctrl + d) to exit container user]

```
cd hadoop-docker
sudo ./start-container-master.sh
# press ctrl+d to exit root@hadoop-master
sudo ./start-container-slave12.sh
```

##### 7. start hadoop

```
# Go into root@hadoop-master
sudo docker exec -it hadoop-master bash

./start-hadoop.sh
```

##### 6. run wordcount

```
./run-wordcount.sh
```
