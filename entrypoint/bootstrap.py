import json
import mysql.connector

conn = mysql.connector.connect(
    host="db",
    user="user",
    password="password",
    database="ubc_campus_explorer",
)
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE rooms (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fullname TEXT,
        shortname TEXT,
        number TEXT,
        name TEXT,
        address TEXT,
        lat DOUBLE,
        lon DOUBLE,
        seats INT,
        type TEXT,
        furniture TEXT
    );
    """
)

with open("rooms.json", "r") as f:
    data = json.load(f)

for room in data:
    cursor.execute(
        """
        INSERT INTO rooms (fullname, shortname, number, name, address, lat, lon, seats, type, furniture)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,
        (
            room["fullname"],
            room["shortname"],
            room["number"],
            room["name"],
            room["address"],
            room["lat"],
            room["lon"],
            room["seats"],
            room["type"],
            room["furniture"],
        ),
    )

conn.commit()
conn.close()
