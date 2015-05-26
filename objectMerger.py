#!/usr/bin/env python
import sys
import json
import os.path
from pymining import itemmining
from os import listdir
from os.path import isfile, join
from jsonmerge import merge

INPUT_RATE_BIN = "/home/ubuntu/miniproject/data/rateBands.json"
INPUT_SPECIE_BIN = "/home/ubuntu/miniproject/data/speciesAmount.json"
INPUT_PATH = "/home/ubuntu/miniproject/data/dataBands/"
INPUT_META_DATA = "/home/ubuntu/miniproject/data/moldsParaExtracted.djson"
OUTPUT_PATH = "/home/ubuntu/miniproject/data/dataMetaBands/"

# Skip alpha_m and alpha_m_g because the values are not varied.
RATE_TYPE = ["k1","k2","alpha_p","mu_m", "mu_p"]
SPECIE_BIN_NUMBER = 10
CONTROL_PARAM = "median"
rateData = []
transaction = ()

#Functions
def mergeObjects():
    
    tmpTransaction = []
    # Get list of file
    onlyFiles = [ f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH,f))]
    objNum = 0
    runner = 0
    # Loop throught every file to create a databand
    for file in onlyFiles:
        with open(INPUT_PATH + file) as fileReader:
            data = json.loads(fileReader.read())
            print("dataModel: %s" % data['URDMEModel'])
            with open(INPUT_META_DATA) as metaReader:
                lines = metaReader.readlines()
                for line in lines:
                    lineData = json.loads(line)
                    runner += 1
                    # print("matching %s : %s \t%d" % (data['URDMEModel'], lineData['URDMEModel'], runner))
                    if lineData['URDMEModel'] == data['URDMEModel']:
                        objNum += 1
                        print("%d\t%d\tMerging %s" % (objNum, runner, data['URDMEModel']))
                        result = merge(data,lineData)
                        f = open(OUTPUT_PATH + data['URDMEModel'] + ".json" ,'w')
                        f.write(json.dumps(result))
                        f.close()
                        break 
        fileReader.close()
        runner = 0


mergeObjects()
