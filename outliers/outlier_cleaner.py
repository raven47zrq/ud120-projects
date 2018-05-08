#!/usr/bin/python

import math

def getKey(item):
    return item[2]

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    #print predictions
    cleaned_data = []

    ### your code goes here
    for i in range(0,len(ages)):
        cleaned_data.append((ages[i],net_worths[i],abs(net_worths[i]-predictions[i])))
    cleaned_data.sort(key=getKey,reverse=True)
    outliers = math.ceil(len(cleaned_data)*0.1)
    #print "outliers: "+str(math.ceil(outliers))
    cleaned_data = cleaned_data[int(outliers):]

    return cleaned_data
