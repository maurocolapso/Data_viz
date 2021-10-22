import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator

class Savitskyau(TransformerMixin, BaseEstimator):
    def __init__(self, value):
        self.value = value
    def message(self, X, y=None):
        print(self.value %'and'% X)
    def fit(self, X):
        return self
    def transform(self, X, y=None):
        X = self.value*X
        return X
