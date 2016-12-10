from DiaryActions.AssistanceMethods import *

class Insert:

    # ===============================================================#
    # this method insert an event to diary                           #
    # ===============================================================#
    @staticmethod
    def insertEventToList(event, eveList):
        res = AssistanceMethods.checkDateInput(event.getDate())     #checks that date is in correct format
        if (res is True):
            newEvent = {"Date" : event.getDate(), "Title" : event.getTitle(), "Description" : event.getDesc()}
            eveList.append(newEvent)
            return "Successfuly Added new Event to Diary: " + "Date: " + event.getDate() + " Title: " + event.getTitle() + " Description: " + event.getDesc()
        else:
            return res
