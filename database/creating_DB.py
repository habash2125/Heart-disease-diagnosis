import sqlite3
import csv
import os

# Path to your SQLite database file
db_file = 'clevland_replica.db'

# Check if the file exists before attempting to delete it
if os.path.exists(db_file):
    os.remove(db_file)
    print("Database deleted successfully.")
else:
    print("Database file not found.")


# creating DataBase
con = sqlite3.connect("clevland_replica.db")
cur = con.cursor()

print('Database Created!!')
## filling the tables with the data from the CSV file 

current_path = os.getcwd()
with open(current_path + '/database/processed_cleveland.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Assuming the first row of the CSV file contains column headers
    data = list(reader)  # Read the remaining rows into a list

    create_table_sql = f"CREATE TABLE IF NOT EXISTS processed_cleveland ({', '.join([f'{header} TEXT' for header in headers])})"
    cur.execute(create_table_sql)

    insert_sql = f"INSERT INTO processed_cleveland ({', '.join(headers)}) VALUES ({', '.join(['?'] * len(headers))})"
    cur.executemany(insert_sql, data)

    create_table_sql = f"CREATE TABLE IF NOT EXISTS extended_cleveland ({', '.join([f'{header} TEXT' for header in headers])})"
    cur.execute(create_table_sql)
    '''
    insert_sql = f"INSERT INTO extended_cleveland ({', '.join(headers)}) VALUES ({', '.join(['?'] * len(headers))})"
    cur.executemany(insert_sql, data)
    '''


# Reset the file pointer to the beginning of the file
print(cur.execute('select * from processed_cleveland limit 1').fetchall())
print(cur.execute('select * from extended_cleveland limit 1').fetchall())

# Commit changes and close the connection
con.commit()
con.close()

print("All Done!!")
