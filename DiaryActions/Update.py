from DiaryActions.AssistanceMethods import *

class Update:

    # ================================#
    # this method updates an event    #
    # ================================#
    @staticmethod
    def updateDiaryEvent(oldDate, oldTitle, newDate, newTitle, newDesc, eveList):
        if (eveList.__len__() == 0):
            return "Diary is Empty, No Events to Update!"
        else:
            res1 = res2 = False
            res1 = AssistanceMethods.checkDateInput(oldDate)        # validate that given date is in the correct format
            res2 = AssistanceMethods.checkDateInput(newDate)
            if ( ( res1 is True ) and (res2 is True ) ):
                for event in eveList:
                    if ((event["Date"] == oldDate) and ((oldTitle in event["Title"] ))):
                        event["Date"] = newDate
                        event["Title"] = newTitle
                        event["Desc"] = newDesc
                        return "Event Successfuly Updated: " + "Date: " + event["Date"] + " Title: " + event["Title"] + " Description: " + event["Desc"]
            else:                                                       # if the given dates are not Ok, i check which one is incorrect
                str = ''
                if (res1 != "" and res1 != True):
                    str = "First Date Value: " + res1
                if (res2 != "" and res2 != True):
                   str += " ,Second Date Value: " + res2
                return str
            return "Event Not Found!"