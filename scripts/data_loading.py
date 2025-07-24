import pandas as pd

def load_csv(file_path, expected_columns):
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {file_path} with shape {df.shape}")
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found. Returning empty DataFrame.")
        return pd.DataFrame(columns=expected_columns)

def load_books():
    columns = ["title", "author", "genre", "pages", "theme of the month", "who suggested the book", "average stars", "meeting date"]
    return load_csv("data/books.csv", columns)

def load_members():
    columns = ["member_id", "name"]
    return load_csv("data/members.csv", columns)

def load_sessions():
    columns = ["session_id", "book"]
    return load_csv("data/sessions.csv", columns)

def load_attendance():
    columns = ["session_id", "member_id", "attended", "voted", "stars_given"]
    return load_csv("data/attendance.csv", columns)

if __name__ == "__main__":
    books_df = load_books()
    members_df = load_members()
    sessions_df = load_sessions()
    attendance_df = load_attendance()

    print(books_df.head())
    print(members_df.head())
    print(sessions_df.head())
    print(attendance_df.head())