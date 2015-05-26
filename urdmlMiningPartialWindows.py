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
START_WINDOW = -1
STOP_WINDOW = -1

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

def convertFrozenSetToJson(input):
    dataSingleObject = "["
    for item in input:
        resultKeys = item.keys()
        resultValues = item.values()
        resultData = "["
        for i in range(len(resultKeys)):
            resultData += "{ \"_key\" : \"" +  str(list(resultKeys[i])) + "\", \"_value\": " + str(resultValues[i]) + "}"
            if i < len(resultKeys) - 1:
                resultData += ","
        dataSingleObject += resultData + "],"
    return dataSingleObject[:-1] + "]"

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: urdmeMiningPartialWindow <winSize> <minSupport> <startRange:inclusion> <stopRange:exclusion>\nThe number of range can be 0 to 99 (Subject to metadata).", file=sys.stderr)
        exit(-1)

    print("\033[93m" + "NOTE: The division of \"(stopWindowPosition - startWindowPosition) / windowSize\" must contain no fraction. Otherwise, it will be ignore!" + "\033[0m")
    MIN_SUPPORT = int(sys.argv[2])
    START_WINDOW = int(sys.argv[3])
    STOP_WINDOW = int(sys.argv[4])
    WIN_SIZE = int(sys.argv[1])

    if STOP_WINDOW < START_WINDOW:
        print("Invalid wondow range!", file=sys.stderr)
        quit()

    windowGroup = []

    '''
Efficiency Note: The developer intend to program it easy which is trade off with the efficiency of the algorithm that need to go throught every file when the createTransaction() is called. This can be optimize, but the developer would like to point out and note to clarify why this step take certain amount of time. 
    '''
    for i in range( (STOP_WINDOW -  START_WINDOW) / WIN_SIZE ):
        
        windowGroup.append(createTransaction(range(i * WIN_SIZE + START_WINDOW, i * WIN_SIZE + START_WINDOW + WIN_SIZE)))
        print("Window Frame: %s" % range(i * WIN_SIZE + START_WINDOW, i * WIN_SIZE + START_WINDOW + WIN_SIZE))

    sc = SparkContext( appName="urdmeMining",  master=os.environ['MASTER'])

    rddWindows = sc.parallelize(windowGroup)
    '''
    Note: Cannot do reduceByKey. Might be something here. Will check later
    result = rddWindows.map(frequentSet).reduceByKey(mergeResult).collect()
    '''
    result = rddWindows.map(frequentSet).collect()

    outputData = convertFrozenSetToJson(result)

    print("\033[92m" + outputData + "\033[0m")

    
    outputFile = "output/urdmeMiningPartialWindow_" + str(WIN_SIZE) + "_" + str(MIN_SUPPORT) + "_" + str(STOP_WINDOW) + "_" + str(START_WINDOW) + ".json"
    f = open(outputFile,'w')
    f.write(json.dumps(outputData))
    f.close()
    print("Complete!!!")
    sc.stop()
