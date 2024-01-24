#!/bin/bash
#crlf to lf change

echo ""

echo -e "\nbuild docker hadoop image\n"
sudo docker build -t william/hadoop .

echo ""