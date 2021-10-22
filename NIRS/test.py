from inspect import Parameter
from Prepo import Savitskyau
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter

X=10

classes_tested = Prepo.Savitskyau(9)
ahora = classes_tested.transform(X)