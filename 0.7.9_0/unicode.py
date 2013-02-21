#!/usr/bin/python2.4
#
# Copyright 2009 Google Inc. All Rights Reserved.

"""Escape UTF-8 characters into '\uFFFF' format.

./unicode.py i18n_orig.js > i18n.js
"""

__author__ = 'jumpei@google.com (Jumpei Takeuchi)'

import sys


def main(argv):
  if len(argv) > 1:
    f = open(argv[1], 'r')
    for line in f:
      translation = unicode(line, 'utf-8')
      escaped_str = []
      for c in translation:
        if ord(c) > 255:
          escaped_str.append('\\u%s' % hex(ord(c))[2:])
        else:
          escaped_str.append(c)
      print ''.join(escaped_str),
    f.close()
  else:
    print 'Usage: unicode.py FILENAME'

if __name__ == '__main__':
  main(sys.argv)
