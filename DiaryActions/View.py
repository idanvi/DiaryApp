from DiaryActions.AssistanceMethods import *

class View:

    # =============================================================#
    # this method find a specific event and display it to the user #
    # =============================================================#
    @staticmethod
    def viewDiaryEvent(Date, Title, eveList):
        if (eveList.__len__() == 0):
            return "Diary is Empty, No Events to View!"
        else:
            res = AssistanceMethods.checkDateInput(Date)
            if (res is True):
                for event in eveList:
                    if ((event["Date"] == Date) and (Title in event["Title"])):
                         return "Date: " + event["Date"] + " Title: " + event["Title"] + " Description: " + event["Description"]
                return "Event Not Found!"
            return res