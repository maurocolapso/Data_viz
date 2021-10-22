from sklearn.base import TransformerMixin, BaseEstimator
from scipy.signal import savgol_filter
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline


def trim(X, wavemin, wavemax):
    spectra_trim = X.loc[:, wavemin:wavemax]
    return spectra_trim


def savgol(spectra, window_length, poly_order, deriv_order):
    return savgol_filter(spectra, window_length, poly_order, deriv_order)


class TRIMMED(TransformerMixin, BaseEstimator):

    'This function cut the spectra bewteen two wavelenghts'

    def __init__(self, wavemin, wavemax):
        self.wavemin = wavemin
        self.wavemax = wavemax

    def fit(self, X):
        return self

    def transform(self, X):
        X = trim(X, wavemin=self.wavemin, wavemax=self.wavemax)
        return X


class SAVITZKYGOLAY(TransformerMixin, BaseEstimator):
    """
    high level support for doing this and that.
    """

    def __init__(self, window, poly, derivative):
        self.window = window
        self.poly = poly
        self.derivative = derivative

    def fit(self, X):
        return self

    def transform(self, X, y=None):
        X = savgol(spectra=X, window_length=self.window,
                   poly_order=self.poly, deriv_order=self.derivative)
        return X


# tests

df = pd.read_csv(
    '/Users/mauro/Documents/Data-Visualization/Data_viz/NIRS/Datasets/victory_test2.csv')
Trimmed_values = TRIMMED('1800', '600')
Xtrimmed = Trimmed_values.transform(df)

savitsky_values = SAVITZKYGOLAY(11, 2, 2)
X_salvit = savitsky_values.transform(Xtrimmed)
X_salvit
np.savetxt('/Users/mauro/Documents/Data-Visualization/Data_viz/NIRS/Datasets/victory_test5.csv',
           X_salvit, delimiter=",")
