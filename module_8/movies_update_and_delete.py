import mysql.connector
from mysql.connector import errorcode
from mysql.connector.constants import SQLMode



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

def show_films(cursor, title):
    # Execute an INNER JOIN on all tables
    # iterate over the dataset and output the results to the terminal window
    cursor.execute("SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    films = cursor.fetchall()

    print("\n-- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

cursor = db.cursor()

# Main Code
# Display before making changes
show_films(cursor, "DISPLAYING FILMS")

# Add a movie to Film table
cursor.execute("INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime) VALUES('Oppenheimer', 'Christopher Nolan', 3, 3, '2023', 181)")
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update 'Alien' to a Horror film
cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - CHANGED Alien TO HORROR")

# Delete 'Gladiator' from database
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

db.close()
input("Press 'Enter' to Exit...")