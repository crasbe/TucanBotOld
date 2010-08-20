'''
Created on 31.07.2010

@author: Christopher
'''
import os
import configparser as ConfigParser

class Config:
    def __init__(self):
        #Base.__init__(self)
        pass
    def readConfigFile(self, section):
        if(not os.path.exists("..\..\config\config.cfg")):
            print("Config File doesn't exists!")
            exit()
        else:
            server = list()
            config_file = ConfigParser.RawConfigParser()
            config_file.read("..\config\config.cfg")
            if(section == "Server"):
                server.append(config_file.get("Server", "HOST"))
                server.append(config_file.getint("Server", "PORT"))
                server.append(config_file.get("Server", "CHANNEL"))
                return server
            elif(section == "User"):
                user = list()
                user.append(config_file.get("User", "NICK"))
                user.append(config_file.get("User", "IDENT"))
                user.append(config_file.get("User", "REALNAME"))
                return user
            
    def readPluginFile(self):
        if(not os.path.exists("..\config\plugin.cfg")):
            print("Plugin File doesn't exists!")
            exit()
        else:
            plugin_list = list()
            plugin_fd = ConfigParser.RawConfigParser()
            plugin_fd.read("..\config\plugin.cfg")
            
            temp = plugin_fd.get("general", "register")
            temp = temp.split(",")
            for i in range(len(temp)-1):
                plugin_list.append(temp[i])
            del temp
            return plugin_list.append(plugin_fd)