#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import csv

def diffCSVofNoHeaderRow(file1, file2, resultFile, fieldnames, keyColumn):
    #with open('masterlist.csv', 'rb') as master:
    with open(file1, 'rb') as master:
        
        #for i, r in enumerate(csv.reader(master)
        #    print i,r
        #print "<---------------"
        reader1 = csv.reader(master, delimiter='\t')
        print "-----reader1---------->"
        #for row in reader1:
        #    print row
        #master_indices = dict((r[2], i) for i, r in enumerate(reader1))
        master_indices = dict((r[2], i) for i, r in enumerate(reader1))
        #print master_indices
        
    #with open('hosts.csv', 'rb') as hosts:
    with open(file2, 'rb') as hosts:
        #with open('results.csv', 'wb') as results:    
        with open(resultFile, 'wb') as results:    
            file2Reader = csv.reader(hosts, delimiter='\t')

            writer = csv.writer(results)
            #Add header row
            writer.writerow(fieldnames+ ['RESULTS'])
            #writer.writerow(next(file2Reader, []) + ['RESULTS'])

            for row in file2Reader:
                #Compare key column
                index = master_indices.get(row[2])
                if index is not None:
                    message = 'FOUND in file1 list (row {})'.format(index)
                    #Compare every column
                else:
                    message = 'NOT FOUND in file1 list'
                writer.writerow(row + [message])
                writer.writerow('\n')

if __name__ == '__main__':
    #path1 = format_path(raw_input('Please input PATH 1: '))
    #path2 = format_path(raw_input('Please input PATH 2: '))
    file1 = "a.csv"
    file2 = "b.csv"
    resultFile = "results.csv"
    # table updatedTranscription
    fieldnames = ['id', 'batch_date', 'transcriber_id', 'voice_num', 'voice_filename', 'transcription', 'tag_1', 'tag_2', 'NonN', 'reviewer1_id', 'reviewer2_id', 'comments', 'AMI_transcription', 'AMI_tag_1', 'AMI_tag_2', 'AMI_NonN', 'check_result', 'pending_level', 'to_so_comment', 'in_AMI_comment', 'result_basis', 'AMI_checker', 'final_checker', 'result_filename', 'create_date', 'update_date']
    keyColumn = 'transcriber_id'
    diffCSVofNoHeaderRow(file1, file2, resultFile, fieldnames, keyColumn)  