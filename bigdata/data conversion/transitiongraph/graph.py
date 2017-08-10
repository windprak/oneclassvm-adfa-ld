'''
uebergangsgraph

'''

# Imports
import itertools
import numpy as np  
import pandas as pd  
from sklearn import utils  
import matplotlib
from collections import Counter

# Test Data
path='/home/force/bigdata/data'



graphmatrix=np.empty([341,341])
for k in range(0,833):
         numb=format(k,'04')
         text_file = open ("data/Training_Data_Master/UTD-"+numb+".txt")
         trace = text_file.read()
         word_list = [int(i) for i in trace.split()]
         x=set()
         for word in word_list:
                   x.add(word)
         for i, val in enumerate(word_list):
             #print i, val
             nextelem= word_list[(i+1)%len(word_list)]
             #print i, nextelem
             graphmatrix[val,nextelem]+=1;
graph= graphmatrix.transpose()
for i in range(len(graph)):
        y = graph[i].sum() 
        quo=0
        if y != 0:
                quo= 1/y
        for j in range(len(graph[i])):
                prob=graph[i,j]*quo 
                print (prob)
                graph[i,j]=prob  
                
output=graph.transpose()

df2 = pd.DataFrame(output)
df2.to_csv(path+"graph.csv", index=False, header=None)   




