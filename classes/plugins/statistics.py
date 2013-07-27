"""
Created: 18.07.2013
Last modified: 18.07.2013

Author: crasbe
"""

import os
import time
import random
import datetime
from datetime import date
from datetime import timedelta

import classes.plugins.plugin as plugin

class Statistics(plugin.Plugin):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        plugin.Plugin.__init__(self)
        
        self.plugins.update({"!didyouknow" : self.didyouknow})
                
    def didyouknow(self):
        random.seed()
        
        def devTime():
            time = int((date.today() - datetime.date(2010, 8, 29)) / \
                       timedelta(days=1))
            return "Wusstest du, dass seit Beginn der Entwicklung von "+ \
                   "TucanBot {0} Tage vergangen sind?".format(time)
        
        def lines():
            codeLines = [i.strip() for i in \
                  os.popen("cd /home/christopher/workspace/TucanBot/src && \
                            find -type f | grep -P '\.py' | grep -P '\.pyc' -v | \
                            xargs cat | wc -l")][0]
            return "Wusstest du, dass im TucanBot "+ \
                    "{0} Zeilen Code friedlich zusammenarbeiten?".format(codeLines)
                   
        def files():
            codeFiles = [i.strip() for i in \
                   os.popen("cd /home/christopher/workspace/TucanBot/src && \
                            find -type f | grep -P '\.py' | grep -P '\.pyc' -v | \
                            wc -l")][0]
            return "Wusstest du, dass TucanBot aus {0} Programmdateien besteht?". \
                    format(codeFiles)
                    
        def timeNow():
            return "Wusstest du, dass es gerade {0} Uhr ist?".\
                    format(time.strftime("%H:%M"))
        
        def length():
            return "Wusstest du, dass crasbe den Längsten hat?"
        
        def drunk():
            return "Wusstest du, dass der Owner dieses Channels mindestens einmal am Tag besoffen ist?"
        
        facts = [lines, devTime, files, timeNow, length, drunk]
        
        return facts[random.randint(0, len(facts)-1)]()