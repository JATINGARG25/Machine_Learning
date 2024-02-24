import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()
print(diabetes.DESCR)