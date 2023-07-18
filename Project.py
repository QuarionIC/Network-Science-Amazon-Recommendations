# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:47:07 2023

@author: motqu
"""
import os
#os.chdir("Folders\ISYE 4803 - NET\Project\Data Sets\Copurchasing Metadata") 

file = open("amazon-meta.txt",encoding="utf8")
file = file.readlines()

import re

products={}
customers={}
initialend=0
temp=[]
for i in range(len(file)):     #this loop seperates different products
    if "Id:" in file[i]:
        temp.append(file[initialend:i])
        initialend=i


customers={} #dictionary of customers and all products they have reviewed in given category
products={} #dictionary of products and salesrank in given category, with 50+ reviews        possibly useful to see if sales rank alligns with one of the node ranking methods
for j in temp:
    try:
        category_count=int(j[6].split()[1])  #index of line w category count
        review_start_index=category_count+7  #index of line w reviews summary
        for m in j[7:review_start_index]:
            b=re.findall(r"\|(\D+?)\[",m)    #remove | and numbers from categories, splits into list organized by broadest>specific


            #specify category here
            if b[0]=="Books" and b[2]=="Nonfiction":                                 #edge count: 408275 node count: 1205 | avg clustering takes 1m to compute
            #if b[0]=="Books" and b[2]=='Literature & Fiction':                      #edge count: 9090607 node count: 5024 | avg clustering takes 10m+
            #if b[0]=="Books" and b[2]=='History':                                    #edge count: 229027 node count: 843| avg clustering takes 30s
            #if b[0]=="Books" and b[2]=="Science Fiction & Fantasy":                  #edge count: 1282164 node count: 1811| avg clustering takes 11m to calculate
                if int(j[review_start_index].split()[2])>=50:     #disqualifies products with less than 5 reviews
                    asin=j[1].split()[1]
                    salesrank=j[4].split()[1]
                    products[asin]=salesrank
                    for t in j[review_start_index+1:]:      #iterates through all reviews to get customer id
                        customer=t.split()[2]
                        if customer not in customers:         
                            customers[customer]=[]
                        if asin not in customers[customer]:     #customers reviewing same product multiple times?
                            customers[customer].append(asin)    #update dictionary of customer reviews 
    except:
        pass

print(len(customers.keys()))


import itertools

edges=[]
for c in customers:
    if len(customers[c])>1:
        for t in list(itertools.product(customers[c],customers[c])):    #all combinations of products a customer pruchases is and edge, excludes self loops
            if t[0]!=t[1]:
                edges.append(t)

import networkx as nx
g = nx.Graph()
g.add_edges_from(edges)
print("edge count:", len(g.edges()), "node count:", len(g.nodes()) )

print(nx.average_clustering(g))

