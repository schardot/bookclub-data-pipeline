import pandas as pd

def filter_books(df_books, genre=None, theme=None) :
    filtered = df_books
    if genre:
        filtered = filtered[filtered['genre'].str.lower() == genre.lower]

def calculate_average_starts_per_book(att_path)