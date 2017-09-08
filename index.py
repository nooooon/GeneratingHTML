#!/usr/bin/env python
# coding: utf-8

import os
import sys
import io
import falcon
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
print('Content-type: text/plain; charset=UTF-8\n')

print(sys.version_info)
print(sys.getdefaultencoding())
print(sys.stdout.encoding)
print(sys.stdin.encoding)

class Resource(object):

  def on_post(self, req, resp):

    try:
      raw_json = req.stream.read()
      msg = {'message': 'Welcome to the Falcon'}
      resp.status = falcon.HTTP_200
    except ValueError:
      msg = {'error': 'ValueError', 'detail': 'invalid value'}
      resp.status = falcon.HTTP_400
      resp.body = json.dumps(msg)
      return

    try:
      data = json.loads(raw_json.decode('utf-8'))
      
    except ValueError:
      raise falcon.HTTPError(falcon.HTTP_753,
        'Malformed JSON',
        'Could not decode the request body. The '
        'JSON was incorrect.')


    if 'name' not in data:
      raise ValueError("No name in given data")
    if 'photo' not in data:
      raise ValueError("No photo in given data")



    if data['name']:
      reqName = data['name']
    else:
      msg = {'error' : 'no name'}
      resp.status = falcon.HTTP_400
      resp.body = json.dumps(msg)
      return

    if data['photo']:
      reqPhoto = data['photo']
    else:
      msg = {'error' : 'no photo'}
      resp.status = falcon.HTTP_400
      resp.body = json.dumps(msg)
      return


    msg = {'title': 'api test', 'name': reqName, 'photo': reqPhoto}

    self.createOutputFile(msg)

    resp.body = json.dumps(msg)



  def createOutputFile(self, tmpValue):
    tmp = open('template.html').read()

    OUTPUT_DIR = './output'
    OUTPUT_FILE = 'output.html'

    if not os.path.isdir(OUTPUT_DIR):
      os.makedirs(OUTPUT_DIR)

    with open(OUTPUT_DIR + '/' + OUTPUT_FILE, 'w', encoding='utf-8') as f:
      f.write(tmp.format(**tmpValue))


app = falcon.API()
app.add_route('/api', Resource())

# if __name__ == "__main__":
#     from wsgiref import simple_server
#     httpd = simple_server.make_server("0.0.0.0", 8000, app)
#     httpd.serve_forever()
