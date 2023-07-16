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

counter=0
observed=[]
not_observed=[]
for i in full:
  if counter == 5:
    not_observed.append(i)
    counter= 0
  else:
    observed.append(i)
    counter+=1
    

df_edges = observed
G = nx.from_pandas_edgelist(df_edges, source="From", target="To")
