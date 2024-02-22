import psycopg2

connection = psycopg2.connect(database= "chinook")

cursor = connection.cursor()
#cursor.execute('SELECT * FROM "artist"')
#cursor.execute('SELECT "name"  FROM "artist"')

#get all 
#results = cursor.fetchall()

#get one method 
cursor.execute('SELECT * FROM "artist" WHERE "name"= %s', ["Queen"])

results = cursor.fetchone()

connection.close()

for result in results: 
    print(result)