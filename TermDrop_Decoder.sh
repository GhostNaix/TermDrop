#!/bin/bash
FILE=$1
SCRIPTNAME=$(basename "$0")

if [ -z "$FILE" ]; then
	echo "You must specify a file"
	echo "Usage: ./$SCRIPTNAME [.b64 filename]"
	exit 1
fi

if [ -f "$FILE" ]; then
    echo "Decoding base64 and decompressing"
    base64 -d $FILE > Compressed_tool.tar.gz
    if [ ! -d "Compressed_tool" ]; then
    	mkdir "Compressed_tool"
    fi
    tar -xzvf Compressed_tool.tar.gz -C Compressed_tool
    exit 0
else 
    echo "The $FILE which you specified does not exist"
    exit 1
fi