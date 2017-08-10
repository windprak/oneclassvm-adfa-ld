# Imports
import itertools
import numpy as np  
import pandas as pd  
from sklearn import utils  
import matplotlib
from collections import Counter


# Test Data
path="C:\\Users\\bastel\\bigdata\\"
tupellist = set()
tupel= ()
tupel2 = ()
#n = tupellaenge 
n=5
c=0


tupeler= ()
tupeler2= ()
n2=5
c2=0
tupel5= ()
tupel6= ()
tupelv=()
tupeldlist= list()
tupel7= ()
lister= list()
knotenlist=list()
listzw= list()
lclear= list()

for k in range(0,833):
         numb=format(k,'04')
         text_file = open ("data/Training_Data_Master/UTD-"+numb+".txt")
         trace = text_file.read()
         word_list = [int(i) for i in trace.split()]
         x=set()
         for word in word_list:
                   x.add(word)
         for i in range (len(word_list)-(n2-1)):
                    for j in range (n2):
                          nextelem= word_list[(i+j)%len(word_list)]  
                          tupel5 +=(nextelem,)
                    listzw.append(tupel5)
                    tupel5=tupel7
                    tupel6=tupel7
                    c=0   
         print (len(listzw)) 
         for v in range (len(listzw)-(n2)):
               val=listzw[(v)%len(listzw)]
               nexter = listzw[(len(listzw)-(len(listzw)-(v+(n2))))%len(listzw)]
               tupelv = val+nexter
               knot="Tuple: {}".format(val)
               testerr="Tuple: {}".format(tupelv)
               print (testerr)
               knotenlist.append(knot)
               tupeldlist.append(testerr)
         listzw=[]

resultpoints=list()
resultluster=list()
#print (tupeldlist)
touplerr=()
listgr= list()
resultlist= list()


graph=np.empty([833,3])
for k in range(0,833):
         numb=format(k,'04')
         print (numb)
         text_file = open ("data/Training_Data_Master/UTD-"+numb+".txt")
         trace = text_file.read()
         word_list = [int(i) for i in trace.split()]
         x=set()
         for word in word_list:
                   x.add(word)
         for i in range (len(word_list)-(n2-1)):
                    for j in range (n2):
                          nextelem= word_list[(i+j)%len(word_list)]  
                          tupel5 +=(nextelem,)
                    listgr.append(tupel5)
                    tupel5=tupel7
                    tupel6=tupel7
                    c=0   
         for v in range (len(listgr)-(n2)):
               val=listgr[(v)%len(listgr)]
               nexter =listgr[(len(listgr)-(len(listgr)-(v+(n2))))%len(listgr)]
               touplerr=val+nexter
               knoten="Tuple: {}".format(val)
               testerrr="Tuple: {}".format(touplerr)
               #print(knotenlist.count(knoten))
               #print (tupeldlist.count(testerrr))
               res= 1/knotenlist.count(knoten)
               ress= res*tupeldlist.count(testerr)
               resultluster.append(ress)
         #print (resultluster)
         avg=np.mean(resultluster)
         std2=np.std(resultluster)
         print("standardt: ")
         print(std2)
         print("mean: ")
         print(avg)
         vari=np.var(resultluster)
         for j in range(len(graph[k])):
               if j==0:
                  graph[k,j]=avg
               if j==1:
                  graph[k,j]=std2
               if j==2:
                  graph[k,j]=vari
         resultluster=[]
         touplerr=tupel7
         listgr=[]
			
df2 = pd.DataFrame(graph)
df2.to_csv(path+"train3.csv", index=False, header=None)   	              