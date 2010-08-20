'''
Created on 02.08.2010

@author: Christopher
'''

import classes.network

def pingpong():
    classes.network.sendData("PingPong!", "PRIVMSG")