from csv_cp import CSVCP
class MegaCSV(CSVCP):
    """A csv object for storing transaction data with an associated tag column"""
    def add_new_lines(self, rows):
        """
        Add a new line to the mega csv for any transaction in the input rows that do not exist in the mega csv rows
        """