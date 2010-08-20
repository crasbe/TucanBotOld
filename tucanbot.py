'''
Created on 02.08.2010

@author: Christopher
Version: 0.0.2
'''

import classes
import classes.network

network = classes.network.Network()
network.socketConnect("irc.euirc.net", 6667, "#winhistory", "TucanBot", \
                      "tuccitucci", "TucciTucci")
network.getInitPing()

while True:
    network.getData()
    network.analyzeData()