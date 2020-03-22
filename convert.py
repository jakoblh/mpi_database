import csv
import json

#tries to cast val to int

def try_cast_int(val):
    try:
        return int(val)
    except ValueError:
        return val
    


# filename : file name of csv 
# returns : dictionary of json parsable structures, with id as key

def convert_meta(filename):
    file = open(filename)
    csv_reader = list(csv.reader(file, delimiter=','))

    res = {}
    for row in csv_reader[1:]:

        #general
        sample = {}
        sample["meta"] = {}
        sample["meta"]["project"] = row[0]
        sample["meta"]["pr_mpi"] = row[1]
        sample["meta"]["pr_extern"] = row[2]
        sample["meta"]["#"] = row[3]

        #ids
        sample["meta"]["id"] = {}
        sample["meta"]["id"]["original_id"] = row[4]
        sample["meta"]["id"]["id_lab"] = row[5]
        sample["meta"]["id"]["id_ss"] = row[6]
        sample["meta"]["id"]["id_starch"] = row[7]
        sample["meta"]["id"]["id_phenolic"] = row[8]

        #attributes
        sample["meta"]["attributes"] = {}
        sample["meta"]["attributes"]["date"] = row[10]
        sample["meta"]["attributes"]["treatment"] = row[11]
        sample["meta"]["attributes"]["tree"] = row[12]
        sample["meta"]["attributes"]["specie"] = row[13]
        sample["meta"]["attributes"]["tissue"] = row[14]
        sample["meta"]["attributes"]["site"] = row[15]
        sample["meta"]["attributes"]["plot/chamber"] = row[16]
        sample["meta"]["attributes"]["campaign"] = row[17]
        sample["meta"]["attributes"]["subsample"] = row[18]
        sample["meta"]["attributes"]["year"] = try_cast_int(row[19])
        sample["meta"]["attributes"]["growth_year"] = try_cast_int(row[20])
        sample["meta"]["attributes"]["sample_time"] = row[21]
        sample["meta"]["attributes"]["leaf"] = row[22]
        sample["meta"]["attributes"]["name_de"] = row[23]
        sample["meta"]["attributes"]["name_lat"] = row[24]
        sample["meta"]["attributes"]["genus"] = row[25]
        sample["meta"]["attributes"]["label"] = row[26]
        sample["meta"]["attributes"]["stored"] = row[27]

        id = row[5]
        res[id] = sample

    return res




# filename : path to delivery file
# meta : dict of sampel metadata

def convert_delivery(filename, meta):
    file = open(filename)
    csv_reader = list(csv.reader(file, delimiter=','))

    res = {}


files = convert_meta("csv/metadaten.csv")
print(json.dumps(files[1:], sort_keys=False, indent=4, separators=(',', ': ')))




