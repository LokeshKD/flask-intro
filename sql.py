import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE table posts(title TEXT, description TEXT)""")
    c.execute('INSERT into posts VALUES("Good", "I am good")')
    c.execute('INSERT into posts VALUES("God", "You are good")')
    c.execute('INSERT into posts VALUES("Good God", "All are good")')
