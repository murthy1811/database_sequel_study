import os
import pymysql
#get username from cloud9 workspace
#(modify this variable if running on another environment)
username = os.getenv('murthy1811_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:        
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                          Friends(name char(20), age int, DOB datetime);""")
        #Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()