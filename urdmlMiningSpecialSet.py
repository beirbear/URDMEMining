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
from appConfig import *
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

def createSpecialTransaction(windowRange=None):

    if windowRange is None:
        print("Get every window frame")

  
    # Get required data
    range_k1 = getRateBin("k1")
    range_k2 = getRateBin("k2")
    range_alpha_p = getRateBin("alpha_p")
    range_mu_m = getRateBin("mu_m")
    range_mu_p = getRateBin("mu_p")
    print("Get rate band complete")

    #Get specie band
    range_pf = getSpecieBin("pf")
    range_po = getSpecieBin("po")
    range_mRNA = getSpecieBin("mRNA")
    range_protein = getSpecieBin("protein")
    print("Get specie band complete")


    tmpTransaction = []
    counter = 0
    # Loop throught every file to create a databand
    
    for file in SPECIAL_FILES:
        with open(INPUT_PATH + file) as fileReader:
            data = json.loads(fileReader.read())
            record = []
            counter += 1
            #if counter == 5:
            #    break
            # Loop for specie type
            sWord = ""
            for sType in RATE_TYPE:
                if sType == "k1":
                    genericRange = range_k1
                elif sType == "k2":
                    genericRange = range_k2
                elif sType == "alpha_p":
                    genericRange = range_alpha_p
                elif sType == "mu_m":
                    genericRange = range_mu_m
                elif sType == "mu_p":
                    genericRange = range_mu_p
                else:
                    print("Range Error")
                    quit()

                sn = float(data[sType])
                if sn < genericRange[1]:
                    record.append(sType + "_B0")
                elif sn < genericRange[2]:
                    record.append(sType + "_B1")
                elif sn < genericRange[3]:
                    record.append(sType + "_B2")
                elif sn < genericRange[4]:
                    record.append(sType + "_B3")
                elif sn < genericRange[5]:
                    record.append(sType + "_B4")
                elif sn < genericRange[6]:
                    record.append(sType + "_B5")
                elif sn < genericRange[7]:
                    record.append(sType + "_B6")
                elif sn < genericRange[8]:
                    record.append(sType + "_B7")
                elif sn <= genericRange[9]:
                    record.append(sType + "_B8")
                else:
                    print(sn)
                    print(genericRange)
                    print("Split Band Error")
                    quit()


            sWord = ""
            for sType in [ "pf", "po", "mRNA", "protein" ]:
                sWord = sType
                if sType == "pf":
                    genericRange = range_pf
                    sWord = "Pf"
                elif sType == "po":
                    genericRange = range_po
                    sWord = "Po"
                elif sType == "mRNA":
                    genericRange = range_mRNA
                elif sType == "protein":
                    genericRange = range_protein
                else:
                    print("Range Error")
                    quit()

                # Loop for time series
                sTime = data['data_' +  sWord]
                specieCounter = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                if windowRange is None:
                    for i in range(len(sTime)):
                        if sTime[i][CONTROL_PARAM] < genericRange[1]:
                            record.append(sWord + "_B0_F" + str(i))
                            specieCounter[0] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[2]:
                            record.append(sWord + "_B1_F" + str(i))
                            specieCounter[1] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[3]:
                            record.append(sWord + "_B2_F" + str(i))
                            specieCounter[2] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[4]:
                            record.append(sWord + "_B3_F" + str(i))
                            specieCounter[3] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[5]:
                            record.append(sWord + "_B4_F" + str(i))
                            specieCounter[4] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[6]:
                            record.append(sWord + "_B5_F" + str(i))
                            specieCounter[5] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[7]:
                            record.append(sWord + "_B6_F" + str(i))
                            specieCounter[6] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[8]:
                            record.append(sWord + "_B7_F" + str(i))
                            specieCounter[7] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] <= genericRange[9]:
                            record.append(sWord + "_B8_F" + str(i))
                            specieCounter[8] += 1
                            continue
                        else:
                            print("Split Band Error")
                            print(sType)
                            print(genericRange)
                            print(sTime[i][CONTROL_PARAM])
                            quit()
                else:
                    for i in windowRange:                            
                        if sTime[i][CONTROL_PARAM] < genericRange[1]:
                            record.append(sWord + "_B0_F" + str(i))
                            specieCounter[0] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[2]:
                            record.append(sWord + "_B1_F" + str(i))
                            specieCounter[1] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[3]:
                            record.append(sWord + "_B2_F" + str(i))
                            specieCounter[2] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[4]:
                            record.append(sWord + "_B3_F" + str(i))
                            specieCounter[3] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[5]:
                            record.append(sWord + "_B4_F" + str(i))
                            specieCounter[4] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[6]:
                            record.append(sWord + "_B5_F" + str(i))
                            specieCounter[5] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[7]:
                            record.append(sWord + "_B6_F" + str(i))
                            specieCounter[6] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] < genericRange[8]:
                            record.append(sWord + "_B7_F" + str(i))
                            specieCounter[7] += 1
                            continue
                        elif sTime[i][CONTROL_PARAM] <= genericRange[9]:
                            record.append(sWord + "_B8_F" + str(i))
                            specieCounter[8] += 1
                            continue
                        else:
                            print("Split Band Error")
                            print(sType)
                            print(genericRange)
                            print(sTime[i][CONTROL_PARAM])
                            quit()
                #if specieCounter[8] > 0:
                #    print("Band 8 found!!!")
                #    quit()
                    #print("Specie frequency: %s" % str(specieCounter))

            tmpTransaction.append(tuple(record))
    return tuple(tmpTransaction)


    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: urdmeMiningSpecialSet <minSupport>", file=sys.stderr)
        exit(-1)

    MIN_SUPPORT = int(sys.argv[1])

    windowGroup = []
    windowGroup.append(createSpecialTransaction())
    #print(windowGroup)
    #quit()
    sc = SparkContext( appName="urdmeMiningSpecialSet",  master=os.environ['MASTER'])
    
    rddWindows = sc.parallelize(windowGroup)

    result = rddWindows.map(frequentSet).reduceByKey(mergeResult).collect()

    print(result)
    sc.stop()
