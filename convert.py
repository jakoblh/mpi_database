import sys
import csv
import json

#tries to cast val to int

def try_cast_int(val):
    try:
        return int(val)
    except ValueError:
        return None 
    

#tries to cast val to int

def try_cast_float(val):
    try:
        return float(val)
    except ValueError:
        return None


# filename : file name of csv 
# returns : dictionary of json parsable structures, with id as key

def convert_meta(filename, delivery_dict):
    file = open(filename)
    csv_reader = list(csv.reader(file, delimiter=',', quotechar='"'))

    res = {} 
    for row in csv_reader[1:]:

        id = row[5]
        id_ss = row[6]
        id_starch = row[7]
        id_phenolic = row[8]


        sample = {}
        
        #sample does not exist in res yet
        if id not in res:


            #general
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


            #data
            sample["data"] = {}
            sample["data"]["ss"] = []
            sample["data"]["starch"] = []
            sample["data"]["phenolic"] = []

            res[id] = sample
        
        #sample exists
        else:
            sample = res[id]


        #extractions
        if id_ss in delivery_dict:
            sample["data"]["ss"].append(delivery_dict[id_ss])
        if id_starch in delivery_dict:
            sample["data"]["starch"].append(delivery_dict[id_starch])
        if id_phenolic in delivery_dict:
            sample["data"]["phenolic"].append(delivery_dict[id_phenolic])


    return res


# filename : path to delivery file
# meta : dict of sampel metadata

def convert_delivery(filename):
    file = open(filename)
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')
    
    res = {}

    for row in csv_reader:
        id = row[6]
        sample = {}
            
        #data meta
        sample["lieferschein"] = {}
        sample["lieferschein"]["costumer"] = row[0]
        sample["lieferschein"]["workgroup"] = row[1]
        sample["lieferschein"]["project"] = row[2]
        sample["lieferschein"]["costcenter"] = row[3]
        sample["lieferschein"]["delivery_date"] = row[4]

        #values
        sample["sample_id"] = id
        sample["year"] = try_cast_int(row[8])
        sample["processing"] = row[10]
        sample["comment_redbook"] = row[11]
        sample["box_no"] = row[12]
        sample["box_position"] = row[13]
        sample["weigth"] = try_cast_float(row[14])
        sample["sample_processing"] = row[15]
        sample["extraction_date"] = row[16]
        sample["extraction_volume"] = try_cast_float(row[17])
        sample["dillution"] = try_cast_int(row[18])

        #extractions to be done
        extractions = {}
        extractions[row[19]] = "True"
        extractions[row[20]] = "True"
        extractions[row[21]] = "True"
        extractions[row[22]] = "True"

        sample["extractions"] = list(extractions.keys())

        res[id] = sample

    return res 


delivery_dict = convert_delivery(sys.argv[2])
meta_dict = convert_meta(sys.argv[1], delivery_dict)
meta_list = list(meta_dict.values())

print(json.dumps(meta_list, sort_keys=False, indent=4, separators=(',', ': ')))

