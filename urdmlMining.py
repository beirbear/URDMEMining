#!/usr/bin/env python
'''
Caution!!!!
When user run this code. They might face with a problem that SparkBuffer is not large enought to hold a sheer volume of data in this circumstance.

According to this, the developer introduce an alternative application name "urdmeMiningPartialWindows" which is locaed in the same folder of this application.

'''


from __future__ import print_function

import sys
import json
import os
import os.path
import operator
from pymining import itemmining
from os import listdir
from os.path import isfile, join
from libbin import *
from pyspark import SparkContext
import numpy as np

MIN_SUPPORT = 0
MIN_DEPENDENT_V = 2

def validDependent(input):
    validNumber = 0
    for item in input:
        if item in DEPENDENT_VARIABLE:
            validNumber += 1

    if validNumber >= MIN_DEPENDENT_V:
        return True
    # Python interpretter is not smart engouht to make a default return without else
    else:
        return False

def frequentSet(input):
    relim_input = itemmining.get_relim_input(input)
    report = itemmining.relim(relim_input, min_support=MIN_SUPPORT)

    return report
    # by pass filtering parameters
    filteredResult = []
    for item in report:
        for key in item:
            if validDependent(list(key)):
                filteredResult.append(item)

 
    return (0,filteredResult)

'''
# This function is used when we want to indicate the specific databand of the output
def filterDependentVariable(input):
    resultSet = ()
    for key, value in input:
        if validDependent(key):
            resultSet.append((key,value))

    return resultSet
'''

def mergeResult(input1,input2):
    return input1.entend(input2)

def filterResult(input):
    resultSet = ()
    for item in input:
        print(item)
        for key, value in item:
            if validDependent(key):
                resultSet.append((key,value))

    return resultSet

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: urdmeMining <winSize> <minSupport>", file=sys.stderr)
        exit(-1)

    MIN_SUPPORT = int(sys.argv[2])

    windowGroup = []

    for i in range( int(WIN_SIZE/ 40.0 / int(sys.argv[1]))):
        # for development, used when we want to limit the number of sample set
        # if i >= 3:
        #    break

        '''
Efficiency Note: The developer intend to program it easy which is trade off with the efficiency of the algorithm that need to go throught every file when the createTransaction() is called. This can be optimize, but the developer would like to point out and note to clarify why this step take certain amount of time. 
        '''
        windowGroup.append(createTransaction(np.arange(i * int(sys.argv[1]), i * int(sys.argv[1]) + int(sys.argv[1]) , 1)))
        print("Window Frame: %s" % np.arange(i * int(sys.argv[1]), i * int(sys.argv[1]) + int(sys.argv[1]) , 1))

    sc = SparkContext( appName="urdmeMining",  master=os.environ['MASTER'])

    rddWindows = sc.parallelize(windowGroup)

    result = rddWindows.map(frequentSet).reduceByKey(mergeResult).collect()

    print(result)
    sc.stop()
