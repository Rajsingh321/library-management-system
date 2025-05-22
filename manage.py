import streamlit as st
import datetime

# Initialize session state for storing book records if not already initialized
if 'books' not in st.session_state:
    st.session_state.books = {}

# Title
st.title("📚 Library Management System")

# Sidebar navigation
menu = st.sidebar.radio("Menu", ["Issue Book", "Re-Issue Book", "Submit Book", "View Records"])

def issue_book():
    st.header("📖 Issue a Book")
    enrolment = st.text_input("Enter Enrolment Number")
    book_name = st.text_input("Enter Book Name")

    if st.button("Issue Book"):
        if enrolment and book_name:
            today = datetime.date.today()
            st.session_state.books[enrolment] = {
                'book': book_name,
                'issue_date': today,
                'due_date': today + datetime.timedelta(days=30)
            }
            st.success(f"Book '{book_name}' issued to {enrolment}.")
        else:
            st.error("Please fill all fields.")

def reissue_book():
    st.header("🔁 Re-Issue a Book")
    enrolment = st.text_input("Enter Enrolment Number")

    if st.button("Re-Issue Book"):
        if enrolment in st.session_state.books:
            today = datetime.date.today()
            st.session_state.books[enrolment]['issue_date'] = today
            st.session_state.books[enrolment]['due_date'] = today + datetime.timedelta(days=30)
            st.success(f"Book re-issued to {enrolment}. New due date is {st.session_state.books[enrolment]['due_date']}.")
        else:
            st.error("No book issued under this enrolment number.")

def submit_book():
    st.header("📥 Submit a Book")
    enrolment = st.text_input("Enter Enrolment Number")

    if st.button("Submit Book"):
        if enrolment in st.session_state.books:
            del st.session_state.books[enrolment]
            st.success("Book submitted successfully.")
        else:
            st.error("No book found for this enrolment number.")

def view_records():
    st.header("📋 Issued Book Records")
    if st.session_state.books:
        for enrol, info in st.session_state.books.items():
            st.write(f"**Enrolment**: {enrol}")
            st.write(f"- Book: {info['book']}")
            st.write(f"- Issue Date: {info['issue_date']}")
            st.write(f"- Due Date: {info['due_date']}")
            st.markdown("---")
    else:
        st.info("No books issued yet.")

if menu == "Issue Book":
    issue_book()
elif menu == "Re-Issue Book":
    reissue_book()
elif menu == "Submit Book":
    submit_book()
elif menu == "View Records":
    view_records()
