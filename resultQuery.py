import json
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

if __name__ == "__main__":
    # read result file one by one
    for _file in RESULT_FILES:
        with open(_file) as _reader:
            data = []
            for line in _reader:
                data.append(json.loads(line))
            if len(data) > 1:
                print("Unimplement Multiple rows query.")
                quit()
            else:
                print(data[0])
                
            
