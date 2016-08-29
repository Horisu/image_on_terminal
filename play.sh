#!/bin/bash

if [ $# -ne 1 ]; then
    echo "input image txt"
    exit 1
fi

ini=1

cat $1 | while read -r line;
do

if [ $ini = 1 ]; then
    height=$line
    num=$height
    ini=0
else
    if [ $num = 0 ]
	then
	num=$height
	sleepenh `echo "${line} / 1000"| bc` > /dev/null
	echo -e "\e[${height}A"
	echo -e "\e[2A"
    else
#	echo $num
#	echo -e "\n"
	echo -e "${line}"
	num=`expr $num - 1`

    fi
fi
done
