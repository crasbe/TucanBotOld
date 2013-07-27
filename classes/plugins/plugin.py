"""
Created: 18.07.2013
Last modified: 19.07.2013

Author: crasbe
"""

class Plugin:
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
            self.channel  - channel name where command was sent   - type: str
            self.username - user who sent command                 - type: str
            self.message  - message user sent (including command) - type: str
            self.plugins    - list with plugins available in this class
                - type: str
        """

        self.channel  = str()
        self.message  = str()
        self.command  = str()
        self.receiver = str()
        self.username = str()
        self.plugins  = dict()

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
        self.channel = channel
        self.username = username
        self.message = message
        self.command = command
        self.receiver = message.replace(command, "").strip()
        if(self.receiver == ""):
            self.receiver = self.username
        return self.plugins[command]()
        # the launcher checks if the plugin to execute is in this class
        # -> no need for an extra test
    
    def __getattr__(self, pluginlist):
        """ __getattr__:
        This function returns a list of the plugins available.
        """
        return list(self.plugins.keys())