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
