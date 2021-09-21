import os
import sys
import re
import getopt
import fnmatch

def write_to_file(file_object,code):
    file_object.write(code)
    file_object.close();

def create_and_write_new_file(filename,code):
     print("creating and writng to " + filename)
     dir = os.path.dirname(filename)
     try:
           os.stat(dir)
     except:
           os.mkdir(dir)

     file_object = open(filename,"w")
     write_to_file(file_object,code)

def append_to_file(filename,code):
    print("appending to " + filename)
    file_object = open(filename,"a")
    write_to_file(file_object,code)

def extract_if_applicable(code):
    regexp = re.compile("//file:\s*\{(.*)\}")
    regexp_for_partial = re.compile("//file\-([0-9]+):\s*\{(.*)\}")

    result = regexp.search(code)
    partial_result = regexp_for_partial.search(code)
    if result:
         filename = result.group(1)
         create_and_write_new_file(filename,code)
    elif partial_result:
         filename = partial_result.group(2)
         if partial_result.group(1) == "1":
             create_and_write_new_file(filename,code)
         else:
             append_to_file(filename,code)

def process_file(f):
    file_buffer = ""
    buffer_read = False

    for line in f:
        if line.startswith("```c") or line.startswith("~~~c"):
            buffer_read = True
        elif line.startswith("```")  or line.startswith("~~~"):
            extract_if_applicable(file_buffer)
            buffer_read = False
            file_buffer = ""
        elif buffer_read:
            file_buffer = file_buffer + line

def process_all_files_in_directory(directory):
  matches = []
  for root, dirnames, filenames in os.walk(directory):
      for filename in fnmatch.filter(filenames, '*.md'):
          md_file = open(os.path.join(root, filename), "r")
          process_file(md_file)
          md_file.close

def main(argv):
   directory = None
   output_directory = ''
   try:
      opts, args = getopt.getopt(argv,"hf:d:o:",["help","file","dir=","output="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-d", "--dir"):
         directory = arg
   
   if directory is None:
      process_file(sys.stdin)
   else:
      process_all_files_in_directory(directory)

if __name__ == "__main__":
   main(sys.argv[1:])

# -d for directory -f for file -o for output-directory (otherwise it's the 
