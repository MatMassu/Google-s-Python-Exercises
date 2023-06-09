#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import requests

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

# Run with: python ./logpuzzle/logpuzzle.py --todir images ./logpuzzle/animal_code.google.com


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  path_list = []
  img_urls = set()

  underbar = filename.index('_')
  host = filename[underbar + 1:]

  with open(filename,'r') as log_file:
    for line in log_file:
      match = re.search(r'GET (\S*puzzle\S*)', line)
      if match:
        path = match.group(1)
        path_list.append(path)

  for path in path_list:
    url = 'https://' + host + path
    img_urls.add(url)

  return list(sorted(img_urls))

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # Make directory if necessary
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir) #images

  count = 0
  # Create index.html with img tag to show each local image file
  file_html = open('index.html', 'w')
  file_html.write('<html><body>')
  for url in img_urls:
    # Write name of image and path for download
    filename = f'img{count}.jpg'
    filepath = os.path.join(dest_dir, filename)
    # Checks for connection and displays status message
    if not os.path.exists(filepath):
      try:
        # Attempt connection and display status
        response = requests.get(url)
        status_code = response.status_code

        # Check for status OK
        if status_code == 200:
          # Download from url to dest_dir
          urllib.request.urlretrieve(url, filepath)
          print(f'{filename} downloaded correctly')
          file_html.write(f'<img src="images/{filename}">')
        else:
          print(f'Error connecting to host for {filename} [Error {status_code}]')

        # Close connection
        response.close()

      except:
        print(f'Error downloading {filename} [Error {status_code}]')
    else:
      print(f'{filename} already exists')

    file_html.write('<html><body>')
    count+=1


def main():
  args = sys.argv[1:]

  if not args:
    print ('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print ('\n'.join(img_urls))

if __name__ == '__main__':
  main()
