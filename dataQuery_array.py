import json
import numpy as ns

INPUT_FILE = "data/moldsParaExtracted.djson"
DATA_PATH = "data/dataMetaBands/"
INTERESTED_PARAMETER = "median"

# Global Variables
modelObjects = []
proteinLists = []
mRNALists = []
pfLists = []
poLists = []

# Function Definition
def initiateList():
    with open(INPUT_FILE) as _file:
        for line in _file:
            modelObjects.append(json.loads(line)['URDMEModel'])

def getAllData():
    for i in range(len(modelObjects)):
        with open(DATA_PATH + modelObjects[i] + ".json") as _file:
            for line in _file:
                data = json.loads(line)

                # extract protein list
                _dataSeries = data['data_protein']
                print("Extracting object %s" % data['URDMEModel'])
                _dataOutput = []
                _winPos = -1
                for j in range(len(_dataSeries)):
                    #if _dataSeries[j][INTERESTED_PARAMETER] > 500:
                    #    print(_dataSeries[j][INTERESTED_PARAMETER])
                    _dataOutput.append("[" + str(i) + "," + str(j) + "," + str(_dataSeries[j][INTERESTED_PARAMETER]) + "]")
                    if _winPos < _dataSeries[j]['start_pos']:
                        _pos = _dataSeries[j]['start_pos']
                    else:
                        print("Window Position Error")
                        quit()
                proteinLists.append(_dataOutput)

                # extract protein list
                _dataSeries = data['data_mRNA']
                _dataOutput = []
                _winPos = -1
                for j in range(len(_dataSeries)):
                    _dataOutput.append("[" + str(i) + "," + str(j) + "," + str(_dataSeries[j][INTERESTED_PARAMETER]) + "]")
                    if _winPos < _dataSeries[j]['start_pos']:
                        _pos = _dataSeries[j]['start_pos']
                    else:
                        print("Window Position Error")
                        quit()
                mRNALists.append(_dataOutput)

                # extract protein list
                _dataSeries = data['data_Pf']
                _dataOutput = []
                _winPos = -1
                for j in range(len(_dataSeries)):
                    _dataOutput.append("[" + str(i) + "," + str(j) + "," + str(_dataSeries[j][INTERESTED_PARAMETER]) + "]")
                    if _winPos < _dataSeries[j]['start_pos']:
                        _pos = _dataSeries[j]['start_pos']
                    else:
                        print("Window Position Error")
                        quit()
                pfLists.append(_dataOutput)

                # extract protein list
                _dataSeries = data['data_Po']
                _dataOutput = []
                _winPos = -1
                for j in range(len(_dataSeries)):
                    _dataOutput.append("[" + str(i) + "," + str(j) + "," + str(_dataSeries[j][INTERESTED_PARAMETER]) + "]")
                    if _winPos < _dataSeries[j]['start_pos']:
                        _pos = _dataSeries[j]['start_pos']
                    else:
                        print("Window Position Error")
                        quit()
                poLists.append(_dataOutput)


if __name__ == "__main__":
    # Initiate List Value
    initiateList()
    # Get data from the file
    getAllData()
    '''
    # Write data series out
    f = open('proteinSeries.txt','w')
    f.write(str(proteinLists))
    f.close() 

   # Write data series out
    f = open('mRNASeries.txt','w')
    f.write(str(mRNALists))
    f.close()

   # Write data series out
    f = open('pfSeries.txt','w')
    f.write(str(pfLists))
    f.close()

   # Write data series out
    f = open('poSeries.txt','w')
    f.write(str(poLists))
    f.close()
    '''
