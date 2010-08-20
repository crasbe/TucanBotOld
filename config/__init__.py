import os
import configparser as ConfigParser

config_file = "config.cfg"
plugin_file = "plugin.cfg"
config_fd   = ConfigParser.RawConfigParser()
plugin_fd   = ConfigParser.RawConfigParser()
server      = dict()
user        = dict()
plugin      = dict()

if(not os.path.exists(config_file)):
    print("Config File "+config_file+" doesn't exists!")
    exit()

if(not os.path.exists(plugin_file)):
    print("Config File "+plugin_file+" doesn't exists!")
    exit()

server.update({"HOST"           : config_fd.get("Server", "HOST")})
server.update({"PORT"           : config_fd.getint("Server", "PORT")})
server.update({"CHANNEL"        : config_fd.get("Server", "CHANNEL")})
user.update({"NICK"             : config_fd.get("User", "NICK")})
user.update({"IDENTIFICATION"   : config_fd.get("User", "IDENT")})
user.update({"REALNAME"         : config_fd.get("User", "REALNAME")})
plugin.update({"LIST"           : plugin_fd.get("General", "register").split(",")})
for i in plugin["LIST"]:
    plugin.update({plugin["LIST"][i]+"_type" : plugin_fd.get(plugin["LIST"][i], "type")})
    plugin.update({plugin["LIST"][i]+"_input" : plugin_fd.get(plugin["LIST"][i], "input")})
    