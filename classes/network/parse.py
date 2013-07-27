"""
Created on 29.08.2010
Last edit on 18.07.2013

Author: crasbe
"""

class Parse:
    """
    This class is responsible for analyzing and parsing the output of the
    IRC-Server.
    Variables:
        none
    """

    def __init__(self):
        """ __init__:
        __init__ is responsible for initializing the class variables
        Class-Attributes:
            self.rawString - contains the raw string recived from the server
                                - type: str
        """
        self.rawString = str()
    
    def __setattr__(self, name, value):
        """ __setattr___:
        This function refreshes variable self.rawString with new
        content.
        Variables:
            rawString - contains the new content - type: str
        """
        if(name == "inputString"):
            self.__dict__["rawString"] = value

        
    def messageSplit(self):
        """ messageSplit:
        This method is responsible for getting the message out of the raw
        String saved in class constructor.
        Example: 'Hello, my name is TucanBot.'
        Variables:
            none
        """
        tmp = self.rawString.split(":", 2)
        if(len(tmp) == 3):
            return tmp[2]
        else:
            return ""
    
    def metaDataSplit(self):
        """ metaDataSplit
        This method is responsible for getting metadata from the recived string.
        Metadata = username, channel, commandtype, etc
        Example: 'crasbe!~crasbe@p5B3CF667.dip0.t-ipconnect.de PRIVMSG #test'
        Variables:
            none
        """
        tmp = self.rawString.split((":"))
        if (len(tmp) >= 2):
            return tmp[1].rstrip()
        else:
            return ""
    
    def usernameSplit(self):
        """ messageSplit:
        This method returns the username of the recived string.
        Example: 'TucanBot'
        Variables:
            none
        """
        return self.metaDataSplit().split("!")[0]

    def channelSplit(self):
        """ messageSplit:
        This method returns the channel from the recived string.
        Example: '#tucanbottestchannel' OR for queries 'crasbe'
        Variables:
            none
        """
        tmp = self.metaDataSplit().split(" ")
        if (len(tmp) >= 3):
            return tmp[2]
        else:
            return ""
    
    def receivedCommandSplit(self):
        """ receivedCommandSplit:
        This method is responsible for getting the IRC command, used by sender
        out of the raw string saved in class constructor.
        Example: 'PRIVMSG', 'KICK', 'NOTICE'
        Variables:
            none
        """
        tmp = self.metaDataSplit().split(" ")
        if (len(tmp) >= 2):
            return tmp[1]
        else:
            return ""
    
    def commandSplit(self):
        """ commandSplit:
        This method is responsible for splitting the message into a valid
        command so a plugin can be loaded.
        Example: '!ping'
        Variables:
            none
        """
        if(self.receivedCommandSplit() == "PRIVMSG"):
            return self.messageSplit().split(" ")[0].strip().lower()
        else:
            return ""