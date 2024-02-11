import sqlite3
import csv

con = sqlite3.connect("clevland_replica.db")
cur = con.cursor()

with open('processed_cleveland.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Assuming the first row of the CSV file contains column headers
    data = list(reader)  # Read the remaining rows into a list

    create_table_sql = f"CREATE TABLE IF NOT EXISTS processed_cleveland ({', '.join([f'{header} TEXT' for header in headers])})"
    cur.execute(create_table_sql)

    insert_sql = f"INSERT INTO processed_cleveland ({', '.join(headers)}) VALUES ({', '.join(['?'] * len(headers))})"
    cur.executemany(insert_sql, data)

    create_table_sql = f"CREATE TABLE IF NOT EXISTS extended_cleveland ({', '.join([f'{header} TEXT' for header in headers])})"
    cur.execute(create_table_sql)

    insert_sql = f"INSERT INTO extended_cleveland ({', '.join(headers)}) VALUES ({', '.join(['?'] * len(headers))})"
    cur.executemany(insert_sql, data)


#print(cur.execute('select * from processed_cleveland limit 3').fetchall())

# Reset the file pointer to the beginning of the file
print(cur.execute('select * from processed_cleveland limit 1').fetchall())
print(cur.execute('select * from extended_cleveland limit 1').fetchall())

# Commit changes and close the connection
con.commit()
con.close()

print("All Done!!")
