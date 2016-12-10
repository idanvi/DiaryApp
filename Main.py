from flask import Flask
from Entities.Event import Event
from DiaryActions.Insert import *
from DiaryActions.Update import *
from DiaryActions.Delete import *
from DiaryActions.View import *
from DiaryActions.Search import *

app = Flask(__name__)
eventsList = []

#==================================================================#
# localhost:5000/   shows the diary's API                          #
#==================================================================#
@app.route("/")
def userMenu():
    return """ <b>Welcome to your new Web Event Diary!</b> <br>
                The operations are:<br><br>
                    1. Insert New Event - /<b>insert</b> , date , title , description <br><br>
                    2. View Event - /<b>view</b> , date , title<br><br>
                    3. Update Event - /<b>update</b> , date , title , newdate , newtitle , newdescription<br><br>
                    4. Delete Event - /<b>delete</b> , date , title<br><br>
                    5. Search By Date Range - /<b>searchByDates</b> , mindate , maxdate<br><br>
                    6. Search By Description - /<b>searchByDesc</b> , description<br><br>
                    7. Search By Dates Range and Description - /<b>searchByDatesAndDesc</b> , mindate , maxdate , description <br><br>

                <b>Note: Date Format is : DD-MM-YYYY </b><br><br>""" + "# Of Events in diary: " + str( eventsList.__len__() )

#=======================================================#
#Insert new event                                       #
#=======================================================#
@app.route("/insert,<date>,<title>,<desc>")
def insertEvent(date, title, desc):
    newEvent = Event(date, title, desc)
    return Insert.insertEventToList(newEvent, eventsList)

#=======================================================#
#update event                                           #
#=======================================================#
@app.route("/update,<oldDate>,<oldTitle>,<newDate>,<newTitle>,<newDesc>")
def updateEvent(oldDate, oldTitle, newDate, newTitle, newDesc):
    return Update.updateDiaryEvent(oldDate, oldTitle, newDate, newTitle, newDesc, eventsList)

#=======================================================#
#delete event                                           #
#=======================================================#
@app.route("/delete,<date>,<title>")
def deleteEvent(date, title):
    return Delete.deleteDiaryEvent(date, title, eventsList)

#=======================================================#
#view event                                             #
#=======================================================#
@app.route("/view,<date>,<title>")
def viewEvent(date, title):
    return View.viewDiaryEvent(date, title, eventsList)

#=======================================================#
#search for events by description                       #
#=======================================================#
@app.route("/searchByDesc,<Desc>")
def searchByDesc(Desc):
    return Search.searchEventByDesc(Desc, eventsList)

#=======================================================#
#search for events by date range                        #
#=======================================================#
@app.route("/searchByDates,<Date1>,<Date2>")
def searchByDates(Date1, Date2):
    return Search.searchByDateRange(Date1, Date2, eventsList)

#=======================================================#
#search for events by date range and description        #
#=======================================================#
@app.route("/searchByDatesAndDesc,<Date1>,<Date2>,<Desc>")
def searchByDatesAndDesc(Date1, Date2, Desc):
    return Search.searchByDateAndDesc(Date1, Date2, Desc, eventsList)
