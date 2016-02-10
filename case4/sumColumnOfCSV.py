#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import csv

def diffCSVofNoHeaderRow(file1Name, resultFile, columnsIdxDic):
    print 'file1Name:' + file1Name
    with open(file1Name, "U") as in_file1, open(resultFile, "wb") as out_file:
        reader1 = csv.reader(in_file1, delimiter='\t')
        columnsResultDic = columnsIdxDic.copy()
        # Init value with zero
        for key, value in columnsResultDic.iteritems():
            columnsResultDic[key] = 0
        for row1 in reader1:
            lenOfRow1 = len(row1)
            #print '*****New Line--row1 length*****->' + str(lenOfRow1)
            if (row1):
                for key, value in columnsIdxDic.iteritems():
                    #print 'column:row1['+ str(value) + ']:' + str(row1[value])
                    if value < lenOfRow1:
                        if (row1[value] and row1[value].strip()):
                           columnsResultDic[key] += 1
                           #print 'columnsResultDic['+ key +']:' + str(columnsResultDic[key])
                        #print '[key]=' + key + \
                        #' [value]=' + str(value) + \
                        #' row1[value]=' + row1[value] + \
                        #' columnsResultDic[key]=' + str(columnsResultDic[key])
                    else:
                        columnsResultDic[key] = -99999
        w = csv.DictWriter(out_file, columnsResultDic.keys())
        w.writeheader()
        w.writerow(columnsResultDic)
        
def runSum(folderName, fileName, columnsIdxDic):
    print '-----Start-------'
    file1Name = folderName + fileName
    resultFile = 'SUM-' + fileName    
    diffCSVofNoHeaderRow(file1Name, resultFile, columnsIdxDic)
    print 'File Name:' + file1Name
    print 'Result File Name:' + resultFile
    print '>>Done<<'

if __name__ == '__main__':
    #path1 = format_path(raw_input('Please input PATH 1: '))
    #path2 = format_path(raw_input('Please input PATH 2: '))
    folderName = 'C:\\sample\\csv\\'
    columnsIdxDic = {'sum1':3, 'sum2':4, 'sum3':6, 'sum4':9, 'sum5':11, 'sum6':12, 'sum7':15, 'sum8':16, 'sum9':18, 'sum10':22}
    # Sum file1
    fileName = '0006_00001-10000_0104.csv'
    runSum(folderName, fileName, columnsIdxDic)
