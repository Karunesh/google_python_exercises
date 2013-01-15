#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def get_file_lines(filename):
  f = open(filename, 'rU')
  file_lines = f.readlines()
  f.close()
  return file_lines

def is_valid_line(line):
  """
  Check if the beginning of a line matches the format we have for lines with 
  names and ranks.
  """
  line_match = re.search(r'<tr align="right"><td>\d+', line)
  if line_match:
    return True
  return False

def get_rank_and_names(line):
  """
  Returns a list containing rank and two names from line, PROVIDED line is valid.
  """
  rank_and_names = []
  rank_match = re.search(r'\d+', line)
  rank_and_names.append(int(rank_match.group()))
  names = re.findall(r'>[a-zA-Z]+<', line)
  for name in names:
    rank_and_names.append(name[1:-1]) # first and last chars in the matches are '>' and '<'
  return rank_and_names

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  year_match = re.search(r'[0-9][0-9][0-9][0-9]\.', filename) # A dot for beginning of file extension after year
  year = int(year_match.group()[:-1]) # last character matched is the dot.
  
  name_year_dict = {}
  file_lines = get_file_lines(filename)
  for file_line in file_lines:
    if is_valid_line(file_line):
      rank_and_names = []
      rank_and_names = get_rank_and_names(file_line)
      name_year_dict[rank_and_names[1]] = rank_and_names[0]
      name_year_dict[rank_and_names[2]] = rank_and_names[0]

  result_list = []
  result_list.append(str(year))
  sorted_tuples = sorted(name_year_dict.items())
  for each_tuple in sorted_tuples:
    result_list.append(each_tuple[0] + ' ' + str(each_tuple[1]))
  
  return result_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  summary_string = ''
  for filename in args:
    for each_string in extract_names(filename):
      summary_string += each_string
      summary_string += '\n'

  if summary: # write summary_string to a summary file
    f = open('summary.txt', 'w')
    f.write(summary_string)
  else:
    print summary_string
  
if __name__ == '__main__':
  main()
