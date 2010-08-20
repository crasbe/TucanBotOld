'''
Created on 02.08.2010

@author: Christopher
Version: 0.0.2
'''

import socket

class Network:
    def __init__(self):
        self.socketfd   = socket.socket()
        self.rawString  = str()
        self.channel    = str()
        self.joined     = False
        
    def socketConnect(self, host, port, channel, nick, id, realname):
        self.channel = channel
        print("Connecting to " + host + ":{0}".format(port))
        try:
            self.socketfd.connect((host, port))
            self.socketfd.send(bytes("NICK " + nick + "\n", "utf8"))
            self.socketfd.send(bytes("USER " + id + " " + host + " " + \
                                     "euda :" + realname + "\n","utf8"))
        except:
            print("Can't connect to " + host + ":" + port)
            exit()
        else:
            print("Connected.")
    
    def getInitPing(self):
        print("Wait for Welcome Messange ...", end="")
        readbuffer = self.socketfd.recv(200)
        print(" here it is!")
        temp = str(readbuffer, "utf8")
        print(temp)
        temp = temp.split("\n") # Secede Ping Messange
        temp = temp[1].split(":") # Get "Ping String"
        print("PONG :"+temp[1])
        self.socketfd.send(bytes("PONG :"+temp[1]+"\n", "utf8"))
    
    def getData(self):
        readbuffer = self.socketfd.recv(1024)
        try:
            self.rawString = str(readbuffer, "utf8")
        except:
            self.rawString = str(readbuffer, "cp1252")
        finally:
            print(self.rawString)
    
    def sendData(self, type, chan=None, messange=None):
        if(type == "PING"):
            temp = self.rawString.split(":")
            print("PONG :" + temp[1])
            self.socketfd.send(bytes("PONG " + temp[1] + "\n", "utf8"))
        elif(type == "PRIVMSG"):
            print("Saying \"" + messange + "\" to " + chan)
            self.socketfd.send(bytes("PRIVMSG " + self.channel + \
                                     " " + messange + "\n", "utf8"))
            
    def analyzeData(self):
        if(not self.joined):
            if("End of /MOTD command." in self.rawString):
                print("Joining Channel " + self.channel)
                self.socketfd.send(bytes("JOIN " + self.channel + \
                                         "\n", "utf8"))
        if("PING :" in self.rawString):
            self.sendData(type="PING")
        elif("!pingpong" in self.rawString):
            self.sendData("PRIVMSG", self.channel, "Pong!")