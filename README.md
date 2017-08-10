# oneclassvm-adfa-ld
One Class SVM used on a Host Intrusion Benchmark Dataset ADFA LD 2013

We have 4 methods of dataconversion.
1. A transitiongraph based approach that is calculating the transistion probabilities and summarize it as average, variation and deviation value.
2. The same method but with a specific tuplelength (n)
3. A String similarity method
4. A semantic approach calculating the  occurences of every call and traces of length n (up to 5)

All programs are done with python. 

The example is showing the use of the OneClassSVM. First all dependencies must be installed: pip install -U scikit-learn,apt-get install python-numpy python-scipy. For Windows you have to install Scipy manually (http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy cd C:\Users\[user]\Downloads pip install scipy-0.18.1-cp35-cp35m-win_amd64.whl.). 

To train the model the svm is using two parameters:

clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(train_data)
	
kernel : radial basis function
Specifies the kernel type to be used in the algorithm. It must be one of ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ or a callable. 
nu : float, optional
An upper bound on the fraction of training errors and a lower bound of the fraction of support vectors. Should be in the interval (0, 1]. 
gamma : seperation sharpness

To execute the program either double click or start it with: "python oneclassvis.py"
It will display the calculation from the transitiongraph (method 1) with just avg and variation as features for good visualization.


For testing other .csv files, just run the proposed convertion programs (change path to the adfa ld datasets) and train the model on the newly generated .csv files.
