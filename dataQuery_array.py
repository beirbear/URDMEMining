import json
import numpy as ns

SPECIAL_FILES =["008003b6-eeb4-11e4-950a-fa163ec79faa.json", \
                "0514b638-eebe-11e4-a227-fa163e31af10.json", \
                "06ce89a4-eebe-11e4-92aa-fa163e31af10.json", \
                "07c70362-eec4-11e4-afb3-fa163e6b3411.json", \
                "08226720-eec9-11e4-81a2-fa163ec14db7.json", \
                "0910c254-eec3-11e4-9c32-fa163e31af10.json", \
                "09de8e82-eebe-11e4-a227-fa163e31af10.json", \
                "0a19a9d6-eec3-11e4-a02f-fa163e909903.json", \
                "0c8725da-eec4-11e4-a535-fa163e6b3411.json", \
                "0dc95fc2-eeaf-11e4-9c30-fa163ee26b1e.json", \
                "0e0572d2-eec3-11e4-ad13-fa163e25d342.json", \
                "0e05c858-eec9-11e4-b2ea-fa163ec14db7.json", \
                "0f293a5e-eeb9-11e4-9478-fa163e6b3411.json", \
                "10691a56-eebe-11e4-92aa-fa163e31af10.json", \
                "16da3d38-eec9-11e4-81a2-fa163ec14db7.json", \
                "16f7dc72-eebe-11e4-97e7-fa163e8e101a.json", \
                "188b6446-eeb4-11e4-a1f0-fa163e8e101a.json", \
                "18b22054-eeaf-11e4-9c30-fa163ee26b1e.json", \
                "18eba860-eeb9-11e4-88db-fa163e909903.json", \
                "1a8695e0-eebe-11e4-b32e-fa163ee26b1e.json", \
                "1c68068c-eebe-11e4-97e7-fa163e8e101a.json", \
                "1c8082b6-eeaf-11e4-a463-fa163ec14db7.json", \
                "1cb9fa82-eeaf-11e4-9a18-fa163ec14db7.json", \
                "1e807a4e-eeb4-11e4-a4d8-fa163e909903.json", \
                "20b0e128-eeb4-11e4-9478-fa163e6b3411.json", \
                "219b4f0a-eeb0-11e4-ad13-fa163e25d342.json", \
                "2321c5ac-eec4-11e4-b32e-fa163ee26b1e.json", \
                "24365116-eeb9-11e4-a535-fa163e6b3411.json", \
                "268abf06-eeb9-11e4-afb3-fa163e6b3411.json", \
                "278d1f48-eeb4-11e4-9702-fa163ee3e607.json", \
                "27b2db52-eec3-11e4-a3dc-fa163e25d342.json", \
                "2990d7ac-eec4-11e4-b32e-fa163ee26b1e.json", \
                "2a69d47c-eeaf-11e4-a836-fa163ec14db7.json", \
                "2d504e6e-eec8-11e4-931a-fa163ee3e607.json", \
                "2f3c5a1a-eeaf-11e4-993a-fa163ec79faa.json", \
                "32070808-eeb9-11e4-a535-fa163e6b3411.json", \
                "33208926-eeb4-11e4-a1ef-fa163ec79faa.json", \
                "33971424-eec3-11e4-ae14-fa163e25d342.json", \
                "343cc64e-eeaf-11e4-9c30-fa163ee26b1e.json", \
                "34b574c2-eebe-11e4-9a18-fa163ec14db7.json", \
                "3582b680-eeb4-11e4-8bc1-fa163e31af10.json", \
                "37c6baea-eeb4-11e4-9478-fa163e6b3411.json", \
                "399ba628-eebe-11e4-a937-fa163e6b3411.json", \
                "3a549340-eeaf-11e4-85a6-fa163ec79faa.json", \
                "3a948b9e-eeb4-11e4-808a-fa163e8e101a.json", \
                "3baba9f4-eeb4-11e4-8bc1-fa163e31af10.json", \
                "3e87e5ba-eec4-11e4-b32e-fa163ee26b1e.json", \
                "4353f476-eec4-11e4-b32e-fa163ee26b1e.json", \
                "43b6a072-eec8-11e4-92aa-fa163e31af10.json", \
                "45ef3976-eeaf-11e4-bb63-fa163ee3e607.json", \
                "46b4cdf8-eeb9-11e4-b32e-fa163ee26b1e.json", \
                "470cc96e-eeb8-11e4-adc1-fa163ec79faa.json", \
                "4781119c-eeaf-11e4-afb3-fa163e6b3411.json", \
                "4804b858-eeaf-11e4-abf8-fa163e6b3411.json", \
                "48527b74-eeaf-11e4-88db-fa163e909903.json", \
                "4a8985a4-eec3-11e4-8054-fa163e31af10.json", \
                "4da79514-eeaf-11e4-b32e-fa163ee26b1e.json", \
                "4dd095d6-eeaf-11e4-a836-fa163ec14db7.json", \
                "4e1c6b00-eeb4-11e4-b06d-fa163e909903.json", \
                "4e5aa870-eec8-11e4-837c-fa163e909903.json" ]


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
                # print("Extracting object %s" % data['URDMEModel'])
                _dataOutput = []
                _winPos = -1
                for j in range(len(_dataSeries)):
                    #if _dataSeries[j][INTERESTED_PARAMETER] > 400:
                    #    print("%s contains %s"% (data['URDMEModel'],_dataSeries[j][INTERESTED_PARAMETER]))
                    #    break     
                    _dataOutput.append(_dataSeries[j][INTERESTED_PARAMETER])
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
                    _dataOutput.append(_dataSeries[j][INTERESTED_PARAMETER])
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
                    _dataOutput.append(_dataSeries[j][INTERESTED_PARAMETER])
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
                    _dataOutput.append(_dataSeries[j][INTERESTED_PARAMETER])
                    if _winPos < _dataSeries[j]['start_pos']:
                        _pos = _dataSeries[j]['start_pos']
                    else:
                        print("Window Position Error")
                        quit()
                poLists.append(_dataOutput)


if __name__ == "__main__":
    # Initiate List Value
    initiateList()
    # modelObjects = SPECIAL_FILES
    # Get data from the file
    getAllData()
    
    # Write data series out
    f = open('proteinSeriesAll.txt','w')
    f.write(str(proteinLists))
    f.close() 

   # Write data series out
    f = open('mRNASeriesAll.txt','w')
    f.write(str(mRNALists))
    f.close()

   # Write data series out
    f = open('pfSeriesAll.txt','w')
    f.write(str(pfLists))
    f.close()

   # Write data series out
    f = open('poSeriesAll.txt','w')
    f.write(str(poLists))
    f.close()
    
