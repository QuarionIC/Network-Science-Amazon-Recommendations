# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:47:07 2023

@author: motqu
"""
import os
os.chdir("Folders\ISYE 4803 - NET\Project\Data Sets\Copurchasing Metadata") 

import os
#os.chdir("Folders\ISYE 4803 - NET\Project\Data Sets\Copurchasing Metadata") 

file = open("amazon-meta.txt",encoding="utf8")
file = file.readlines()
import re

products={}
customers={}
initialend=0
temp=[]
for i in range(len(file)):
    if "Id:" in file[i]:
        temp.append(file[initialend:i])
        initialend=i
reviews_name=["date",'customer', 'rating', 'votes', 'helpful']
print(len(temp))
for j in temp[450000:]:
    temp={}
    prod_reviews=[]
    for k in j:
        if "ASIN:" in k:
            asin=k.split()[1]
        if "title:" in k:
            temp["title"]=k[len("title:  "):-len("\n")].strip()
        if "group:" in k:
            temp["group"]=k[len("group:   "):-len("\n")].strip()
        if "salesrank:" in k:
            temp["salesrank"]=k[len("salesrank:  "):-len("\n")].strip()
        if "similar" in k:
            temp["similar"]=k.split()[2:]
        ##not sure how to approach categories
        date=[]
        date=re.findall(r"\d{4}-\d\d?-\d\d?",k)
        if date != []:
            review_values=k.split()[::2]
            review={}
            for j in range(5):
                review[reviews_name[j]]=review_values[j]
            prod_reviews.append(review)
            if review["customer"] not in customers:
                customers[review["customer"]]=[]
            customers[review["customer"]].append({"product":asin,"date":review["date"],"rating":review["rating"],"votes":review["votes"],"helpful":review["helpful"]})
    if prod_reviews!=[]:
        temp["reviews"]=prod_reviews
    if temp !={}:
        products[asin]=temp
