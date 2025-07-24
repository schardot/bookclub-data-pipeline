import streamlit as st
import pandas as pd

st.title("📚 Buchblick - Book Club Dashboard")

books_df = pd.read_csv("data/books.csv")

st.write("Suggestions picked:")
st.dataframe(books_df)