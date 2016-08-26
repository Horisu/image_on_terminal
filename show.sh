#!/bin/bash

if [ $# -ne 1 ]; then
    echo "input image txt"
    exit 1
fi


cat $1 | while read -r line;
do
    echo -e $(line)
done
