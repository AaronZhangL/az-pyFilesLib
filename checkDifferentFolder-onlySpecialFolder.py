#!/usr/bin/python
# -*- coding: utf-8 -*-

# Example Input: F:\, F:\temp

import os, sys, time

def get_file_info_list(path):
    file_info_list = {}
    
    for root, dir_list, file_list in os.walk(path):
        for file_name in file_list:
            cur_file = os.path.join(root, file_name)

            # Added try-except to prevent "windows error" causing by filename parsing error
            try:
                file_stat = os.stat(cur_file)
                file_info = {
                    'file_size': file_stat[-4],
                    'file_mtime': file_stat[-2],
                }
                file_info_list[cur_file.replace(path, '', 1)] = file_info
            except:
                print "Error: " + cur_file
    
    return file_info_list

def file_contrast(path1, path2):
    file_info_list1 = get_file_info_list(path1)
    file_info_list2 = get_file_info_list(path2)
    
    for fi in file_info_list1.keys():
        if fi in file_info_list2.keys():
            if file_info_list1[fi] == file_info_list2[fi]:
                del file_info_list1[fi]
            del file_info_list2[fi]
    
    different_files = add_root_path(path1, file_info_list1)
    different_files += add_root_path(path2, file_info_list2)
    different_files.sort()
    
    return different_files

def add_root_path(path, file_info_list):
    return [os.path.join(path, name) for name in file_info_list.keys()]

def format_path(path):
    return path.rstrip('\\') + '\\'

def write_file(content):
    dateStr = time.strftime("%Y%m%d-%H%M%S",time.localtime())
    fileName = "file_contrast_result_" + dateStr + ".txt"
    with open(fileName, "w") as f:
        f.writelines([line + os.linesep for line in content])
        print "Done!"
    
if __name__ == '__main__':
    #path1 = format_path(raw_input('Please input PATH 1: '))
    #path2 = format_path(raw_input('Please input PATH 2: '))
    path1 = "D:\\20160205_tmp-simple\\03 232122"
    path2 = "D:\\20160205_tmp-simple\\05 154131"
    print path1
    print path2
    write_file(file_contrast(path1, path2))
