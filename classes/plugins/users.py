"""
Created: 18.07.2013
Last modified: 18.07.2013

Author: crasbe
"""

import random
from datetime import timedelta
from datetime import datetime

import classes.config

import classes.plugins.plugin as plugin

class Users(plugin.Plugin):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        plugin.Plugin.__init__(self)
        
        self.plugins.update({"mmfan" : self.mmfan, \
                             "!seen" : self.seen, \
                             "!lastmsg" : self.lastmsg})
        self.config = classes.config.Config("users.ini")
        
    def mmfan(self):
        answers = [ "MMFan stinkt wie ein alter Abfalleimer!",
                    "Hau bloß ab mit MMFan!",
                    "MMFan... *schüttel*",
                    "MMFan ist ein echter Taugenichts!",
                    "MMFan hat hier nichts zu suchen!",
                    "\001ACTION mag MMFan nicht.\001" ]
        random.seed()
        return answers[random.randint(0, len(answers)-1)]
    
    def seen(self):
        self.receiver = self.message.replace(self.command, "").strip().lower()
        if(self.receiver == ""):
            output = "Folgende User habe ich schon gesehen: "
            for i in self.config.sections():
                output += self.config.read(i, "name")+" "
            return output
        if(not self.config.hasSection(self.receiver)):
            return "Ich habe den User "+self.receiver+" noch nicht gesehen."
        section = self.config.readSection(self.receiver)
        
        deltaTime = datetime.now() - datetime.strptime(section["time"], "%d.%m.%Y-%H:%M:%S %Z")
        seconds = int(deltaTime / timedelta(seconds=1))
        minutes = int(seconds // 60)
        seconds %= 60
        hours = int(minutes // 60)
        minutes %= 60
        days = int(hours // 24)
        hours %= 24
        
        output = section["name"]+" habe ich zuletzt vor "

        if(days >= 1):
            if(days == 1):
                output += "1 Tag"
            elif(days > 1):
                output += str(days)+" Tagen"
            
            if(hours == 1):
                output += ", 1 Stunde"
            elif(hours > 1):
                output += ", "+str(hours)+" Stunden"
                   
            if(minutes == 1):
                output += ", 1 Minute"
            else:
                output += ", "+str(minutes)+" Minuten"
                        
            if(seconds == 1):
                output += " und 1 Sekunde"
            else:
                output += " und "+str(seconds)+" Sekunden"

        else:
            if(hours >= 1):
                if(hours == 1):
                    output += "1 Stunde"
                elif(hours > 1):
                    output += str(hours)+" Stunden"
                
                if(minutes == 1):
                    output += ", 1 Minute"
                else:
                    output += ", "+str(minutes)+" Minuten"
                        
                if(seconds == 1):
                    output += " und 1 Sekunde"
                else:
                    output += " und "+str(seconds)+" Sekunden"
            else:
                if(minutes >= 1):
                    if(minutes == 1):
                        output += "1 Minute"
                    else:
                        output += str(minutes)+" Minuten"
                        
                    if(seconds == 1):
                        output += " und 1 Sekunde"
                    else:
                        output += " und "+str(seconds)+" Sekunden"
                else:
                    if(seconds == 1):
                        output += "1 Sekunde"
                    else:
                        output += str(seconds)+" Sekunden"
        
        return output+" in "+self.channel+" gesehen."
    
    def lastmsg(self):
        self.receiver =self. message.replace(self.command, "").strip()
        if(self.receiver == ""):
            return "Wessen letzte Nachricht möchtest du lesen???"
        section = self.config.readSection(self.receiver)
        return self.receiver+" hat zuletzt in "+section["channel"]+" um "+\
                section["time"].split("-")[1]+" gesagt: \""+\
                section["message"]+"\""