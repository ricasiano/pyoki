# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import os
from subprocess import Popen
from subprocess import call
from pyoki_lib import pyokiStyles
from pyoki_lib import pyokiPlay
FNULL = open(os.devnull, 'w')
pyokiStyles.title()
class WSHandler(tornado.websocket.WebSocketHandler):
  def check_origin(self, origin):
    return True
  def open(self):
    pyokiStyles.title()
    print('We have found your device! You may now navigate for songs via App.')
    self.write_message("OK")
  def on_message(self, message):
    pyokiStyles.title()
    if message=='play':
      self.write_message("OK")
      print('Please wait while we prepare your video...')
      Popen(["omxplayer", "/home/py/pyoki_videos/Sublime-Santeria.mp4"], stdout=FNULL, stderr=FNULL)
    elif message=='stop':
      Popen(["killall", "-9", "omxplayer.bin"], stdout=FNULL, stderr=FNULL)
      self.write_message("OK")
    elif message=='off':
      self.write_message("OK")
      Popen(["sudo", "shutdown", "-h", "now"], stdout=FNULL, stderr=FNULL)
    else:
      self.write_message("ERROR")
  def on_close(self):
    print("")

application = tornado.web.Application([
  (r'/ws', WSHandler),
])

if __name__ == "__main__":
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
