'''
Created on 03.08.2010

@author: Christopher Büchse
'''

import classes.network

def pingpong(socket, channel):
    socket.send(bytes("PRIVMSG {0} {1}\n".format(channel, "PongPing!"), "utf8"\
                      ))