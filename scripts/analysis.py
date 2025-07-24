import pandas as pd

def count_total_books(books_df: pd.DataFrame) :
    return len(books_df)

def total_pages_read(books_df: pd.DataFrame) :
    return books_df["pages"].sum()

def attendance_by_member(attendance_df: pd.DataFrame, members_df: pd.DataFrame)
    return attendance_df[attendance_df["attended" == True]] \
    .groupby("member_id")["attended"] \
    .count() \
    .reset_index() \
    .merge(members_df, left_on="member_id", right_on="id", how="left") \
    .rename(columns={"attended": "sessions_attended"})