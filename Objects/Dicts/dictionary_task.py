import csv

with open('TreeOrdersSubset.csv', mode='r') as infile:
    reader = csv.reader(infile)
    treeOrders = {}
    for row in reader:
        key = row[0]
        value = int(row[1])
        if key not in treeOrders:
            treeOrders[key] = value
        else:
            treeOrders[key] += value

infile.close()
print("length of dictionary ", len(treeOrders))

# Create a new dict treeOrders10 with subdivisions that have more than 10 tree orders
# use dict comprehension
new_dict = {k: v for k, v in treeOrders.items() if treeOrders[k] > 10}
for k, v in new_dict.items():
    print(f'|{k:^9} - {v:^9}|')
print(f"Length of dictionary - {len(new_dict)}")
