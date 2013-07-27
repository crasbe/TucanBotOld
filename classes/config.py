"""
Created on 29.08.2010
Last edit on 17.07.2013

Author: crasbe
"""

import os
import sys
import configparser
from configparser import ExtendedInterpolation

class Config:
    """ Config-Class:
    This class reads the configuration-files.
    Variables:
        none
    """
    
    def __init__(self, path):
        """ __init__:
        Sets the configparser to the configurationfile.
        Nothing fancy here.
        Variables:
            See to the Class-Docstring.
        """
        if(not os.path.exists(path)):
            sys.exit("File not found: {0}".format(path))
        
        self.config = configparser.ConfigParser(interpolation=None)
        self.path = path

    def readSection(self, section):
        """ readSection:
        Reads the sections of the configurationfile and returns it as dict.
        Variables:
            section - contents the section to read - type: str
        """
        
        output = dict()
        with open(self.path, "r") as file:
            self.config.read_file(file)
        
        for key in self.config.options(section):
            output.update({key : self.config.get(section, key)})
        return output
    
    def read(self, section, key):
        with open(self.path, "r") as file:
            self.config.read_file(file)
            return self.config.get(section, key)
    
    def writeSection(self, section, inputDict):
        """ writeSection:
        """
        with open(self.path, "r") as file:
            self.config.read_file(file)
        
        if(not self.config.has_section(section)):
            self.config.add_section(section)
            
        for key in list(inputDict.keys()):
            self.config[section][key] = inputDict[key]
               
        with open(self.path, "w+") as file:
            self.config.write(file, False)
        
    def write(self, section, key, value):
        with open(self.path, "r") as file:
            self.config.read_file(file)
            
        if(not self.config.has_section(section)):
            self.config.add_section(section)
                
        self.config[section][key] = value
        
        with open(self.path, "w+") as file:
            self.config.write(file, False)
            
    def hasSection(self, section):
        with open(self.path, "r") as file:
            self.config.read_file(file)
        return self.config.has_section(section)
    
    def sections(self):
        with open(self.path, "r") as file:
            self.config.read_file(file)
        return self.config.sections()