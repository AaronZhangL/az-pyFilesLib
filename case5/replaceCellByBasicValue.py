#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import csv

# [Parameter sample]
# BasicFileName: standard.csv
# targetFileName: abc_MERGE.csv
#                 abc_NonN_0120FORMAT.csv
#                 abc_0120FORMAT.csv
# resultFileName: result.csv
def replaceCellByBasicValue(BasicFileName, targetFileName, resultFileName, logFileName):
    with open(BasicFileName, "U") as in_file1, open(targetFileName, "rb") as in_file2, open(resultFileName, "wb") as out_file, open(logFileName, "wb") as log_file:
        reader1 = csv.reader(in_file1, delimiter='\t')
        reader2 = csv.reader(in_file2, delimiter='\t')
        writer = csv.writer(out_file, delimiter='\t')
        logWriter = csv.writer(log_file, delimiter='\t')
        rows1 = [row for row in reader1] # all the content of file1 goes in RAM.
        for row2 in reader2:
            print '[KEY COLUMN OF ROW] = ' + row2[2]
            for row1 in rows1:
                if (row1[0] == row2[2]):
                    print '  Update value of current row'
                    markRow = ['[UpdatedRow][Privous]']
                    logWriter.writerow(markRow)
                    logWriter.writerow(row2)
                    row2[10] = row1[2]
                    row2[17] = row2[17] + ',' + row1[8]
                    markRow = ['[Current]']
                    logWriter.writerow(markRow)
                    logWriter.writerow(row2)
                    break
            writer.writerow(row2)
    print '--DONE----------------------'
    print '[BasicFileName]'
    print '  ' + BasicFileName
    print '[targetFileName]'
    print '  ' + targetFileName
    print '[resultFileName]'
    print '  ' + resultFileName
    print '[logFileName]'
    print '  ' + logFileName
    print '----------------------------'
#-------------------------------------

if __name__ == '__main__':
    #path1 = format_path(raw_input('Please input PATH 1: '))
    #path2 = format_path(raw_input('Please input PATH 2: '))
    folderName = 'C:\\temp'
    BasicFileName = folderName + 'abc.csv'
    fileName = 'efg.xlsx.aaron.csv'
    targetFileName = folderName + fileName
    resultFileName = 'RESULT-' + fileName
    logFileName = 'LOG-' + fileName
    replaceCellByBasicValue(BasicFileName, targetFileName, resultFileName, logFileName)