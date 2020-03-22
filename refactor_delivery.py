import csv
import sys

def refactor(in_file):
    csv_file = open(in_file, "r")
    csv_reader = csv.reader(csv_file, delimiter=',')

    meta = {}
    is_meta = True
    printed_header = False
    key_list = ["customer", "workgroup", "project", "costcenter", "delivery date"]
    

    for row in csv_reader:
        if "Einlieferungsschein" in row[0]:
            is_meta = True
        elif "BGC#" in row[0]:
            if not printed_header:
                print(",".join(key_list + row))
                printed_header = True
            is_meta = False
        elif is_meta and row[0] != "":
            print(row)
            meta[row[0]] = row[1]
        elif not is_meta:
            value_list = [meta[x] for x in key_list]
            
            print(",".join(value_list + row))
    csv_file.close()


refactor(sys.argv[1])


