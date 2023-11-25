import mysql.connector
from mysql.connector import errorcode
from mysql.connector.constants import SQLMode

config = { #Using the movies_user from db_init_2022.sql file
    "user": "movies_user", 
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
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

# Query 1: Studio Table
cursor.execute("SELECT studio_id, studio_name FROM studio")
studios = cursor.fetchall()

print("-- DISPLAYING Studio RECORDS --")
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

# Query 2: Genre Table
cursor.execute("SELECT genre_id, genre_name FROM genre")
genres = cursor.fetchall()

print("-- DISPLAYING Studio RECORDS --")
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

# Query 3: Movies with runtime less than 120 minutes
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
films = cursor.fetchall()

print("-- DISPLAYING Short Film RECORDS --")
for film in films:
    print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

# Query 4: List film names and directors, ordered by Director
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
filmsByDir = cursor.fetchall()

print("-- DISPLAYING Director RECORDS in Order --")
for film in filmsByDir:
    print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))

db.close()
input("Press 'Enter' to exit...")
