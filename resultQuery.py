import json
import operator
import numpy as ns
'''
RESULT_FILES = ["output/urdmeMiningPartialWindow_4_1000_0_8.json", \
                "output/urdmeMiningPartialWindow_4_1000_8_16.json", \
                "output/urdmeMiningPartialWindow_4_1000_24_32.json", \
                "output/urdmeMiningPartialWindow_4_1000_32_40.json", \
                "output/urdmeMiningPartialWindow_4_1000_40_48.json", \
                "output/urdmeMiningPartialWindow_4_1000_48_56.json", \
                "output/urdmeMiningPartialWindow_4_1000_56_64.json", \
                "output/urdmeMiningPartialWindow_4_1000_64_72.json", \
                "output/urdmeMiningPartialWindow_4_1000_72_80.json", \
                "output/urdmeMiningPartialWindow_4_1000_80_88.json", \
                "output/urdmeMiningPartialWindow_4_1000_88_96.json", \
                "output/urdmeMiningPartialWindow_4_1000_96_100.json"  ]
'''
RESULT_FILES = ["output/urdmeMiningPartialWindow_SE_4_5_0_4.json", \
                "output/urdmeMiningPartialWindow_SE_4_5_4_8.json", \
                "output/urdmeMiningPartialWindow_SE_4_5_8_12.json", \
                "output/urdmeMiningPartialWindow_SE_4_5_12_16.json", \
                "output/urdmeMiningPartialWindow_SE_4_5_24_28.json" ]

resultList = []

'''
def filterData(inputData, matching):
    result = []
    for line in inputData:
        if matching in str(line):
            result.append(line)
'''

if __name__ == "__main__":
    # read result file one by one
    for _file in RESULT_FILES:
        print(_file)
        with open(_file) as _reader:
            data = []
            for line in _reader:
                data.append(json.loads(line))
            if len(data) > 1:
                print("Unimplement Multiple outer rows query.")
                quit()
            else:
                if len(data[0]) != 1:
                    for dataSet in data[0]:
                        content = dataSet
                         
                        sortedResult = sorted(content, key=lambda x: x['_value'], reverse=True)
                        print("First")
                        print(sortedResult[0])
                        print(sortedResult[1])
                        print(sortedResult[2])
                        print(sortedResult[3])
                        print(sortedResult[4])

                        print("Last")
                        print(sortedResult[-5])
                        print(sortedResult[-4])
                        print(sortedResult[-3])
                        print(sortedResult[-2])
                        print(sortedResult[-1])
                        
                        # for bandValue in reversed(range(9)):
                        for bandValue in range(9):
                            filteredResult = filter(lambda x: True if ('protein_B'+str(bandValue)) in str(x['_key']) else False, content)
                            sortedFilterResult = sorted(filteredResult, key=lambda x: x['_value'], reverse=True)
                            print("B" + str(bandValue) + " First")
                            if len(sortedFilterResult) >= 5:
                                print(sortedFilterResult[0])
                                print(sortedFilterResult[1])
                                print(sortedFilterResult[2])
                                print(sortedFilterResult[3])
                                print(sortedFilterResult[4])
                                print("B" + str(bandValue) + " Last")
                                print(sortedFilterResult[-5])
                                print(sortedFilterResult[-4])
                                print(sortedFilterResult[-3])
                                print(sortedFilterResult[-2])
                                print(sortedFilterResult[-1])
                            elif len(sortedFilterResult) == 0:
                                print("Empty Result")
                                continue
                            else:
                                for j in range(len(sortedFilterResult)):
                                    print(sortedFilterResult[j])
                                for j in reversed(range(1,len(sortedFilterResult))):
                                    print(sortedFilterResult[j * -1])
                            print("Band Set--------")
                        print("Window Set---------------------")
                else:
                    content = data[0][0]
                     
                    sortedResult = sorted(content, key=lambda x: x['_value'], reverse=True)
                    print("First")
                    print(sortedResult[0])
                    print(sortedResult[1])
                    print(sortedResult[2])
                    print(sortedResult[3])
                    print(sortedResult[4])

                    print("Last")
                    print(sortedResult[-5])
                    print(sortedResult[-4])
                    print(sortedResult[-3])
                    print(sortedResult[-2])
                    print(sortedResult[-1])
                    
                    # for bandValue in reversed(range(9)):
                    for bandValue in range(9):
                        filteredResult = filter(lambda x: True if ('protein_B'+str(bandValue)) in str(x['_key']) else False, content)
                        sortedFilterResult = sorted(filteredResult, key=lambda x: x['_value'], reverse=True)
                        print("B" + str(bandValue) + " First")
                        if len(sortedFilterResult) >= 5:
                            print(sortedFilterResult[0])
                            print(sortedFilterResult[1])
                            print(sortedFilterResult[2])
                            print(sortedFilterResult[3])
                            print(sortedFilterResult[4])
                            print("B" + str(bandValue) + " Last")
                            print(sortedFilterResult[-5])
                            print(sortedFilterResult[-4])
                            print(sortedFilterResult[-3])
                            print(sortedFilterResult[-2])
                            print(sortedFilterResult[-1])
                        elif len(sortedFilterResult) == 0:
                            print("Empty Result")
                            continue
                        else:
                            for j in range(len(sortedFilterResult)):
                                print(sortedFilterResult[j])
                            for j in reversed(range(1,len(sortedFilterResult))):
                                print(sortedFilterResult[j * -1])
                            
        print('Frame Set-----------------------------------------------------------------------------------')
