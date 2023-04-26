import csv

def add_calendar(calendar_file):
    print("You have selected Add Calendar - you can now add an activity to your calendar.")
    activity_title = input("Input the name of the activity you want to add to your calendar: ")
    activity_date = input("Input the date that the activity will take place (dd/mm): ")
    with open("calendar.csv", "a") as file:
        write_to_csv = csv.writer(file)
        write_to_csv.writerow([activity_title, activity_date])
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



def view_calendar():
    pass

def measure_calendar():
    pass
