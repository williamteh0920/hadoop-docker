#!/bin/bash
#crlf to lf change

# test the hadoop cluster by running wordcount

# create input directory on HDFS
hadoop fs -mkdir -p input

# put input files to HDFS
hdfs dfs -put ./input_1000_words.txt input

# run wordcount 
hadoop jar ~/hadoop-streaming-3.3.6.jar -mapper ~/mapper.py -reducer ~/reducer.py -input ./input/* -output /output

# print the output of wordcount
echo -e "\nwordcount output:"
hdfs dfs -cat output/part-00000