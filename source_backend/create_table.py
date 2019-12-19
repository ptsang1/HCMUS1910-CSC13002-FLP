import sqlite3


connection =sqlite3.connect("database/database.db")
cursor = connection.cursor()

query ="CREATE TABLE IF NOT EXISTS users (userid text PRIMARY KEY , email text,password text,full_name text,create_date DATE ,avatar_link text)"

#query ="CREATE TABLE IF NOT EXISTS recipe(postid text PRIMARY KEY, userid text NOT NULL,foodname text,descriptor text,foodimage text)"

cursor.execute(query)
connection.commit()
connection.close()