#!/usr/bin/env python

"""
Pandoc filter to process code blocks with class "graphviz" into
graphviz-generated images.
"""

import os
import sys
from pandocfilters import toJSONFilter, Str, Para, Image
import re

def write_to_file(file_object,data):
    file_object = open(filename,"w")
    file_object.write(code)
    file_object.close();

def create_and_write_new_file(file_name,data):
     dir = os.path.dirname(filename)
     try:
           os.stat(dir)
     except:
           os.mkdir(dir)

     file_object = open(filename,"w")
     write_to_file(file_object,data)

def append_to_file(file_name,data):
     file_object = open(filename,"a")
     write_to_file(file_object,data)

def coding(key, value, format, meta):
    regexp = re.compile("//file:(.*)")
    regexp_for_partial = re.compile("//file\-([0-9]+):(.*)")
    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        caption = "caption"
        result = regexp.search(code)
        partial_result = regexp.search(code)
        if result:
             filename = result.group(1)
             create_and_write_new_file(filename,code)
        elif partial_result:
             filename = result.group(2)
             if result.group(1) == "1"
                 create_and_write_new_file(filename,code)
             if result.group(1) == "1"
                 append_to_file(filename,code)

if __name__ == "__main__":
    toJSONFilter(coding)
