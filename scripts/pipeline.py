import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

books = pd.read_csv(os.path.join(DATA_DIR, 'books.csv'))
members = pd.read_csv(os.path.join(DATA_DIR, 'members.csv'))
sessions = pd.read_csv(os.path.join(DATA_DIR, 'sessions.csv'))
attendance = pd.read_csv(os.path.join(DATA_DIR, 'attendance.csv'))

print("Books:")
print(books.head(), "\n")

print("Members:")
print(members.head(), "\n")

print("Sessions:")
print(sessions.head(), "\n")

print("Attendance:")
print(attendance.head(), "\n")
