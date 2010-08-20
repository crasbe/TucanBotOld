# -*- coding: UTF-8 -*-
import classes
import classes.config
import classes.plugin
import classes.network

import config

config  = classes.config.Config()
plugin  = classes.plugin.Plugin()
network = classes.network.Network()

config_server   = config.readConfigFile("Server")
config_user     = config.readConfigFile("User")
plugin_list     = config.readPluginFile()
plugin_fd       = plugin_list.pop(len(plugin_list)-1)
plugin_dict     = plugin.loadPluginInfo(plugin_list, plugin_fd)
plugin.loadPlugins(plugin_dict)

network.socketConnect()

while True:
    network.getData()