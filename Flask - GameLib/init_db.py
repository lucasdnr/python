import mysql.connector
from mysql.connector import errorcode

print('Connecting...')

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )

except mysql.connector.Error as err:
    if err.errno == errorcode.ERACCESS_DENIED_ERROR:
        print('There is something wrong with the username or password')
    else:
        print(err)
else:
    print('Connected')

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS gamelib;")

cursor.execute("CREATE DATABASE gamelib;")

cursor.execute("USE gamelib")

# creating tables
TABLES = {}

TABLES['Games'] = ('''
    CREATE TABLE `gamelib`.`games` (
      `id` INT NOT NULL AUTO_INCREMENT,
      `name` VARCHAR(50) NOT NULL,
      `category` VARCHAR(40) NOT NULL,
      `console` VARCHAR(20) NOT NULL,
      PRIMARY KEY (`id`))
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8
    COLLATE = utf8_bin; ''')

TABLES['Users'] = ('''
    CREATE TABLE `gamelib`.`users` (      
      `name` VARCHAR(50) NOT NULL,
      `nickname` VARCHAR(10) NOT NULL,
      `password` VARCHAR(100) NOT NULL,
      PRIMARY KEY (`nickname`))
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8
    COLLATE = utf8_bin;  ''')

for table_name in TABLES:
    table_sql = TABLES[table_name]
    try:
        print(f'Creating Table {table_name}')
        cursor.execute(table_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Table already exists')
        else:
            print(err.msg)
    else:
        print('ok')

# inserting users
users_sql = 'INSERT INTO users (name, nickname, password) values (%s,%s,%s)'

users = [
    ("Jason", "L", "123"),
    ("Kaike", "DOG", "321"),
]

cursor.executemany(users_sql, users)

cursor.execute('select * from gamelib.users')
print('---------------- Users ----------------')
for user in cursor.fetchall():
    print(user[0])

# inserting games
game_sql = 'INSERT INTO games (name, category, console) values (%s,%s,%s)'

games = [
    ("Tetris", "Puzzle", "Atari"),
    ("God of War", "Hack and Slash", "PS2"),
    ("Mortal Kombat I", "Fight", "PS2"),
    ("Need for Speed", "Rush", "PC"),
]

cursor.executemany(game_sql, games)

cursor.execute('select * from gamelib.games')
print('---------------- Games ----------------')
for game in cursor.fetchall():
    print(game[1])

# commit to save the database
conn.commit()

cursor.close()
# closing DB connection
conn.close()
