'''
testdatensatz
'''

# Imports
import itertools
import numpy as np  
import pandas as pd  
from sklearn import utils  
import matplotlib
from collections import Counter
import csv 

# Test Data
path='/home/force/bigdata/data'
reader = csv.reader(open('datagraph.csv', "rb"), delimiter=",")
x = list(reader)
result = np.array(x).astype("float")
print result

graph=np.empty([4372,2])
for k in range(0,4372):
         numb=format(k,'04')
         text_file = open ("data/Validation_Data_Master/UVD-"+numb+".txt")
         trace = text_file.read()
         word_list = [int(i) for i in trace.split()]
         x=set()
         probl= list()
         for word in word_list:
                   x.add(word)
         for i, val in enumerate(word_list):
             #print i, val
             nextelem= word_list[(i+1)%len(word_list)]
             #print i, nextelem
             probl.append(result[val,nextelem]);
         vari=np.var(probl)
         avg=np.mean(probl)
         std=np.std(probl)
         for j in range(len(graph[k])):
              if j == 0:
                  graph[k,j]=avg
              if j == 1:
                  graph[k,j]=std
              if j == 2:
                  graph[k,j]=std
        

df2 = pd.DataFrame(graph)
df2.to_csv(path+"datatest3.csv", index=False, header=None)   

