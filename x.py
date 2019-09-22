import random
import numpy as np
import csv

xs =[]
ys=[]
size_width = 200
size_height = 200
with open('Locations.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} ***** {row[1]} ***** {row[2]}.')
            xs.append(float(row[1]))
            ys.append(float(row[2]))
            line_count += 1
    print(f'Processed {line_count} lines.')
   

print(np.column_stack((xs, ys)))
# population_size = 70

# xs = np.random.randint(size_width, size=population_size)
# ys = np.random.randint( size_height, size=population_size)


# print(np.column_stack((xs, ys)))