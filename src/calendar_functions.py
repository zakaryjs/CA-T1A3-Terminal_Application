import csv

def add_calendar(calendar_file):
    print("You have selected Add Calendar - you can now add an activity to your calendar.")
    activity_title = input("Input the name of the activity you want to add to your calendar: ")
    activity_date = input("Input the date that the activity will take place (dd/mm): ")
    with open("calendar.csv", "a") as file:
        write_to_csv = csv.writer(file)
        write_to_csv.writerow([activity_title, activity_date])
    input("Press enter to continue...")


def delete_calendar():
    pass

def view_calendar():
    pass

def measure_calendar():
    pass
