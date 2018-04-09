import sqlite3


conn = sqlite3.connect('diary.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM diary WHERE username=?',("test" ,))

print cursor.fetchall()
