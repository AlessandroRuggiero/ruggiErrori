import pandas as pd
import numpy as np
from ruggiErrori.Misure import Misura
def carica_tabella (name):
    return pd.read_excel(name)
def prepara_tabella (tabella,struttura):
    df = pd.DataFrame()
    for nome , (valore,errore) in struttura:
        if type (errore) is float:
            df [nome] = np.array ([
                    Misura (n,errore) for n in tabella [valore]
            ])
        else :
            df[nome] = np.array ([
                Misura(tabella[valore][i],tabella[errore][i])  for i in range (len (tabella[valore]))
            ])
    return df