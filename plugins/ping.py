'''
Created on 11.08.2010

@author: christopher
'''

def ping(socket, channel):
    socket.send(bytes("PRIVMSG {0} {1}\n".format(channel, "Pong!"), "utf8"))