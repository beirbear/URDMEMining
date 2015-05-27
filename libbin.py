'''
Library for bin creation
'''
import sys
import json
import os.path
from os import listdir
from os.path import isfile, join
from appConfig import *

def getRateBin(rateType):
    # Check for rate bin file
    if not os.path.isfile(INPUT_RATE_BIN):
        print("Rate bin file does not exist in %s" % INPUT_RATE_BIN)
        quit()

    # Read bin file
    with open(INPUT_RATE_BIN) as fileReader:
        rateData = json.loads(fileReader.read())

    # Get rate index
    rateIndex = -1;
    for i in range(len(rateData)):
        if rateData[i]['rateType'] == rateType:
            rateIndex = i
            break

    # Check for rate band error
    if rateIndex == -1:
        print("Rate Type Error")
        quit()

    # return band data
    return rateData[rateIndex]['range']

	
def getSpecieBin(specieType):
    # Check for specie file
    if not os.path.isfile(INPUT_SPECIE_BIN):
        print("Specie bin file does not exist in %s" % INPUT_SPECIE_BIN)
        quit()

    # Read bin file
    with open(INPUT_SPECIE_BIN) as fileReader:
        binData = json.loads(fileReader.read())

    # Get rate index
    _max = _min = None
    _max = float(binData[specieType + '_max'])
    _min = float(binData[specieType + '_min'])

    # Check for rate band error
    if _max is None or _min is None:
        print("Specie type Error")
        quit()

    # Generate bin
    numStep = (_max - _min) / (SPECIE_BIN_NUMBER - 1)
    tmp = []
    for i in range(SPECIE_BIN_NUMBER):
        tmp.append(_min + (i * numStep))

    return tmp


def createTransaction(windowRange=None):
     
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
    
    if windowRange is None:
        print("Get every window frame")

    if not all(isinstance(item, int) for item in windowRange):
        print("Invalid windows range")
        quit()

    tmpTransaction = []
    # Get list of file
    onlyFiles = [ f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH,f))]
    counter = 0
    # Loop throught every file to create a databand
    for file in onlyFiles:
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

