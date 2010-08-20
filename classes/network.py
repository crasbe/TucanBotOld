'''
Created on 31.07.2010

@author: Christopher
'''

import socket
import classes.config as Config

class Network:
    def __init__(self):
        self.__socketfd  = socket.socket()
        self.__rawString = str()
    
    def socketConnect(self):
        server = Config.readConfigFile("Server")
        user   = Config.readConfigFile("User")
        try:
            print("Connecting to {0]:{1}".format())
            self.__socketfd.connect((server[0], server[1]))
            self.__socketfd.send(bytes("NICK {0}\n".format(user[0]),\
                                       "utf8"))
            self.__socketfd.send(bytes("USER {0} {1} oeoe :{2}\n".\
                                       format(user[1], server[0], \
                                              user[2]), "utf-8"))
            print("Connected")
        except:
            print("Cannot connected to Server {0}:{1}".format(server[0],\
                                                              server[1]))
            exit()

    def getData(self):
        readbuffer = self.__socketfd.recv(1024)
        try:
            self.__rawString = str(readbuffer, "utf8")
        except:
            self.__rawString = str(readbuffer, "cp1252")
        # Give output
        print(self.__rawString)
    
    def sendData(self, messange, type):
        if(type == "PRIVMSG"):
            self.__socketfd.send(bytes("PRIVMSG {0} {1}\n".format(self.__channel, messange), "utf8"))