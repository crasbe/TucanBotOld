"""
Created: 18.07.2013
Last modified: 18.07.2013

Author: crasbe
"""

import random

import classes.plugins.plugin as plugin

class QuestionAndAnswer(plugin.Plugin):
    """ QuestionAndAnswer:
    This class contains Q&A-like plugins with random results.
    Variables: 
        none
    """
    
    def __init__(self):
        """ __init__:
        The constructor executes the constructor of the parent
        and updates the list of plugins.
        Variables:
            self.plugins - from classes.plugins.plugin - type: dict
        """
        plugin.Plugin.__init__(self)
        self.plugins.update({"!ping"     : self.ping, \
                             "!pingpong" : self.pingpong, \
                             "!decide"   : self.decide, \
                             "!eightball": self.eightball, \
                             "!8ball"    : self.eightball})

    def ping(self):
        """ ping:
        This function returns 'Pong!'. Nothing fancy.
        Variables:
            none
        """
        return "Pong!"
    
    def pingpong(self):
        """ pingpong:
        This function returns 'Pongping!'. Nothing fancy.
        Variables:
            none
        """
        return "Pongping!"
    
    def decide(self):
        """ decide:
        This function returns a random answer. Three answers are
        possible. It can also decide between >=2 possibilities.
        Variables:
            none
        Classes:
            random
        """
        random.seed()
        if (" oder " in self.message):
            elemente = self.message.split("oder")
            return elemente[random.randint(0, len(elemente)-1)].\
                    strip().replace("!decide ", "")
        elif (" or " in self.message):
            elemente = self.message.split("or")
            return elemente[random.randint(0, len(elemente)-1)].\
                    strip().replace("!decide ", "")
        
        rand = random.randint(0, 2)
        if (rand == 0):
            return "Ja!"
        elif (rand == 1):
            return "Nein!"
        elif (rand == 2):
            return "Frag später noch mal nach."
        else:
            return "CORE FUCKUP!"

    def eightball(self):
        """ eightball:
        This function returns a random answer from a given anwerset.
        Classes:
            random
        """
        answers = [ 'Soweit ich sehe, ja.',
                    'Bestimmt.',
                    'Wurde so entschieden.',
                    'Ziemlich wahrscheinlich.',
                    'Sieht danach aus.',
                    'Alle Anzeichen weisen darauf hin.',
                    'Ohne jeden Zweifel.',
                    'Ja.',
                    'Ja - definitiv.',
                    'Darauf kannst du dich verlassen.',

                    'Keine genaue Antwort, probier es nochmals.',
                    'Frage nochmals.',
                    'Sage ich dir besser noch nicht.',
                    'Kann ich jetzt noch nicht sagen.',
                    'Konzentriere dich und frage erneut.',

                    'Würde mich nicht darauf verlassen.',
                    'Meine Antwort ist nein.',
                    'Meine Quellen sagen nein.',
                    'Sieht nicht so gut aus.',
                    'Sehr zweifelhaft.']
        random.seed()
        return answers[random.randint(0, len(answers)-1)]