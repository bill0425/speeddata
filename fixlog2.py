#! /usr/bin/python3

# Script to convert CSV file from TAB (\t) delimiters to ";"

import sys
import os.path

if len(sys.argv) < 2 :
    name=input("Enter input file: ")
    if os.path.isfile(name) == False:
        print ("Input file does not exist")
        exit
else:
    name=sys.argv[1]
if len(sys.argv) < 3 :
    oname=input('Enter output: ')
    ofile=open(oname,"w")
else:
    ofile=open(sys.argv[2],"w")
with open(name) as SPEED:
    for line in SPEED:
#        line2=line.rstrip('\n')
        if line.find(";") < 0:
            tline=line.replace("\t",";")
            line=tline
        ofile.writelines(line)
#            time.sleep(3)
SPEED.close()
ofile.close()
print ("All Done")
