"""
Created: 19.07.2013
Last modified: 19.07.2013

Author: crasbe
"""

import random

import classes.plugins.plugin as plugin

class Haus(plugin.Plugin):
    """
    classdocs
    """


    def __init__(self):
        """
        Constructor
        """
        plugin.Plugin.__init__(self)
        
        self.plugins.update({"?haus" : self.haus, \
                             "?küche" : self.kueche, \
                             "?mikrowelle" : self.mikrowelle, \
                             "?backofen" : self.backofen, \
                             "!tv-gericht" : self.tvgericht, \
                             "!reste" : self.reste, \
                             "!popcorn" : self.popcorn, \
                             "!körnerkissen" : self.koernerkissen, \
                             "!keks" : self.cookie,
                             "!bier" : self.beer})
        
    def haus(self):
        pass
    
    def kueche(self):
        return "\001ACTION hat in seiner Küche: Mikrowelle, "+\
            "Backofen, Kühlschrank, Spülbecken.\001"
            
    def mikrowelle(self):
        return "\001ACTION hat in der Mikrowelle: TV-Gericht, "+\
            "Reste, Popcorn, Körnerkissen\001"
    
    def tvgericht(self):
        return "\001ACTION schiebt für "+self.receiver+" ein TV-Gericht "+\
            "in die Mikrowelle und wünscht guten Appetit!\001"       
    def reste(self):
        random.seed()
        source = ["vom großen Schlachtfest", "von gestern",
                  "vom Mittagessen", "von der Gartenparty", "vom Hackbraten",
                  "vom Nudelauflauf"]
        return "\001ACTION schiebt für "+self.receiver+" die Reste "+\
            source[random.randint(0, len(source)-1)]+" in die Mikrowelle. "+\
            "Guten Hunger!\001"
    def popcorn(self):
        return "\001ACTION legt für "+self.receiver+" eine Tüte "+\
            "Popcorn in die Mikrowelle. Schau wie es poppt!\001"
    def koernerkissen(self):
        return "\001ACTION legt für "+self.receiver+" das "+\
            "Körnerkissen in die Mikrowelle. Vorsicht, heiß!\001"

    
    def backofen(self):
        return "\001ACTION hat in seinem Backofen: Pizza, Flammkuchen, "+\
            "Hackbraten, Sonntagsbraten, Kekse\001"
    
    def cookie(self):
        return "\001ACTION gibt "+self.receiver+" einen Keks.\001"
    
    def kuehlschrank(self):
        pass
    
    def beer(self):
        return "\001ACTION gibt "+self.receiver+" ein Bier.\001"