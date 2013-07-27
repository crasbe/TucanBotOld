"""
Created on 29.08.2010
Last edit on 17.07.2013

Author: crasbe
"""

import classes.config
import classes.network.network

config = classes.config.Config("config.cfg")
network = classes.network.network.Network()

network.connect(config.readSection("server"))


while True:
    network.getData()
    network.analyze()
    network.log()