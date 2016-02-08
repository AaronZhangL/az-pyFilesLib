#!/usr/bin/python
# -*- coding: utf-8 -*-

# Example Input: F:\, F:\temp

import os, sys, time
from filecmp import dircmp

def write_file(path1, path2):
    dcmp = dircmp(path1, path2)
    dateStr = time.strftime("%Y%m%d-%H%M%S",time.localtime())
    fileName = "file_contrast_result_" + dateStr + ".txt"
    with open(fileName, "w") as f:
        f.write("[left folder]" + path1 + os.linesep)
        f.write("[right folder]" + path2 + os.linesep)
        f.write("---------Result------------" + os.linesep)
        
        #f.writelines([line + os.linesep for line in content])
        print_diff_files(dcmp, f)
        #print "Done!AZ"
# Add by Aaron.Z
def print_diff_files(dcmp, f):
    for name in dcmp.diff_files:
        content = "diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right)
        #print("diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right))
        print "[diff files]"
        print content
        f.write("[diff file]" + os.linesep)
        f.write(content + os.linesep)
    for name in dcmp.left_only:
        content = "diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right)
        print "[left only]"
        print content
        f.write("[left only file]" + os.linesep)
        f.write(content + os.linesep)
    for name in dcmp.right_only:
        content = "diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right)
        print "[right only]"
        print content
        f.write("[right only file]" + os.linesep)
        f.write(content + os.linesep)
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp, f)

if __name__ == '__main__':
    path1 = format_path(raw_input('Please input PATH 1: '))
    path2 = format_path(raw_input('Please input PATH 2: '))
    #path1 = "D:\\temp\\20160205diffFolder\\20160205_tmp\\03 232122"
    #path2 = "D:\\temp\\20160205diffFolder\\20160205_tmp\\05 154131"
    write_file(path1, path2)    
