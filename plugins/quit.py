'''
Created on 12.08.2010

@author: christopher
'''

def quit(socket, channel):
    socket.send(bytes("PRIVMSG {0} {1}\n".format(channel, "Heute ist nicht \
                                                 alle Tage, ich komme wieder, \
                                                 keine Frage!"), "utf8"))
    socket.send(bytes("QUIT {0}".format("Bye!"), "utf8"))
    return "end"