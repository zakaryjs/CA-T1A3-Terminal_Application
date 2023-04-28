import datetime
from datetime import date
import calendar
# from colored import fg, bg, attr
from calendar_functions import add_calendar, delete_calendar, view_calendar, measure_calendar
import csv

file = "calendar.csv"

try:
    calendar_file = open(file, "r")

    calendar_file.close()

except FileNotFoundError as file_not_found:
    print("calendar.csv not found, initialising set up...")
    while True:
        try:
            year = int(input("Input the calendar year: "))
            break
        except ValueError as value_error:
            print("Incorrect value, please type a year.")
    print("Success!")
    input("Press enter to continue...")
    print("For a guide on how to use the application, please visit https://github.com/zakaryjs/T1A3-Terminal_Application")
    input("Press enter to continue...")
    calendar_file = open(file, "w")
    calendar_file.write(f"Year: {year}\n")
    calendar_file.write("Activity_Title, Month, Day\n")
    calendar_file.close()


print("""
███████╗░█████╗░░█████╗░██╗░░░░░███████╗███╗░░██╗██████╗░░█████╗░██████╗░
╚════██║██╔══██╗██╔══██╗██║░░░░░██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗
░░███╔═╝██║░░╚═╝███████║██║░░░░░█████╗░░██╔██╗██║██║░░██║███████║██████╔╝
██╔══╝░░██║░░██╗██╔══██║██║░░░░░██╔══╝░░██║╚████║██║░░██║██╔══██║██╔══██╗
███████╗╚█████╔╝██║░░██║███████╗███████╗██║░╚███║██████╔╝██║░░██║██║░░██║
╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝""")
print("Welcome to zCalendar, a calendar application created in Python.")
print("Enjoy!")

input("Press enter to continue...")

def main_menu():
    print("MAIN MENU:")
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
        add_calendar(calendar_file)
    elif (decision == "2"):
        delete_calendar(calendar_file)
    elif (decision == "3"):
        view_calendar(calendar_file)
    elif (decision == "4"):
        measure_calendar(calendar_file)
    elif (decision == "5"):
        pass
    else:
        print("Invalid input. Please return an input between 1 and 5.")
        input("Press enter to continue...")


print("You have ended zCalendar. I hope you enjoyed using the program!")