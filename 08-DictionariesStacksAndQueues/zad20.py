import csv
import json
with open("products.csv",'r') as file1:
    csdict=csv.DictReader(file1)
    data_list = []
    for row in csdict:
        data_list.append(row)
with open("products.json",'w')as file2:
    json.dump(data_list,file2, indent=4)
    