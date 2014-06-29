#!/usr/bin/env python
# encoding: utf-8

import os
import os.path
from os.path import basename
import simplejson
import sys


if len(sys.argv) < 2:
  print "jrxml templates should be specified"
  sys.exit(1)

jrxml_templates = sys.argv[1:]
main_report = jrxml_templates[0]
subreports = jrxml_templates[1:]

if len(subreports) < 1:
  print "subreport templates should be specified"
  sys.exit(1)

designs = { 'main': open(main_report).read().replace("\t", '') }

for i in subreports:
  designs[os.path.splitext(basename(i))[0]] = open(i).read().replace("\t", '')

print simplejson.dumps(designs)
