__author__ = 'michel'

from interaction031 import Interaction031
from experiment import Experiment

class Anticipation031():
    experience=None
    proclivity=0
    
    def __init__(self, experience, proclivity):
        self.experience = experience
        self.proclivity = proclivity
        
    def equals(self, otherProposition):
        return otherProposition.getExperience() == self.experience
    
    def getExperience(self):
        return self.experience
    
    def setExperience(self, experience):
        self.experience=experience
    
    def getProclivity(self):
        return self.proclivity
    
    def addProclivity(self, proclivity):
        self.proclivity += proclivity
        
    def compareTo(self):
        return self.getProclivity()
    
    def __repr__(self):
        return "{0} proclivity {1}".format(self.experience.getLabel(), self.proclivity)