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
tupellist = set()
tupel= ()
tupel2 = ()
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
listoflists=list()
listoflista=list()
graph=np.empty([733,1])
for k in range(0,833):
         numb=format(k,'04')
         #print(numb)
         text_file = open ("data/Training_Data_Master/UTD-"+numb+".txt")
         trace = text_file.read()
         word_list = [int(i) for i in trace.split()]
         x=set()
         for word in word_list:
                   x.add(word)
         listoflists.insert(k,word_list)
print (len(listoflists))


for k in range(0,733):
         numba=format(k,'04')
         print (numba)
         text_filea = open ("data/Attack_Data/"+numba+".txt")
         tracea = text_filea.read()
         word_lista = [int(i) for i in tracea.split()]
         x=set()
         for word in word_lista:
                   x.add(word)
         listoflista.insert(k,word_lista)







for i in range (0,733):
     print(i)
     ratiodata=list()
     ratiol=list()
     val=listoflista[i]
     for p, val2 in enumerate(listoflists):
        #print(val)
        sm=difflib.SequenceMatcher(None,val,val2)
        #print(sm.ratio())
        ratiodata.insert(p,sm.ratio())
     ratiodata.sort()
     for h in range (0,3):
          ratiol.insert(h,ratiodata[len(ratiodata)-1-h])
     avg=np.mean(ratiol)
     print(ratiol)
     for o in range (len(graph[i])):
           if o==0:
                graph[i,o]=avg
     #print(ratiodata)
     ratiodata=[]
     ratiol=[]

df2 = pd.DataFrame(graph)
df2.to_csv(path+"similatac.csv", index=False, header=None)  
           
     
	              