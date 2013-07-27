"""
Created on 29.08.2010
Last edit on 17.07.2013

Author: crasbe
"""

import imp
import sys
import time
import socket

import classes.config
import classes.pluginLauncher

import classes.network.parse
import classes.network.ircprotocol

class Network:
    """ Network-Class:
    This class is responsible for the connection and the communication with
    the server. It extends the class with the IRC-Protocol.
    """
    
    def __init__(self):
        """ __init__:
        Sets the class attributes and defines an object for the ircprotocol 
        class.
        Class-Attributes:
            self.socket    - contains the socket - type: socket
            self.ircpro  - contains the object from the IRC-class 
                            - type: object
            self.config  - contains the object from config-class - type: obj
            self.parse   - contains the object from parser-class - type: obj
            self.rawString - contains the raw String from the IRC-Server
                            - type: str
            self.channel   - contains the channel - type: list
            self.quitmsg   - contains the predefined quitmsg
        """
        self.socket = socket.socket()
        self.ircpro = classes.network.ircprotocol.IRCProtocol(self.socket)
        self.userObj = classes.config.Config("users.ini")
        self.parse = classes.network.parse.Parse()
        self.pluginLauncher = classes.pluginLauncher.PluginLauncher()
        self.rawString = str()
        self.channel = list()
        self.quitmsg = str()

            
    def connect(self, netcfg):
        """ connect:
        Connects to the IRC-Server.
        Variables:
            netcfg - contains server information - type: dict
        """
        self.quitmsg = netcfg["quitmsg"]
        try:
            self.socket.connect((netcfg["host"], int(netcfg["port"])))
        except socket.error as e:
            sys.exit(e)
        try:
            self.socket.send(bytes("NICK {0}\n".format(netcfg["nick"]), "utf8"))
            self.socket.send(bytes("USER {0} {1} euda : {2}\n".\
                                   format(netcfg["ident"], netcfg["host"], \
                                            netcfg["realname"]),"utf8"))
            for i in netcfg["channel"].strip().split(","):
                self.ircpro.join(i)
                self.channel.append(i)
        except socket.error as e:
            sys.exit(e)

    def getData(self):
        """ getData:
        Gets the data from the server, encodes it and checks the Ping.
        Variables:
            none
        """
        readbuffer = self.socket.recv(2048)
        try:
            self.rawString = str(readbuffer, "utf8")
        except:
            self.rawString = str(readbuffer, "cp1252")
        
        if("PING :" in self.rawString):
            temp = self.rawString.strip()
            temp = temp.split("PING :")
            self.ircpro.pong(temp[1])

        self.rawString = self.rawString.strip()

        print(self.rawString)
    
        if(self.rawString == ""):
            self.close()
            sys.exit("Close connection, Ping timeout")            
            
    def say(self, text, channel=0):
        """ say:
        This function is a simplified implementation of PRIVMSG.
        Variables:
            text    - text to say     - type: str
            channel - channel to send - type: str
        """
        if(channel == 0): channel = self.channel
        self.ircpro.privmsg(channel, text)
        print("said: "+text)
        
    def close(self, channel, msg):
        """ close:
        Sends the QUIT command to the IRC-server, closes the socket and 
        quits the script.
        Variables:
            channel    - contains the name of the channel - type: str
            msg        - contains the message             - type: str
        """
        self.ircpro.quit(msg)
        self.socket.close()
        sys.exit("Closed connection")
    
    def analyze(self):
        if("PING :" == self.rawString[:5]):
            return
        
        self.parse.inputString = self.rawString
        channel = self.parse.channelSplit()
        username = self.parse.usernameSplit()
        message = self.parse.messageSplit()
        
        receiverChan = channel
        if(receiverChan == "TucanBot"):
            receiverChan = username
        
        if("mmfan" in message.lower()):
            self.say(self.pluginLauncher("mmfan", channel, receiverChan, \
                                         message))
            return
        else:
            command = self.parse.commandSplit()
        
        if(command == "!refresh"):
            imp.reload(classes.pluginLauncher)
            self.pluginLauncher = classes.pluginLauncher.PluginLauncher()
            self.say("Refresh complete!", receiverChan)
            return
        elif(command == "!quit" and username.lower() == "crasbe"):
            self.close(receiverChan, self.quitmsg)

        answer = self.pluginLauncher(command, channel, username, message)
        if(answer != "" and answer != None):
            self.say(answer, receiverChan)
            
    def log(self):
        if(len(self.channel) < 1 or self.parse.receivedCommandSplit() != "PRIVMSG"): # when not joined, there is nothing to log
            return
        self.userObj.writeSection(self.parse.usernameSplit().lower(), \
                                  {"time" : time.strftime("%d.%m.%Y-%H:%M:%S %Z"), \
                                   "message" : self.parse.messageSplit(), \
                                   "channel" : self.parse.channelSplit(), \
                                   "name"    : self.parse.usernameSplit()})