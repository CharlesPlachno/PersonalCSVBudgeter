from csv_cp import CSVCP
import os
from datetime import datetime, date
class MegaCSV(CSVCP):
    """
    A csv object for storing transaction data with an associated tag column
    |date|value|name|tag|

    keep the data updated in a dictionary with month/year for keys for faster searching
    """

    def __init__(self, path):
        # check if file exists, if it does read from it
        if os.path.exists(path):
            self.from_file(path)
            #TODO fail if incorrect number of files or add other identifier to top of file
        else:
            open(path, "a").close()

    def add_new_lines(self, csv_data):
        """Add new line to the mega csv for any transaction in the input rows that do not exist in the mega csv rows"""
        for row in csv_data:
            new_row =[row[0], row[1], row[4], ""]
            #check if this row exists already
            if new_row not in self.rows:
                self.rows.append(new_row)
        self.sort_rows()

    def sort_rows(self):
        self.rows.sort(key=lambda x: int(datetime.strptime(x[0], "%m/%d/%Y").strftime("%Y%m%d")), reverse=True)

    def give_tags(self, search_string, tag):
        for row in self.rows:
            if search_string in row[2]:
                row[3] = tag
