import mysql.connector
from mysql.connector import errorcode
from mysql.connector.constants import SQLMode

# Create Database
db = mysql.connector.connect( # Using movies_user from previous modules, because everyone should already have this user.
    host="localhost",
    user="movies_user",
    password="popcorn"
)
cursor = db.cursor()

# Create Database WillsonFinancial
cursor.execute("CREATE DATABASE IF NOT EXISTS WillsonFinancial")
cursor.close()
db.close() # Going to re-connect to the new database, because I can re-use the code below

config = { # Using the movies_user
    "user": "movies_user", 
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "WillsonFinancial",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    db.sql_mode = ''

    print("Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n Press 'Enter' to continue...\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

cursor = db.cursor()

