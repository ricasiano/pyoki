#!/usr/bin/python

import pycdg
from pykmanager import manager
player = pycdg.cdgPlayer("SF342-16 - Magic! - Rude.cdg")
player.Play()
manager.WaitForPlayer()
