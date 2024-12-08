from csv_cp import CSVCP
from mega_csv import MegaCSV
import os
"""
For each file in the input path, write each unique entry into the master csv file.
Then move the input files into the history path
"""
BUDGET_FILES_PATH = "C:/Users/charl/budget_files/"
IN_FOLDER_PATH = f"{BUDGET_FILES_PATH}csv_in"
HISTORY_FOLDER_PATH = f"{BUDGET_FILES_PATH}vault"
MEGA_TRANSACTION_PATH = f"{BUDGET_FILES_PATH}mega.csv"
default_tags = [
    ["ONLINE PAYMENT THANK YOU", "transfer"],
    ["DOORDASH", "doordash"],
    ["GOOD LIFE", "groceries"],
    ["SAFEWAY", "groceries"],
    ["Playstation", "videogames"],
    ["STEAM", "videogames"]
]
input_dir = os.listdir(IN_FOLDER_PATH)
mega_file = MegaCSV(MEGA_TRANSACTION_PATH)
for item in input_dir:
    path = f"{IN_FOLDER_PATH}/{item}"
    if os.path.isfile(path):
        print(path)
        in_file = CSVCP()
        in_file.from_file(path)
        print("PRINTING READ FILE")
        mega_file.add_new_lines(in_file.rows)
for query in default_tags:
    mega_file.give_tags(query[0], query[1])
print("PRINTING TAGGED MEGA")
mega_file.print_rows()
mega_file.write_to(MEGA_TRANSACTION_PATH)


