from datetime import datetime

def non_empty(value):
    while not value.strip():
        value = input("This field cannot be empty. Enter again: ")
    return value.strip()

def valid_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False
