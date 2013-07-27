"""
Created: 20.07.2013
Last modified: 20.07.2013

Author: crasbe
"""

import classes.plugins.plugin as plugin

import urllib.request

class Net(plugin.Plugin):
    """
    classdocs
    """


    def __init__(self):
        """
        Constructor
        """
        plugin.Plugin.__init__(self)
        
        self.plugins.update({"!tinyurl" : self.tinyurl})
        
    def tinyurl(self):
        if(self.receiver == self.username):
            return "Bitte eine URL angeben!"
        url = self.receiver
        if(not (url.startswith("http://") or url.startswith("https://"))):
            url = "http://"+self.receiver
        return urllib.request.urlopen("http://tinyurl.com/api-create.php?url=" \
                                      + url).readline().decode('utf8')
        
    def urltitle(self):
        if(self.receiver == self.username):
            return "Bitte eine URL angeben!"
        url = self.receiver
        if(not (url.startswith("http://") or url.startswith("https://"))):
            url = "http://"+self.receiver
        