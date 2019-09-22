import random
import numpy as np
import csv

xs = []
ys = []

class NodeGenerator:
    def __init__(self, width, height, nodesNumber):
        self.width = width
        self.height = height
        self.nodesNumber = nodesNumber

    def generate(self):
        # xs = np.random.randint(self.width, size=self.nodesNumber)
        # ys = np.random.randint(self.height, size=self.nodesNumber)
        with open('Locations.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                # print(f'\t{row[0]} ***** {row[1]} ***** {row[2]}.')
                    xs.append(float(row[2]))
                    ys.append(float(row[1]))
                    line_count += 1                
                
                
                    

        return np.column_stack((xs, ys))
