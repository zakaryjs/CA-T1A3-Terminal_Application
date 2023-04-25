# Implementation Plan
## Zakary Sutherland

<hr>

## Features

1. Main Menu
Acts as the main interface for the application, presenting the user with a variety of options for what tasks can be completed with the application. These features include creating events, modifying events, viewing events and receiving an output depending on how many events are in a certain month.

2. Add Activity to Date
This applications main feature is the ability to add activities to specific days, like you would on a normal calendar. Multiple activities can be stored inside of one date, and the same activity can be stored inside of multiple different days.

3. Delete Activity from Date
This application also provides the user with the ability to remove activities from specific days, again, like you would on a normal calendar. Removal can happen at any point in time, and results in permanent event deletion from the calendar.

4. View Activities from a Month
This application provides the user with the ability to print all saved dates within a certain month. The dates and activities will be printed in a list format, to make sure that they are easy to view.

5. Month Output
This application also provides the user with the ability to request an output (one of three) that will determine how busy a users month is. The three available outputs are "This is a quiet month", "This is a relatively busy month", "This is a really busy month!".

Files will be output in CSV format after modifications have been made.

## How each Feature will be Implemented

1. Main Menu
Will be implemented with a main_menu function, printing all available features along with their associated inputs required for operation. This will be located in ```main.py```. 

2. Add Activity to Date
Will be implemented with an add_calendar function, allowing the user to input a date (month and day) as well as an activity name - with additional details if needed. This function will be located in ```add_calenar.py```.

3. Delete Activity from Date
Will be implemented with a delete_calendar function, allowing the user to input a date, view all of the activities associated with that date, and then delete a certain activity. This function will be located in ```delete_calendar.py```. 

4. View Activities from a Month
Will be implemented with a view_calendar function, allowing the user to input a month, and view all of the activities in said month. This function will be located in ```view_calendar,py```.

5. Month Output 
Will be implemented with a ```measure_calendar``` function, used in conjunction with the view_calendar function. This will provide an output depending on how many activities are stored in a certain month. The three available outputs are "This is a quiet month", "This is a relatively busy month", "This is a really busy month!".


Priorities, checklists all in Trello.


Develop an implementation plan which:
- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

Utilise a suitable project management platform to track this implementation plan.

Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan. 


> Your checklists for each feature should have at least 5 items.