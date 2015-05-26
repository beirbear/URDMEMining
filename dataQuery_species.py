#!/usr/bin/env python

import sys
import json
import numpy as ns
from os import listdir
from os.path import isfile, join

INPUT_PATH = "/home/ubuntu/miniproject/data/dataBands/"
VALID_NUMBER = 10000
INTERESTED_PARAM = 'median'

if __name__ == "__main__":

    # Get all files
    onlyFiles = [ f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH,f))]

    validNumber = 0
    for eachFile in onlyFiles:
        # Load data into the list
        with open(INPUT_PATH + eachFile) as _file:
            for line in _file:
                data = json.loads(line)
                
                # Check for validity
                if data['URDMEModel'] + ".json" == eachFile:
                    validNumber += 1

    if validNumber != VALID_NUMBER:
        print("Every files is not valid! %d" % validNumber)
        quit()

    pf_max = po_max = mRNA_max = protein_max = sys.float_info.min
    pf_min = po_min = mRNA_min = protein_min = sys.float_info.max
    round = 0
    for eachFile in onlyFiles:
        # Load data into the list
        with open(INPUT_PATH + eachFile) as _file:
            for line in _file:
                data = json.loads(line)
        
                # Get intersted value from and measure for max and min in every time frame
                dataRange = data['data_Po']
                for i in range(100):
                    if float(dataRange[i][INTERESTED_PARAM]) > po_max:
                        po_max = float(dataRange[i][INTERESTED_PARAM])
                    if float(dataRange[i][INTERESTED_PARAM]) < po_min:
                        po_min = float(dataRange[i][INTERESTED_PARAM])
                    round += 1

                dataRange = data['data_Pf']
                for i in range(100):
                    if float(dataRange[i][INTERESTED_PARAM]) > pf_max:
                        pf_max = float(dataRange[i][INTERESTED_PARAM])
                    if float(dataRange[i][INTERESTED_PARAM]) < pf_min:
                        pf_min = float(dataRange[i][INTERESTED_PARAM])

                dataRange = data['data_mRNA']
                for i in range(100):
                     if float(dataRange[i][INTERESTED_PARAM]) > mRNA_max:
                        mRNA_max = float(dataRange[i][INTERESTED_PARAM])
                     if float(dataRange[i][INTERESTED_PARAM]) < mRNA_min:
                        mRNA_min = float(dataRange[i][INTERESTED_PARAM])

                dataRange = data['data_protein']
                for i in range(100):
                    if float(dataRange[i][INTERESTED_PARAM]) > protein_max:
                        protein_max = float(dataRange[i][INTERESTED_PARAM])
                    if float(dataRange[i][INTERESTED_PARAM]) < protein_min:
                        protein_min = float(dataRange[i][INTERESTED_PARAM])

                break
    print("{ "),
    print("\"pf_max\": %f, \"pf_min\": %f," % (pf_max,pf_min)),
    print("\"po_max\": %f, \"po_min\": %f," % (po_max,po_min)),
    print("\"mRNA_max\": %f, \"mRNA_min\": %f," % (mRNA_max,mRNA_min)),
    print("\"protein_max\": %f, \"protein_min\": %f }" % (protein_max,protein_min))    

    quit()

