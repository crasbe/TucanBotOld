'''
Created on 02.08.2010

@author: Christopher Büchse
Version: 0.0.2
'''

import socket

class Network:
    def __init__(self):
        self.socket = socket.socket()
        self.rawString = str()
        self.channel = str()
        self.joined = False
        
    def socketConnect(self, host, port, channel, nick, id, realname):
        self.channel = channel
        try:
            self.socket.connect((host, port))
            self.socket.send(bytes("NICK {0}\n".format(nick), "utf8"))
            self.socket.send(bytes("USER {0} {1} euda : {2}\n".\
                                   format(id, host, realname),"utf8"))
        except:
            print("Can't connect to {0}:{1}".format(host, port))
            exit()
    
    def getInitPing(self):
        readbuffer = self.socket.recv(200)
        pingmsg = str(readbuffer, "utf8")
        pingmsg = pingmsg.split("\n")
        pingmsg = pingmsg[1].split(":")
        self.socket.send(bytes("PONG :{0}\n".format(pingmsg[1]), "utf8"))
    
    def getData(self):
        readbuffer = self.socket.recv(1024)
        try:
            self.rawString = str(readbuffer, "utf8")
        except:
            self.rawString = str(readbuffer, "cp1252")
        finally:
            if(not "PING :" in self.rawString):
                print(self.rawString)
    
    def sendData(self, chan, messange):
        self.socket.send(bytes("PRIVMSG {0} {1}\n".format(self.channel, \
                                                            messange), "utf8"))
    
    def join(self):
        if("End of /MOTD command." in self.rawString):
            self.socket.send(bytes("JOIN {0}\n".format(self.channel), "utf8"))
            
    def analyzeData(self, pluginObjects):
        if(not self.joined):
            self.join()
        if("PING :" in self.rawString and not "PRIVMSG" in self.rawString):
            pingvalue = self.rawString.split(":")
            self.socket.send(bytes("PONG :{0}".format(pingvalue), "utf8"))
        elif("PRIVMSG" in self.rawString):
            try:
                work_value = self.rawString.split(":")
                work_value = work_value[2].split("!")
                try:
                    work_value = work_value[1].strip()
                except:
                    pass
                for k in pluginObjects:
                    if(k == work_value):
                        if(getattr(pluginObjects[k], work_value)(self.socket,\
                                                                 self.channel)\
                           == "end"):
                            self.socket.close()
                            return "end"
            except:
                print("Can't execute function.")