# -*- coding: utf-8 -*-


import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import os
import time
import json
from subprocess import Popen
from subprocess import call
from pyoki_lib import pyokiStyles, pyokiPlay, pyokiList
from pycdg_lib import pycdg, pykmanager
#from pykmanager import manager
styles = pyokiStyles.Header()
myplay = pyokiPlay.Play()
mylist = pyokiList.List()
FNULL = open(os.devnull, 'w')
styles.title()
class WSHandler(tornado.websocket.WebSocketHandler):
  def check_origin(self, origin):
    return True
  def open(self):
    styles.title()
    print('We have found your device! You may now navigate for songs via App.')
  def on_message(self, message):
    styles.title()
    if message=='LIST':
      self.write_message("OK")
      print('Listing all songs')
    elif message=='ARTISTS':
      print('Listing all artists')
      myartists = mylist.artists()
      data = json.dumps(myartists)
      self.write_message(data)
    elif 'SONGS' in message:
      artistid = message.split(' ')
      print('Listing all songs')
      mysongs = mylist.artistSongs(artistid[1])
      data = json.dumps(mysongs)
      self.write_message(data)
    elif 'PLAY' in message:
      self.write_message("OK")
      songid = message.split(' ')
      print('Preparing your song. Please Wait...')
      mysong = myplay.song(songid[1])
      print('Title:'+mysong['name'] + ' File:' + mysong['file'])
      #Pplayer = pycdg.cdgPlayer("/media/NASDRIVE/"+mysong['file'], playErrorCallback, playFinishedCallback)
      #Pplayer.Play()
      #Pmanager.WaitForPlayer()
      Popen(["pycdg", "/media/NASDRIVE/"+mysong['file']], stdout=FNULL, stderr=FNULL)
      #Popen(["omxplayer", "/home/py/pyoki_videos/1.mp4"], stdout=FNULL, stderr=FNULL)
    elif message=='STOP':
      #Popen(["killall", "-9", "omxplayer.bin"], stdout=FNULL, stderr=FNULL)
      Popen(["killall", "-9", "pycdg"], stdout=FNULL, stderr=FNULL)
      self.write_message("OK")
    elif message=='OFF':
      self.write_message("OK")
      Popen(["sudo", "shutdown", "-h", "now"], stdout=FNULL, stderr=FNULL)
    else:
      self.write_message("ERROR")
  def on_close(self):
    print("")

application = tornado.web.Application([
  (r'/', WSHandler),
])

if __name__ == "__main__":
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(1819)
  tornado.ioloop.IOLoop.instance().start()
