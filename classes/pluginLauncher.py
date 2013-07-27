"""
Created on 19.09.2010
Last edit on 17.07.2013

Author: crasbe
"""

import imp
from classes.plugins import statistics
from classes.plugins import questionAndAnswer
from classes.plugins import users
from classes.plugins import maths
from classes.plugins import house
from classes.plugins import net

class PluginLauncher:
    """ Plugin-Class:
    This class manages the plugins.
    Variables:
        none
    """

    def __init__(self):
        """ __init__:
        Sets the class attributes.
        Nothing fancy here.
        Class-Attributes:
            self.food  - object for food-plugins            - type: object
            self.stats - object for statistical-plugins     - type: object
            self.users - object for user-handling plugins   - type: object
            self.qaa   - object for question&answer plugins - type: object
        """
        imp.reload(statistics)
        imp.reload(questionAndAnswer)
        imp.reload(users)
        imp.reload(maths)
        imp.reload(house)
        imp.reload(net)
        self.stats = statistics.Statistics()
        self.users = users.Users()
        self.qaa = questionAndAnswer.QuestionAndAnswer()
        self.house = house.Haus()
        self.maths = maths.Maths()
        self.net   = net.Net()
        
    def __call__(self, command, channel, username, message):
        """ __call__:
        This method updates the information needed for the individual plugins.
        It also executes the plugins.
        Variables:
            command  - contains the command                - type: str
            channel  - contains the channelname            - type: str
            username - contains the username of the sender - type: str
            message  - contains the sended message         - type: str
        """
        if(command in self.stats.pluginlist):
            return self.stats(command, channel, username, message)
        elif(command in self.users.pluginlist):
            return self.users(command, channel, username, message)
        elif(command in self.qaa.pluginlist):
            return self.qaa(command, channel, username, message)
        elif(command in self.maths.pluginlist):
            return self.maths(command, channel, username, message)
        elif(command in self.house.pluginlist):
            return self.house(command, channel, username, message)
        elif(command in self.net.pluginlist):
            return self.net(command, channel, username, message)
        else:
            return ""   