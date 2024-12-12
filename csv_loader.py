from historydb import HistoryDB
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
mega_file = HistoryDB()
for item in input_dir:
    path = f"{IN_FOLDER_PATH}/{item}"
    if os.path.isfile(path):
        print(path)
        #add lines
        mega_file.add_lines_from_csv(path)
for query in default_tags:
    mega_file.give_tags(query[0], query[1])
print("PRINTING SQLite3 DB")
mega_file.print_table()



