import pandas as pd

def count_total_books(books_df: pd.DataFrame) :
    return len(books_df)

def total_pages_read(books_df: pd.DataFrame) :
    return books_df["pages"].sum()

def attendance_by_member(attendance_df: pd.DataFrame, members_df: pd.DataFrame) :
    return attendance_df[attendance_df["attended" == True]] \
    .groupby("member_id")["attended"] \
    .count() \
    .reset_index() \
    .merge(members_df, left_on="member_id", right_on="id", how="left") \
    .rename(columns={"attended": "sessions_attended"})

def member_with_most_suggestions(books_df):
    if books_df.empty or "suggested_by" not in books_df.columns:
        return "No data"
    suggestion_counts = books_df["suggested_by"].value_counts()
    if suggestion_counts.empty:
        return "No suggestions yet"
    return suggestion_counts.idxmax()

def members_with_most_attendance(attendance_df, members_df):
    if attendance_df.empty or "voted" not in attendance_df.columns or "member_id" not in attendance_df.columns:
        return ["No data"]

    attendance_counts = attendance_df[attendance_df["voted"] == True]["member_id"].value_counts()

    if attendance_counts.empty:
        return ["No attendance records"]

    max_attendance = attendance_counts.max()
    top_members_ids = attendance_counts[attendance_counts == max_attendance].index.tolist()
    top_members_names = members_df[members_df["member_id"].isin(top_members_ids)]["name"].tolist()

    return top_members_names
