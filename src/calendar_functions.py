import csv

def add_calendar(calendar_file):
    print("You have selected Add Calendar - you can now add an activity to your calendar.")
    activity_title = input("Input the name of the activity you want to add to your calendar: ")
    activity_month = input("Input the name of the month that the activity will take place: ")
    activity_day = input("Input the day that the activity will take place (dd): ")
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
        if month.lower() == "january":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "february":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "march":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "april":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "may":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "june":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "july":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "august":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "september":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "october":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "november":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")
        if month.lower() == "december":
            input("Success! Press enter to continue.")
            print(i)
            input("Press enter to continue...")

    
def measure_calendar():
    pass
