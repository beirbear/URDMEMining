#!/usr/bin/env python

import json
import numpy as ns

INPUT_FILE = "moldsParaExtracted.djson"

# Global Variables
k1 = list()
k2 = list()
alpha_m = list()
alpha_m_g = list()
alpha_p = list()
mu_m = list()
mu_p = list()

# Function Definition
def getDataBin(_list):
    sd = float(ns.std(_list))
    half_sd = float( sd / 2.0)
    avg = float(ns.average(_list))
    _max = max(_list)
    _min = min(_list)
    _bin = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    er = 0

    for data in _list:
        if data < avg - sd - sd:
            _bin[0] += 1
        elif data < avg - sd - half_sd:
            _bin[1] += 1
        elif data < avg - sd:
            _bin[2] += 1
        elif data < avg - half_sd:
            _bin[3] += 1
        elif data < avg:
            _bin[4] += 1
        elif data < avg + half_sd:
            _bin[5] += 1
        elif data < avg + sd:
            _bin[6] += 1
        elif data < avg + sd + half_sd:
            _bin[7] += 1
        elif data < avg + sd + sd:
            _bin[8] += 1
        elif data <= _max:
            _bin[9] += 1
        else:
            er += 1

    if er > 0:
        return ( False, _min, _max, avg, sd, _bin)

    return ( True, _min, _max, avg, sd, _bin)

# Function Definition
def exportDataBin(_list, _listName):
    sd = float(ns.std(_list))
    half_sd = float( sd / 2.0)
    avg = float(ns.average(_list))
    _max = max(_list)
    _min = min(_list)
    _bin = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    _binRange = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    er = 0

    for data in _list:
        if data < avg - sd - sd:
            _bin[0] += 1
        elif data < avg - sd - half_sd:
            _bin[1] += 1
        elif data < avg - sd:
            _bin[2] += 1
        elif data < avg - half_sd:
            _bin[3] += 1
        elif data < avg:
            _bin[4] += 1
        elif data < avg + half_sd:
            _bin[5] += 1
        elif data < avg + sd:
            _bin[6] += 1
        elif data < avg + sd + half_sd:
            _bin[7] += 1
        elif data < avg + sd + sd:
            _bin[8] += 1
        elif data <= _max:
            _bin[9] += 1
        else:
            er += 1

        if er > 0:
            print("Bin Error: %s" % _listName)
            quit()

    _binRange[0] = avg - sd - sd
    _binRange[1] = avg - sd - half_sd
    _binRange[2] = avg - sd
    _binRange[3] = avg - half_sd
    _binRange[4] = avg
    _binRange[5] = avg + half_sd
    _binRange[6] = avg + sd
    _binRange[7] = avg + sd + half_sd
    _binRange[8] = avg + sd + sd
    _binRange[9] = _max

    output = "{ \"rateType\": \"%s\"," % _listName
    output += "\"max\": %f," % _max
    output += "\"min\": %f," % _min
    output += "\"avg\": %f," % avg
    output += "\"sd\": %f," % sd
    output += "\"half_sd\": %f," % half_sd
    output += "\"distribution\": %s," %  _bin
    output += "\"range\": %s }" %  _binRange
    print(output),

def initiateList():
    with open(INPUT_FILE) as _file:
        for line in _file:
            data = json.loads(line)
            k1.append(float(data['k1']))
            k2.append(float(data['k2']))
            alpha_m.append(float(data['alpha_m']))
            alpha_m_g.append(float(data['alpha_m_g']))
            alpha_p.append(float(data['alpha_p']))
            mu_m.append(float(data['mu_m']))
            mu_p.append(float(data['mu_p']))

def getDataBand(rateType):
    (_, _min, _max, _avg, _sd, _bin) = getDataBin(rateType)
    if _ is False:
        print("Data Distribution Error")
        quit()

    print("bin distribution:\n %s" % (_bin))
    return (_avg, _sd, _max)

if __name__ == "__main__":
    # Initiate List Value
    initiateList()

    # Get data bin
    '''
    print("k1: "),
    getDataBand(k1)
    print("k2: "),
    getDataBand(k2)
    print("alpha_m: "),
    getDataBand(alpha_m)
    print("alpha_m_g: "),
    getDataBand(alpha_m_g)
    print("alpha_p: "),
    getDataBand(alpha_p)
    print("mu_m: "),
    getDataBand(mu_m)
    print("mu_p: "),
    getDataBand(mu_p)
    '''
    print("["),
    exportDataBin(k1,"k1")
    print(","),
    exportDataBin(k2,"k2")
    print(","),
    exportDataBin(alpha_m,"alpha_m")
    print(","),
    exportDataBin(alpha_m_g,"alpha_m_g")
    print(","),
    exportDataBin(alpha_p,"alpha_p")
    print(","),
    exportDataBin(mu_m,"mu_m")
    print(","),
    exportDataBin(mu_p,"mu_p")
    print("]")
