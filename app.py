import streamlit as st
import pandas as pd

from scripts.analysis import (
    count_total_books,
    total_pages_read,
    attendance_by_member,
    member_with_most_suggestions,
    members_with_most_attendance,
)

from scripts.data_loading import (
    load_attendance,
    load_books,
    load_csv,
    load_members,
    load_sessions
)

BOOKS_CSV = "data/books.csv"
MEMBERS_CSV = "data/members.csv"
ATTENDANCE_CSV = "data/attendance.csv"

books_df = load_books()
members_df = load_members()
attendance_df = load_attendance()

st.title("📚 Buchblick - Book Club Dashboard")

st.subheader("Club statistics")


col1, col2 = st.columns(2)
col1.metric("Books read", count_total_books(books_df))
col2.metric("Total pages", total_pages_read(books_df))

st.metric("Top Book Suggester", member_with_most_suggestions(books_df))
top_attendees = members_with_most_attendance(attendance_df, members_df)
print(top_attendees)
top_attendees_str = ", ".join(top_attendees) if isinstance(top_attendees, list) else str(top_attendees)

st.metric("Top Attendees", top_attendees_str)

st.header("Add a New Book")

with st.form("add_book_form"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    pages = st.number_input("Pages", min_value=1, step=1)
    theme = st.text_input("Theme of the Month")
    suggested_by = st.text_input("Who Suggested It?")
    average_stars = st.number_input("Average Stars", min_value=0.0, max_value=5.0, step=0.1)
    meeting_date = st.date_input("Meeting Date")

    submitted = st.form_submit_button("Add Book")

    if submitted:
        new_book = {
            "title": title,
            "author": author,
            "genre": genre,
            "pages": pages,
            "theme of the month": theme,
            "who suggested it": suggested_by,
            "average stars": average_stars,
            "meeting date": meeting_date.strftime("%Y-%m-%d")
    }

    current_df = load_books()
    updated_df = pd.concat([current_df, pd.DataFrame([new_book])], ignore_index=True)
    updated_df.to_csv(BOOKS_CSV, index=False)

    st.success(f"Book '{title}' added!")

    st.subheader("Current Books")
    st.dataframe(updated_df)
