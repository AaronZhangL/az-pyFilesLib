#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import csv
from collections import OrderedDict

def diffCSV(file1, file2, resultFile, fieldnames, keyColumn):
    signature_row_map = OrderedDict()
    #with open('hosts.csv') as file_object:
    with open(file1) as file_object:
        for line in csv.DictReader(file_object, delimiter='\t'):
            #signature_row_map[line['Signature']] = {'line': line, 'found_at': None}
            signature_row_map[line[keyColumn]] = {'line': line, 'found_at': None}

    print "------debug1------"
    #with open('masterlist.csv') as file_object:
    with open(file2) as file_object:
        for i, line in enumerate(csv.DictReader(file_object, delimiter='\t'), 1):
            #if line['Signature'] in signature_row_map:
            if line[keyColumn] in signature_row_map:
                #signature_row_map[line['Signature']]['found_at'] = i
                signature_row_map[line[keyColumn]]['found_at'] = i

    print "------debug2------"
    #with open('newhosts.csv', 'w') as file_object:
    with open(resultFile, 'w') as file_object:
        #fieldnames = ['Path', 'Filename', 'Size', 'Signature', 'RESULTS']
        writer = csv.DictWriter(file_object, fieldnames, delimiter='\t')
        writer.writer.writerow(fieldnames)
        for signature_info in signature_row_map.itervalues():
            result = '{0} FOUND in masterlist {1}'
            # explicit check for sentinel
            if signature_info['found_at'] is not None:
                result = result.format('', '(row %s)' % signature_info['found_at'])
            else:
                result = result.format('NOT', '')
            payload = signature_info['line']
            payload['RESULTS'] = result
            
            print payload
            print "----------------"
            writer.writerow(payload)

if __name__ == '__main__':
    #path1 = format_path(raw_input('Please input PATH 1: '))
    #path2 = format_path(raw_input('Please input PATH 2: '))
    file1 = "a.csv"
    file2 = "b.csv"
    resultFile = "result.txt"
    # table updatedTranscription
    fieldnames = ['id', 'batch_date', 'transcriber_id', 'voice_num', 'voice_filename', 'transcription', 'tag_1', 'tag_2', 'NonN', 'reviewer1_id', 'reviewer2_id', 'comments', 'AMI_transcription', 'AMI_tag_1', 'AMI_tag_2', 'AMI_NonN', 'check_result', 'pending_level', 'to_so_comment', 'in_AMI_comment', 'result_basis', 'AMI_checker', 'final_checker', 'result_filename', 'create_date', 'update_date', 'RESULTS']
    keyColumn = 'transcriber_id'
    diffCSV(file1, file2, resultFile, fieldnames, keyColumn)  