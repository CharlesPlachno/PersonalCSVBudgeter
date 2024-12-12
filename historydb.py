import os
import sqlite3
from datetime import datetime, date
from csv_cp import CSVCP
class HistoryDB:
    """
    sqlite3 database which houses all the rows read from input files
    """
    db_location = 'data'
    table_name = 'budget_history'
    row_structure = "(date, value, name, tag)"

    def __init__(self):
        self.create_table()

    def sql_query(self, sql, params=None, get_response=False):
        response = ""
        conn = sqlite3.connect('data')
        c = conn.cursor()
        if params:
            c.execute(sql, params)
        else:
            c.execute(sql)
        if get_response:
            response = c.fetchall()
        conn.commit()
        conn.close()
        return response

    def create_table(self):
        sql = f"create table if not exists {self.table_name} (date, value, name, tag)"
        self.sql_query(sql)

    def add_row(self, row):
        #select for this row, if it already exists don't add it
        query = f"SELECT * FROM {self.table_name} WHERE date = ? AND value = ? AND name = ?"
        params = (row[0], row[1], row[2])
        row_exists = self.sql_query(query, params, get_response=True)
        print(row_exists)
        if row_exists:
            print(f"Row already exists: {str(row)}")
        else:
            sql = f"INSERT INTO {self.table_name} (date, value, name, tag) VALUES (?, ?, ?, ?)"
            params = (row[0], row[1], row[2], "")
            self.sql_query(sql, params)

    def add_lines_from_csv(self, path):
        # iterate through reader and add each row
        csvfile = CSVCP()
        csvfile.from_file(path)
        for row in csvfile.rows:
            self.add_row([row[0], row[1], row[4], ''])

    def give_tags(self, search_string, tag):
        pass

    def print_table(self):
        sql = f"SELECT * FROM {self.table_name}"
        response = self.sql_query(sql, get_response=True)
        print(response)