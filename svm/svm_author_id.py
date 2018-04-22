#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC

clf = SVC(kernel='rbf',C=10000.)
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
t0 = time()
clf.fit(features_train,labels_train)
t1 = time()
print "training time:", round(t1-t0, 3), "s"
print "test length: "+str(len(features_test))
t2 = time()
pre = clf.predict(features_test)
t3 = time()
print "chris(1): "+str((pre.tolist()).count(1))
print "prediction time:", round(t3-t2, 3), "s"

score = clf.score(features_test,labels_test)

print score
#########################################################
