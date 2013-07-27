"""
Created: 19.07.2013
Last modified: 19.07.2013

Author: crasbe
"""

import math

from classes.plugins import plugin

class Maths(plugin.Plugin):
    """
    classdocs
    """


    def __init__(self):
        """
        Constructor
        """
        plugin.Plugin.__init__(self)
        
        self.operators = ["+", "-", "*", "x", ":", "/", "^"]
        
        self.plugins.update({"!calc" : self.calculator})
        
    def calculator(self):
        return "{0}".format(self.parser(self.message.replace(self.command, "").strip()))
            
    def parser(self, lValue):
        lValue = str()
        if(lValue.count(",") > 0 or lValue.count(".") > 0):
            return "Floatpoint is not supported yet. Sorry."
        operator = str()
        count = int()
        for op in self.operators:
            if(type(lValue) == int):
                return lValue
            if(op in lValue):
                count += 1
                rValue = lValue.split(op)[1]
                lValue = lValue.split(op)[0]
                operator = op
        if(count > 1):
            return "Formulas are not supported yet. Sorry."
        if(operator == "+"):
            return int(lValue)+int(rValue)
        elif(operator == "-"):
            return int(lValue)-int(rValue)
        elif(operator == "*" or operator == "x"):
            return int(lValue)*int(rValue)
        elif(operator == ":" or operator == "/"):
            return int(lValue)/int(rValue)
        elif(operator == "^"):
            return int(lValue)**int(rValue)
        