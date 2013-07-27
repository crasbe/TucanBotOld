class Plugin:
    """ Plugin-Class:
    This class is the mother-class for every plugin.
    Variables:
        none
    """

    def __init__(self):
        """ __init__:
        Sets the class attributes.
        Nothing fancy here.
        Class-Attributes:
            self.__channel  - channel name where command was sent   - type: str
            self.__username - user who sent command                 - type: str
            self.__message  - message user sent (including command) - type: str
            self.plugins    - list with plugins available in this class
                - type: str
        """

        self.channel = str()
        self.username = str()
        self.message = str()
        self.command = str()
        self.receiver = str()
        self.plugins = dict()

    def execute(self, command, channel, username, message):
        """ execute:
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
        self.receiver = message.replace(self.command, "").strip()
        if(self.receiver == ""):
            self.receiver = self.username
        return self.plugins[command]()
    
class Food(Plugin):
    def __init__(self):
        Plugin.__init__(self)
        
        self.plugins.update({"!keks"   : self.cookie})
    
    def cookie(self):
        return "\001ACTION gibt "+self.receiver+" einen Keks.\001"
        
if(__name__ == "__main__"):
    foodObj = Food()
    print(foodObj.execute("!keks", "#asdf", "crasbe", ""))