import pandas as pd
import numpy as np
from sklearn.base import TransformerMixin, BaseEstimator

df = pd.read_csv("/Users/mauro/Documents/Data Visualization/Data_viz/NIRS/NIRS_dataset.csv",header=0)
df.head()
y = df['Species']
X = df.iloc[:,1:]

def trim(X,wavemin,wavemax):
    spectra_trim = X.loc[:,wavemin:wavemax]
    return spectra_trim 

class TRIMMED(TransformerMixin,BaseEstimator):
    
    'This function cut the spectra bewteen two wavelenghts'

    def __init__(self,wavemin, wavemax):
        self.wavemin=wavemin
        self.wavemax=wavemax
    def fit(self, X):
        return self

    def transform(self, X):
        X = trim(X,wavemin=self.wavemin,wavemax=self.wavemax)
        return X

# t = TRIMMED('9.50E+02','9.76E+02')
# t.transform(X)

class DROP_COLS(TransformerMixin,BaseEstimator):
    def __init__(self,columnnames):
        self.columnames=columnnames
    def fit(self,X):
        return self
    def transform(self,dataset)
        
