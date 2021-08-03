# // Convert CSV data from different files to a single File

import csv
import json

path = "C:\\Users\\sachinsri12345\\Desktop\\Python\\"

with open(path + "data.csv", "r") as csvFile:
    csvReader = csv.DictReader(csvFile)
    csvData = list(csvReader)

    with open(path + "data.json", "w") as jsonFile:
        jsonFile.write(json.dumps(csvData, indent=4))
    
    print("JSON File Created")
    

