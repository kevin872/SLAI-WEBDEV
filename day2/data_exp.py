import csv

def read_csv(file_name):
    with open(file_name, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        return [item for item in reader]
