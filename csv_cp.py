import csv

class CSVCP():
    """Contains useful methods for csv files"""
    rows = []

    def from_file(self, path):
        with open(path, newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                self.rows.append(row)

    def print_rows(self):
        for row in self.rows:
            print(row)

    def write_to(self, path):
        with open(path, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            for row in self.rows:
                csvwriter.writerow(row)
