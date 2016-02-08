#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import csv

def diffCSVofNoHeaderRow(file1Name, file2Name, resultFile, fieldnames):
    with open(file1Name, "U") as in_file1, open(file2Name, "rb") as in_file2,open(resultFile, "wb") as out_file:
       reader1 = csv.reader(in_file1,delimiter='\t')
       reader2 = csv.reader(in_file2,delimiter='\t')
       writer = csv.writer(out_file,delimiter='\t')
       writer.writerow(fieldnames)
       
       rows2 = [row for row in reader2] # all the content of file2 goes in RAM.
       #print rows2
       for row1 in reader1:
           for row2 in rows2:
                #print '[row1]' + row1[1] 
                #print '[row2]' + row2[2]
                if (row1[2] == row2[2]):
                    count = 0
                    row2ColLen = len(row2)
                    for i in range(row2ColLen):
                        if row1[i] == row2[i]:
                            count = i
                            #print '--count-->' + str(count)
                        else:
                            break
                    print '-- row2ColLen:' + str(row2ColLen-1)
                    print '-- count:' + str(count)
                    if ((row2ColLen-1) == count):
                       data = ['Same row', row1[2]]
                       print '-----eq------'
                       #print data
                       #writer.writerow(data)
                    else:
                        print '------else---------'
                        data = ['[Diff row of file2 with file1]']
                        for cell in row2:
                            data.append(cell)
                        writer.writerow(data)
                print '[mark]'

if __name__ == '__main__':
    #path1 = format_path(raw_input('Please input PATH 1: '))
    #path2 = format_path(raw_input('Please input PATH 2: '))
    file1Name = "a.csv"
    file2Name = "b.csv"
    resultFile = "results.csv"
    # Define: column of updatedTranscription table
    fieldnames = ['RESULT','id', 'batch_date', 'transcriber_id', 'voice_num', 'voice_filename', 'transcription', 'tag_1', 'tag_2', 'NonN', 'reviewer1_id', 'reviewer2_id', 'comments', 'AMI_transcription', 'AMI_tag_1', 'AMI_tag_2', 'AMI_NonN', 'check_result', 'pending_level', 'to_so_comment', 'in_AMI_comment', 'result_basis', 'AMI_checker', 'final_checker', 'result_filename', 'create_date', 'update_date']
    diffCSVofNoHeaderRow(file1Name, file2Name, resultFile, fieldnames)