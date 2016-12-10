from DiaryActions.AssistanceMethods import *

class Delete:

    # ===============================================================#
    # this method deletes an event from diary                        #
    # ===============================================================#
    @staticmethod
    def deleteDiaryEvent(eveDate, eveTitle, eveList):
        if (eveList.__len__() == 0):
            return "Diary is Empty, No Events to Delete!"
        else:
            res = AssistanceMethods.checkDateInput(eveDate)
            if (res is True):
                for event in eveList:
                    if ((event["Date"] == eveDate) and ((event["Title"] == eveTitle))):
                        eveList.remove(event)
                return "Event Successfuly Deleted"
            return "Delete Failed, Event was Not Found!"
