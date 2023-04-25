import datetime
from datetime import date
import calendar
# from colored import fg, bg, attr
from calendar_functions import add_calendar, delete_calendar, view_calendar, measure_calendar
import csv

csv_file = "calendar.csv"

print("""
███████╗░█████╗░░█████╗░██╗░░░░░███████╗███╗░░██╗██████╗░░█████╗░██████╗░
╚════██║██╔══██╗██╔══██╗██║░░░░░██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗
░░███╔═╝██║░░╚═╝███████║██║░░░░░█████╗░░██╔██╗██║██║░░██║███████║██████╔╝
██╔══╝░░██║░░██╗██╔══██║██║░░░░░██╔══╝░░██║╚████║██║░░██║██╔══██║██╔══██╗
███████╗╚█████╔╝██║░░██║███████╗███████╗██║░╚███║██████╔╝██║░░██║██║░░██║
╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝""")
print("Welcome to zCalendar, a calendar application created in Python.")
print("Enjoy!")

def main_menu():
    print("1. Input 1 to add an activity to the calendar")
    print("2. Input 2 to remove an activity from the calendar")
    print("3. Input 3 to view activities stored in a certain month")
    print("4. Input 4 to see how busy a certain month is")
    print("5. Input 5 to end the application")
    user_input = input("What would you like to do? ")
    return user_input

decision = ""

while decision != "5":
    decision = main_menu()

    if (decision == "1"):
        add_calendar()
    elif (decision == "2"):
        pass
    elif (decision == "3"):
        pass
    elif (decision == "4"):
        pass
    elif (decision == "5"):
        pass
    else:
        print("Invalid input. Please return an input between 1 and 5.")


print("You have ended zCalendar. I hope you enjoyed the program!")