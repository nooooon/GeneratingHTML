#!/Users/keishu/.pyenv/versions/GeneratingHTML/bin/python
# coding: utf-8


import os
# import falcon
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
print('Content-type: text/html; charset=UTF-8\n')

print(sys.version_info)
print(sys.getdefaultencoding())
print(sys.stdout.encoding)
print(sys.stdin.encoding)

# app = falcon.API()
tmpValue = {'title': 'test', 'body': 'あああおはようsample0３'}

tmp = open('template.html').read()

OUTPUT_DIR = "./output"
OUTPUT_FILE = 'output.html'

print(tmp.format(**tmpValue))
if not os.path.isdir(OUTPUT_DIR):
  os.makedirs(OUTPUT_DIR)

with open(OUTPUT_DIR + '/' + OUTPUT_FILE, "w", encoding='utf-8') as f:
  f.write(tmp.format(**tmpValue))

