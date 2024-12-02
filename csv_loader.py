from csv_cp import CSVCP
import os
"""
For each file in the input path, write each unique entry into the master csv file.
Then move the input files into the history path
"""
BUDGET_FILES_PATH = "C:/Users/charl/budget_files/"
IN_FOLDER_PATH = f"{BUDGET_FILES_PATH}csv_in"
HISTORY_FOLDER_PATH = f"{BUDGET_FILES_PATH}vault"
MEGA_TRANSACTION_PATH = f"{BUDGET_FILES_PATH}mega"

input_dir = os.listdir(IN_FOLDER_PATH)
for item in input_dir:
    if os.path.isfile(item):
        print(item)
        in_file = CSVCP(item)
        in_file.print_rows()


