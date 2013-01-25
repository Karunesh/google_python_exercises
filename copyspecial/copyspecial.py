#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_paths(dir_path):
  if not dir_path.endswith('/'):
    dir_path = dir_path + '/'
  files_and_dirs = os.listdir(dir_path)
  special_paths = []
  for _name in files_and_dirs:
    is_special = re.search(r'__\w+__', _name)
    if is_special:
      special_paths.append(dir_path + _name)
  return special_paths



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  special_paths = get_special_paths(args[0])

  for special_path in special_paths:
    if todir: # empty strings return False
      if not os.path.exists(todir):
        os.makedirs(todir)
      shutil.copy(special_path, todir)
    elif tozip:
      print 'case tozip yet to be implemented'
    else:
      print special_path
  
if __name__ == "__main__":
  main()
