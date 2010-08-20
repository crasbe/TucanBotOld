'''
Created on 02.08.2010

@author: Christopher Büchse
Version: 0.0.2
'''

import sys

import classes
import classes.base
import classes.config
import classes.network

config_file = {
               "config" : "config/config.cfg",
               "plugin" : "config/plugin.cfg"
               }


base    = classes.base.Base()

pluginObjects = base.loadPlugins(["pingpong", "quit"])

network = classes.network.Network()
network.socketConnect("irc.euirc.net", 6667, "#winhistory", "TucanBot", \
                      "tuccitucci", "TucciTucci")
try:
    network.getInitPing()
except:
    pass

while True:
    network.getData()
    if(network.analyzeData(pluginObjects) == "end"):
        sys.exit()