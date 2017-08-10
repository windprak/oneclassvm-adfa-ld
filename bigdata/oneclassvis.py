'''
scikitlearn one class SVM
'''
print(__doc__)
# Imports
import numpy as np  
import pandas as pd  
from sklearn import svm  
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager
import collections
import csv 
xx, yy = np.meshgrid(np.linspace(-1, 2, 500), np.linspace(-1, 2, 500))
# Training Data
train_data = pd.read_csv('datatrain.csv', low_memory=False)
test_data=pd.read_csv('datatest.csv', low_memory=False)
attack_data=pd.read_csv('attackdata.csv', low_memory=False)
testres = np.array(test_data).astype("float")
result = np.array(train_data).astype("float")

clf = svm.OneClassSVM(nu=0.11, kernel="rbf", gamma=0.11)
clf.fit(train_data)

y_pred_train=clf.predict(train_data)
y_pred_test=clf.predict(test_data)
y_pred_attack=clf.predict(attack_data)
print ("Trainingssatz: ")
print (collections.Counter(y_pred_train))
print ("Testdatensatz: ")
print (collections.Counter(y_pred_test))
print ("attackdata: ")
print (collections.Counter(y_pred_attack))
n_error_train = y_pred_train[y_pred_train == -1].size

Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

print (result)
plt.title("Novelty Detection")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')
a, b = np.loadtxt('attackdata.txt', delimiter=',', unpack=True)
x, y = np.loadtxt('datatest.txt', delimiter=',', unpack=True)
z, w = np.loadtxt('datatrain.txt', delimiter=',', unpack=True)
plt.plot(x,y, 'bo')
plt.plot(z,w, 'go')
plt.plot(a,b, 'ro')
plt.axis([0, 2, 0, 2])
plt.show()