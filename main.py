import mysql.connector

db = mysql.connector.connect(
    host="db",
    user="CHANGE_ME",
    password="CHANGE_ME",
    database="app_db"
)

# NOTE: This code will spam the db, due to the docker-compose.yml specificing 'restart: always'. It is merely an example.
# cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS testing (id INT AUTO_INCREMENT PRIMARY KEY, test VARCHAR(255))")
# cursor.execute("INSERT INTO testing (test) VALUES ('this is a test')")
# db.commit()  NOTE: You must commit when modifying tables.
# print("Completed")
