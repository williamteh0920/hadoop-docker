#!/bin/bash

# test the hadoop cluster by running wordcount

# create input files 
mkdir input
echo "Hello world! This is a sample text file for word count.
It contains multiple lines and words. Each line is different, and words may repeat.

Word count is a common task in data processing and analysis. Hadoop MapReduce is often used for such tasks.

This is the end of the sample text file. Have a great day!" >input/file.txt

# create input directory on HDFS
hadoop fs -mkdir -p input

# put input files to HDFS
hdfs dfs -put ./input/* input

# run wordcount 
hadoop jar ~/hadoop-streaming-3.3.6.jar -mapper ~/mapper.py -reducer ~/reducer.py -input ./input/* -output /output

# print the input files
echo -e "\ninput file.txt:"
hdfs dfs -cat input/file.txt

# print the output of wordcount
echo -e "\nwordcount output:"
hdfs dfs -cat output/part-r-00000

