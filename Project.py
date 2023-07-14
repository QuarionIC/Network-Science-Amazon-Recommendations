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

df_edges = pd.read_csv("com-Amazon.csv", delimiter = " ")
G = nx.from_pandas_edgelist(df_edges, source="From", target="To")