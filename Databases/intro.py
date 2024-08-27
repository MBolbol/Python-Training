# Datbase is places where we can store data
# it organized into tables (users, categories)
# tables has columns (ID, Username, Password)
# many types of databases (MongoDB, MySQL, SQLite)
# SQL stand for => Structured Query Language
# SQLite => can run in memory or single file
# you can browse file with https://sqlitebrowser.org/
# Data inside DB has types (text, int, date)
# -------------------------------------------------------------
# Create DB and connect
# -------------------------
# - Connect
# - Execute
# - Close
# -----------------------

# import sqlite module
import sqlite3

# Creat DB and connect

db = sqlite3.connect('app.db')

# creates tables & fields

db.execute('CREATe TABLE if not exists skills (name TEXT, progress INT, uesr_id INT)')

# close

db.close()
