#!/usr/bin/env python

"""
Pandoc filter to process code blocks with class "include" and
replace their content with the included file
"""

from pandocfilters import toJSONFilter, CodeBlock
import os.path
import re
import sys
import subprocess

def code_include(key, value, format, meta):
    if key == 'CodeBlock':
        # regexp = re.compile("$ # make and run: \{(.*)\}")
        regex = re.compile("\$ \# make and run: \{(.*)\}")
        [[ident, classes, namevals], code] = value
        result = regex.search(code)
        if result:
            comp_file = result.group(1)
            make_command = "make " + comp_file
            try:
                p = subprocess.Popen(make_command,shell=True,bufsize=64,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
                new_code = "$ # make and run: {" + comp_file + "}\n"
                new_code = new_code + "$ " + make_command
                for line in p.stdout:
                    new_code = new_code + "\n" + str(line.rstrip())
                p = subprocess.Popen(comp_file,shell=True,bufsize=64,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
                new_code = new_code + "\n$ " + comp_file
                for line in p.stdout:
                    new_code = new_code + "\n"  + str(line.rstrip())
            except e:
                sys.stderr.write(e)
            return CodeBlock([ident, classes, namevals], new_code)

if __name__ == "__main__":
    toJSONFilter(code_include)
