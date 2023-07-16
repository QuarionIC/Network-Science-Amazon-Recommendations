# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:47:07 2023

@author: motqu
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import itertools
from scipy.optimize import curve_fit
full=pd.read_csv("com-Amazon.csv", delimiter = " ")


unobserved=full.iloc[::5,:]
observed=full.iloc[full.index %5 !=0]
    



G = nx.from_pandas_edgelist(observed, source="From", target="To")
G1 =nx.from_pandas_edgelist(unobserved, source="From", target="To")


prediction = list(G1.edges())[1:5]  #test: we know these to be true
prediction.append((8,2)) #test: we know to be false

success=0
failure=0
for i in prediction:
  if i in list(G1.edges()):
    success+=1
  else:
    failure+=1

print("success rate:",success/(success+failure),"failure rate:", failure/(success+failure))
