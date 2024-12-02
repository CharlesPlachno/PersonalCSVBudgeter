import csv

class CSVCP():
    """Contains useful methods for csv files"""
    rows = []
    def __init__(self, path):
        rows = []
        with open(path, newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                rows.append(row)
        self.rows = rows

    def print_rows(self):
        for row in self.rows:
            print(row)