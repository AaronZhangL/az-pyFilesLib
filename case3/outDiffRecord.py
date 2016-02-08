#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import csv
from collections import OrderedDict

signature_row_map = OrderedDict()


with open('hosts.csv') as file_object:
    for line in csv.DictReader(file_object, delimiter='\t'):
        signature_row_map[line['Signature']] = {'line': line, 'found_at': None}


with open('masterlist.csv') as file_object:
    for i, line in enumerate(csv.DictReader(file_object, delimiter='\t'), 1):
        if line['Signature'] in signature_row_map:
            signature_row_map[line['Signature']]['found_at'] = i


with open('newhosts.csv', 'w') as file_object:
    fieldnames = ['Path', 'Filename', 'Size', 'Signature', 'RESULTS']
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

