'''
Created on 31.07.2010

@author: Christopher
'''

import os
import imp

class Plugin:
    def loadPluginInfo(self, plugin_list, plugin_fd):
        plugin = {
                  "list"      : plugin_list,
                  "fd"        : plugin_fd,
                  "type"      : list(),
                  "input"     : list(),
                  "output"    : list(),
                  "funtion"   : list(),
                  "file"      : list()
                  }
                
        for i in plugin["list"]:
            plugin["type"].append(plugin["fd"].get(plugin["list"][i], \
                                                   "type"))
            plugin["input"].append(plugin["fd"].get(plugin["list"][i], \
                                                    "input"))
            if(plugin["type"][i] == "Simple"):
                plugin["output"].append(plugin["fd"].get \
                                        (plugin["list"][i], "output"))
            
            elif(plugin["type"][i] == "ExternFile"):
                plugin["function"].append(plugin["fd"].get \
                                          (plugin["list"][i], \
                                           "function"))
                plugin["file"].append(plugin["fd"].get\
                                      (plugin["list"][i], "file"))
        return plugin
    def loadPlugins(self, plugin):
        for i in plugin["list"]:
            if(not os.path.exists('..\plugins\\'+plugin["file"][i]+".py")):
                print("Module "+plugin["list"][i]+" doesn't exists!")
                continue
            else:
                try:
                    herbert = __import__(plugin["list"][i])
                except:
                    print("Cannot load Module "+plugin["list"][i]+"!")
                    continue
                #try:
                #    pass