import json
import operator
import numpy as ns

RESULT_FILES = ["output/urdmeMiningPartialWindow_10_1000_0_10.json", \
                "output/urdmeMiningPartialWindow_10_1000_10_20.json", \
                "output/urdmeMiningPartialWindow_10_1000_20_30.json", \
                "output/urdmeMiningPartialWindow_10_1000_30_40.json", \
                "output/urdmeMiningPartialWindow_10_1000_40_50.json", \
                "output/urdmeMiningPartialWindow_10_1000_50_60.json", \
                "output/urdmeMiningPartialWindow_10_1000_60_70.json", \
                "output/urdmeMiningPartialWindow_10_1000_70_80.json", \
                "output/urdmeMiningPartialWindow_10_1000_80_90.json", \
                "output/urdmeMiningPartialWindow_10_1000_90_100.json" ]

resultList = []

if __name__ == "__main__":
    # read result file one by one
    for _file in RESULT_FILES:
        print(_file)
        with open(_file) as _reader:
            data = []
            for line in _reader:
                data.append(json.loads(line))
            if len(data) > 1:
                print("Unimplement Multiple rows query.")
                quit()
            else:
                if len(data[0]) != 1:
                    print("Unimplement Multiple rows query.")
                    quit()

                content = data[0][0]
                
                sortedResult = sorted(content, key=lambda x: x['_value'])
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

                for bandValue in range(9):
                    filteredResult = filter(lambda x: True if 'B'+str(bandValue) in str(x['_key']) else False, content)
                    sortedFilterResult = sorted(filteredResult, key=lambda x: x['_value'])
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
                        
        print('\n\n\n')
