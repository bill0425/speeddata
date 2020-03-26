#! /bin/python3
#
# This script takes the input line from speedtest and makes the upload and
# download data a bit more readable so that it can be loaded into some 
# sort of database
#
# BTW each version of speedtest.cli seems to have different formating rules
# so this script is specific to the on currently being used. The goal is to 
# format the data so it can be put into some sort of a database.

import sys

for line in sys.stdin:

    line2=line.rstrip()
    speedline=line2.split(';')
#
# The following takes care of the header line

    if speedline[6] == "Download":
        continue
#
# Set the throughput number to be in Megabytes instead of bytes

    speedline[6]=float(speedline[6])/1024/1024
    speedline[7]=float(speedline[7])/1024/1024
#
# Convert the data back to string

    str(speedline[6])
    str(speedline[7])
#
# Print out the data
    newline=""
    for data in speedline:
        newline = newline + str(data) + ";"
    print(newline)

