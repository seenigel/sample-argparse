#!/usr/bin/python3
import csv

# This works if I just want to hard code name of the file.
# fileName = "presidents.csv"


# But let's try using argparse to pass the file from the command line
import argparse

parser = argparse.ArgumentParser(description='Write the names of presidents to a file of my choosing')
parser.add_argument('-in', '--fileName', type=str, required=True, help='Name of input file')
parser.add_argument('-out','--writeFile', type=str, required=True, help="Name of ouput file")
args = parser.parse_args()

def writePresidents(fileName, writeFile):
    with open (fileName, 'r') as csv_file:
        
        # DictReader lets you call things by the column names, as you would in pandas
        csv_reader = csv.DictReader(csv_file)
        
        f = open(writeFile, 'w+')
        
        for row in csv_reader:
            # print(row['President'])
            line = row['President'] + ' was President from ' + row['Started'] + ' till ' + row['Ended'] + '\n'
            f.write(line)

        f.close()
    csv_file.close()

writePresidents(args.fileName, args.writeFile)

#Now that I've added argparse I can pass the function my variables from the CLI like so:
# ./write-presidents.py -in presidents.csv -out list.txt