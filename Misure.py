import math
import numpy as np
#import pandas as pd 

class Misura ():
    "Classe per semplificare il calcolo del errore in fisica"
    def __init__ (self,valore,errore = 0):
        self.errore = errore
        self.valore = valore
    def __add__ (self,other):
        if type (other) is int or type (other) is float:
            other = Misura (other)
        assert type (other) is type (self)
        return Misura (self.valore+other.valore,self.errore+other.errore)
    def __sub__ (self,other):
        if type (other) is int or type (other) is float:
            other = Misura (other)
        assert type (other) is type (self)
        return Misura (self.valore-other.valore,self.errore+other.errore)
    def __str__ (self):
        return f"{self.valore} ± {self.errore}"
    def __mul__ (self,other):
        if type (other) is int or type (other) is float:
            other = Misura (other) 
        valore = self.valore*other.valore
        return Misura (valore,(self.relativo+other.relativo)*valore)
    def __truediv__ (self,other):
        if type (other) is int or type (other) is float:
            other = Misura (other)
        valore = self.valore/other.valore
        return Misura (valore,(self.relativo+other.relativo)*valore)
    #def __rtruediv__(self,other):
        #if type (other) is np.ndarray:
            #return np.array ([m for ])
    def __round__ (self,size):
        return Misura (round (self.valore,size),round(self.errore,6))
    @property
    def relativo (self):
        "errore relativo di una Misura"
        return self.errore/self.valore
    @property
    def percentuale (self):
        return self.relativo*100
    @property
    def radice (self):
        return Misura (math.sqrt(self.valore),self.relativo*2*math.sqrt(self.valore)    )
radice = lambda valore :np.array ([v.radice for v in valore])
arrotonda = lambda valori,size: np.array ([round(valore,size) for valore in valori])
percentuale = lambda valori: np.array ([v.percentuale for v in valori])