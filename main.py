import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')

cursor = conn.cursor()

# Множественная вставка строк:

# new_artists = [
#     ('A Aagrh!',),
#     ('A Aagrh!-2',),
#     ('A Aagrh!-3',),
# ]
# cursor.executemany("insert into Artist values (Null, ?);", new_artists)

# Запись в бд:

# cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")
#
# conn.commit()
#
# cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
# results = cursor.fetchall()
# print(results)

# Чтение из бд(вывод всей бд):

cursor.execute("SELECT * FROM Artist")

results = cursor.fetchall()
results2 = cursor.fetchall()

print(results)
print(results2)

conn.close()
