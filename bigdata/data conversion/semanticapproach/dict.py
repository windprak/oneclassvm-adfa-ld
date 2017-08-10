# Imports
import itertools
import numpy as np  
import pandas as pd  
from sklearn import utils  
import matplotlib
from collections import Counter
import difflib

# Test Data
path="C:\\Users\\bastel\\bigdata\\"
x=set()
wordset=set()
word=()
phrases=()
dicitionaryset=list()
dictionary=list()
phrase=list()
n2=4
phrase3=list()
graph=np.empty([833,5])

tupel1=()
for n in range (1,6):
    listzw=list()
    for k in range(0,833):
             numb=format(k,'04')
             text_file = open ("data/Training_Data_Master/UTD-"+numb+".txt")
             trace = text_file.read()
             word_list = [int(i) for i in trace.split()]
             x=set()
             for word in word_list:
                       x.add(word)
             for i in range (len(word_list)-(n-1)):
                        tupel5=()
                        for j in range (n):
                              nextelem= word_list[(i+j)%len(word_list)]  
                              tupel5 +=(nextelem,)
                        listzw.append(tupel5) 
    print(len(listzw))

    
    for k in range(0,833):
          numb=format(k,'04')
          print(numb)
          listdata=list()
          text_file = open ("data/Training_Data_Master/UTD-"+numb+".txt")
          trace = text_file.read()
          word_list = [int(i) for i in trace.split()]
          x=set()
          for i in range (len(word_list)-(n-1)):
                  tupel5=()
                  for j in range (n):
                           nextelem= word_list[(i+j)%len(word_list)]  
                           tupel5 +=(nextelem,)
                  listdata.append((1.0/len(listzw)*listzw.count(tupel5)))
                  #print((1.0/len(listzw)*listzw.count(tupel5)))
          avg=np.mean(listdata)
          std=np.mean(listdata)
          var=np.mean(listdata)
          graph[k,(n-1)]=avg
          print(avg)   
    #print(listdata)


df2 = pd.DataFrame(graph)
df2.to_csv(path+"zdiction.csv", index=False, header=None) 


               
     