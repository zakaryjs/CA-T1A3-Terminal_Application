import csv

def add_calendar(calendar_file):
    activity_title = ""
    activity_day = ""
    activity_month = ""
    print("You have selected Add Calendar - you can now add an activity to your calendar.")
    while activity_title == "":
        activity_title = input("Input the name of the activity you want to add to your calendar: ")
    while activity_month == "":
        activity_month = input("Input the name of the month that the activity will take place: ")
        while activity_month.lower() not in ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]:
            activity_month = input("Input the name of the month that the activity will take place: ")
    while activity_day == "":
        try:
            activity_day = int(input("Input the day that the activity will take place (dd): "))
        except ValueError as add_cal_value_error:
            print("Incorrect value. Please type a numerical value.")
    with open("calendar.csv", "a") as file:
        write_to_csv = csv.writer(file)
        write_to_csv.writerow([activity_title, activity_month, activity_day])
    input("Press enter to continue...")


def delete_calendar(calendar_file):
    print("You have selected Delete Calendar - you can now delete an activity from your calendar.")
    delete_activity = input("Input the name of the activity that you wish to delete: ")
    calendar_list = []
    with open("calendar.csv", "r") as file:
        read_csv = csv.reader(file)
        for row in read_csv:
            if(delete_activity != row[0]):
                calendar_list.append(row)
    input("Press enter to continue...")
    with open("calendar.csv", "w") as file:
        write_to_csv = csv.writer(file)
        write_to_csv.writerows(calendar_list)
    print("Updated calendar preview:")
    print(calendar_list)
    print("If the item you tried to delete is still in the list, it means it was not deleted correctly. Please try again.")
    input("Press enter to continue...")



def view_calendar(calendar_file):
    print("You have selected View Calendar - you can now view activities that are saved to a certain month in your calendar.")
    view_month = input("Input the name of the calendar month that you would like to view: ")
    view_calendar_list = []
    with open("calendar.csv", "r") as file:
        read_csv = csv.reader(file)
        for row in read_csv:
            view_calendar_list.append(row)
    # print(view_calendar_list[2])
    for i in view_calendar_list[2:]:
        month = i[1]
        if month.lower() == view_month.lower():
            print(i)
    
    input("Success! Press enter to continue...")

    
def measure_calendar(calendar_file):
    score = 0
    print("You have selected Measure Calendar. You can now select a month and receive an output based on how busy the selected month is.")
    view_month = input("Input the name of the calendar month that you would like to view: ")
    view_calendar_list = []
    with open("calendar.csv", "r") as file:
        read_csv = csv.reader(file)
        for row in read_csv:
            view_calendar_list.append(row)
    for i in view_calendar_list[2:]:
        month = i[1]
        if month.lower() == view_month.lower():
            score += 1

    if score >= 4:
        print(f"{view_month} is a really busy month!")
        input("Press enter to continue...")

    elif score >= 2:
        print(f"{view_month} is a relatively busy month!")
        input("Press enter to continue...")

    elif score >= 0:
        print(f"{view_month} is a really quiet month!")
        input("Press enter to continue...")
                