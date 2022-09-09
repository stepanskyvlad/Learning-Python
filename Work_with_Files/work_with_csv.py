import csv


with open('10_02_us.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)  # skip the first row
    for row in reader:
        print(row)

with open('10_02_us.csv', 'r') as f:
    reader = list(csv.reader(f, delimiter='\t'))
    for row in reader[1:]: # skip the first row
        print(row)
