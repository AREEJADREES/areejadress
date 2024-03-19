import streamlit as st

def welcome_students(student_name):
    st.title(f"Welcome to Students, {student_name}!")

def main():
    st.header("Welcome to the Student Welcome App")
    student_name = st.text_input("Enter your name:")
    if student_name:
        welcome_students(student_name)

if __name__ == "__main__":
    main()
