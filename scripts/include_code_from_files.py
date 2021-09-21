#!/usr/bin/env python

"""
Pandoc filter to process code blocks with class "include" and
replace their content with the included file
"""

from pandocfilters import toJSONFilter, CodeBlock
import os.path
import re

def code_include(key, value, format, meta):
    if key == 'CodeBlock':
        regexp = re.compile("//file:(.*)")
        [[ident, classes, namevals], code] = value
        result = regexp.search(code)
        if result:        
            filename = result.group(1)
            if os.path.isfile(filename):
                with open(filename, 'rb') as content_file:
                     content = content_file.read()
                     content.decode('utf-8')
                return CodeBlock([ident, classes, namevals], content)

if __name__ == "__main__":
    toJSONFilter(code_include)
