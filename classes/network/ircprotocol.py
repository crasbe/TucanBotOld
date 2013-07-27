"""
Created on 29.08.2010
Last edit on 18.07.2013

Written by dav1d.
Rewritten for python3 by crasbe.
"""

class IRCProtocol:
    """ IRCProtocol:
   
    This class is responsible for a _correct communication with the IRC-Server
    specified by RFC 1459. (Hopefully correct implemented.)
    Variables:
        socket - contains the socket of the connection to the server - 
            type: socket
    """
    
    def __init__(self, socket):
        """ __init__:
        __init__ is responsible for getting the socket for a direct communication
        with the server.
        Class-Attributes:
            self.socket - 
                contains the socket of the connectionto the IRC-Server - 
                type: socket
        """
        self.socket = socket
    
    def invite(self, nick, channel):
        """ invite:
        Invites nick to channel.
        Variables:
            nick    - contains the nickname of the user to invite - type: str
            channel - contains the name of the channel            - type: str
        """
        self.socket.send(bytes("INVITE {0} {1}\n".format(nick, channel), \
                                "utf8"))
        
    def join(self, channel):
        """ join:
        Joins into a channel.
        Variables:
            channel - contains the name of the channel - type: str
        """
        self.socket.send(bytes("JOIN {0}\n".format(channel), "utf8"))
        
    def kick(self, channel, nick, comment=""):
        """ kick:
        Kicks an user specified by his nickname with a specific comment from
        the channel.
        Variables:
            channel - contains the name of the channel      - type: str
            nick    - contains the nick of the user to kick - type: str
            comment - contains a reason for kicking         - type: str
        """
        self.socket.send(bytes("KICK {0} {1} :{2}".\
                               format(channel, nick, comment), "utf8"))
        
    def mode(self, channel, mode, user=""):
        """ mode:
        Sets channel- or usermodes.
        Variables:
            channel - contains the name of the channel - type: str
            mode    - contains the mode to set         - type: str
            user    - contains the user or channel     - type: str
        """
        self.socket.send(bytes("MODE {0} {1} {2}\n".format(channel, mode, \
                                                           user), "utf8"))
        
    def names(self, channel):
        """ names:
        Requests a list of all users, who are in the channel, specified by a
        variable.
        Variables:
            channel - contains the name of the channel - type: str
        """
        self.socket.send(bytes("NAMES {0}\n".format(channel), "utf8"))
        
    def nick(self, nick):
        """ nick:
        Sets the nickname of the bot / an user.
        Variables:
            nick - contains the new nick - type: str
        """
        self.socket.send(bytes("NICK {0}\n".format(nick), "utf8"))
    
    def notice(self, nick, text):
        """ notice:
        Sends a notice to somebody or something. Alternative to PRIVMSG.
        Variables:
            nick - contains the nick- or channelname - type: str
            text - contains the text to send         - type: str
        """
        self.socket.send(bytes("NOTICE {0} :{1}\n".format(nick, text), \
                               "utf8"))
        
    def part(self, channel, message=""):
        """ part:
        Leave a channel with a specified quit message. Default empty.
        Variables:
            channel  - contains the channel name  - type: str
            message  - contains the quitmessage   - type: str
        """
        self.socket.send(bytes("PART {0} {1}\n".format(channel, message), \
                               "utf8"))
        
    def pong(self, target):
        """ pong:
        Sends a PONG message (Answer to PING messages).
        Variables:
            target - contains the target to pong - type: str
        """
        self.socket.send(bytes("PONG :{0}\n".format(target), "utf8"))
        
    def privmsg(self, channel, text):
        """ privmsg:
        Sends a messange to somebody or something (for example a channel).
        Variables:
            channel - contains channel- or nickname - type: str
            text - contains the messange to send    - type: str
        """
        self.socket.send(bytes("PRIVMSG {0} :{1}\n".format(channel, text), \
                               "utf8"))
        
    def topic(self, channel, new_topic):
        """ topic:
        Sets the topic of a channel.
        Variables:
            channel   - contains the name of the channel - type: str
            new_topic - contains the new topic to set    - type: str
        """
        self.socket.send(bytes("TOPIC {0} :{1}".format(channel, new_topic), \
                            "utf8"))

    def user(self, ident, host, realname):
        """ user:
        I don't have any idea, what this does.
        Variables:
            ident    - contains the identification - type: str
            host     - contains the host           - type: str
            realname - contains the realname       - type: str
        """
        self.socket.send(bytes("USER {0} {1} euda :{2}\n".\
                               format(ident, host, realname), "utf8"))
        
    def whois(self, nick):
        """ whois:
        I don't have any idea, what this does.
        Variables:
            nick - contains the nick - type: str
        """
        self.socket.send(bytes("WHOIS {0}\n".format(nick), "utf8"))
        
    def whowas(self, nick, maximum="", server=""):
        """ whowas:
        I don't have any idea, what this does.
        Variables:
            nick   - contains the nick - type: str
            max    - ???               - type: str
            server - ???               - type: str
        """
        self.socket.send(bytes("WHOWAS {0} {1} {2}\n".format(nick, maximum, \
                                                             server), "utf8"))
    
    def quit(self, msg=""):
        """ quit:
        Quits the connection to the server.
        Variables:
            msg - contains the quitmessage - type: str
        """
        self.socket.send(bytes("QUIT :{0}\n".format(msg), "utf8"))