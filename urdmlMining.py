#!/usr/bin/env python

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
        #print("p: %s" % item)
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
        # print(item)
        for key in item:
            if validDependent(list(key)):
                filteredResult.append(item)

 
    return filteredResult
'''
def filterDependentVariable(input):
    resultSet = ()
    for key, value in input:
        if validDependent(key):
            resultSet.append((key,value))

    return resultSet
'''
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
        print("Usage: urdmeFrameDiscSweep <winSize> <minSupport>", file=sys.stderr)
        exit(-1)

    MIN_SUPPORT = int(sys.argv[2])

    windowGroup = []

    for i in range( int(WIN_SIZE/ 40.0 / int(sys.argv[1]))):
        # for development
        #if i >= 3:
        #    break

        windowGroup.append(createTransaction(np.arange(i * int(sys.argv[1]), i * int(sys.argv[1]) + int(sys.argv[1]) , 1)))
        print(np.arange(i * int(sys.argv[1]), i * int(sys.argv[1]) + int(sys.argv[1]) , 1))

    sc = SparkContext( appName="urdmeFrameDiscSweep",  master=os.environ['MASTER'])
    rddWindows = sc.parallelize(windowGroup)
    result = rddWindows.map(frequentSet).collect()
    # print(result)
    #tmp = result[0]
    #for item in result:
    #    print(set(list(tmp)))
    #    tmp = set(list(tmp)) & set(list(item))
    #print(len(result))
    #quit()
    # sortedResult = sorted(result[1].items(), key=operator.itemgetter(0))
    #print(sorted(list(result[0]), key=operator.itemgetter(1)))
    print(result)
    sc.stop()
    quit()
    # by pass the rest
    filteredResult = []
    for item in result:
        # print(item)
        for key in item:
            if validDependent(list(key)):
                filteredResult.append(item)
    print("resultSet: %s" % filteredResult)
    # Filter result
    #print(filterResult(result))    

    sc.stop()
