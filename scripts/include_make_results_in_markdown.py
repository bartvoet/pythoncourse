import os
import sys
from pandocfilters import toJSONFilter, Str, Para, Image
import re
import subprocess

file_buffer = ""
copy_lines = True

for line in sys.stdin:
    regex = re.compile("\$ \# make and run: \{(.*)\}")
    result = regex.search(line)
    new_code = ""
    if result:
        comp_file = result.group(1)
        make_command = "make " + comp_file
        p = subprocess.Popen(make_command,shell=True,bufsize=64,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        new_code = "$ # make and run: {" + comp_file + "}\n"
        new_code = new_code + "$ " + make_command
        for line in p.stdout:
            new_code = new_code + "\n" + str(line.rstrip())
        p = subprocess.Popen(comp_file,shell=True,bufsize=64,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        new_code = new_code + "\n$ " + comp_file
        for result_line in p.stdout:
            new_code = new_code + "\n"  + str(result_line.rstrip())
        sys.stdout.write(new_code + "\n")
        copy_lines = False
    else:
        if line.startswith("```") or line.startswith("~~~"):
            copy_lines = True
    if copy_lines:
        sys.stdout.write(line)
