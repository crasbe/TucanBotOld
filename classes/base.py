'''
Created on 03.08.2010

@author: Christopher Büchse
'''

import sys
import configparser

class Base(object):
    def loadConfig(self, config_file):
        config_fd = configparser.RawConfigParser()
        config_fd.read("")
  
    def loadPlugins(self, plugins):
        if(not "plugins/" in sys.path):
            sys.path.insert(0, "plugins/")
        returnValue = {}
        for plugin in plugins:
            returnValue.update({plugin : __import__(plugin)})
        return returnValue
        