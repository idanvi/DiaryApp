from AssistanceMethods import *

class DiaryActions:

    #***************************************************************
    # this method insert an event to diary                          
    #***************************************************************
    @staticmethod
    def insertEventToList(event, eveList):
        res = AssistanceMethods.checkDateInput(event.getDate())         # checks that date is in correct format
        if (res is True):
            newEvent = {"Date": event.getDate(), "Title": event.getTitle(), "Description": event.getDesc()}
            eveList.append(newEvent)
            return "Successfuly Added new Event to Diary: " + "Date: " + event.getDate() + " Title: " + event.getTitle() + " Description: " + event.getDesc()
        else:
            return res

    #***************************************************************
    # this method deletes an event from diary                       
    #***************************************************************
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
            else:
                return res

    #***********************************
    # this method updates an event
    #***********************************
    @staticmethod
    def updateDiaryEvent(oldDate, oldTitle, newDate, newTitle, newDesc, eveList):
        if (eveList.__len__() == 0):
            return "Diary is Empty, No Events to Update!"
        else:
            res1 = res2 = False
            res1 = AssistanceMethods.checkDateInput(oldDate)    # validate that given date is in the correct format
            if ( res1 != True ):
                return res1
            res2 = AssistanceMethods.checkDateInput(newDate)
            if ( res2 != True ):
                return res2
            if ( ( res1 is True ) and ( res2 is True ) ):
                for event in eveList:
                    if ( ( event["Date"] == oldDate ) and ( ( oldTitle in event["Title"] ) ) ):
                        event["Date"] = newDate
                        event["Title"] = newTitle
                        event["Desc"] = newDesc
                        return "Event Successfuly Updated: " + "Date: " + event["Date"] + " Title: " + event[
                            "Title"] + " Description: " + event["Desc"]
            return "Event Not Found!"

    #********************************************************
    # this method searches for events by their description       
    #********************************************************
    @staticmethod
    def searchEventByDesc(txt, eventsList):            
        if (eventsList.__len__() == 0):
            return "Diary is Empty, No Events to Search For!"
        else:
            resList = []
            for event in eventsList:
                if ( ( txt in event["Description"] ) or ( txt in event["Title"] ) ):
                    resList.append(event)
            if (resList):                                   # if the list is not empty
                resList = AssistanceMethods.sortListByDate(resList)
                return AssistanceMethods.fromListToString(resList)
        return "Event not Found!"

    #*************************************************
    # this method searches for events by date range          
    #*************************************************
    @staticmethod
    def searchByDateRange(From, To, eventsList):
        if (eventsList.__len__() == 0):
            return "Diary is Empty, No Events to Search For!"
        else:
            res1 = AssistanceMethods.checkDateInput(From)
            if ( res1 != True):
                return res1
            res2 = AssistanceMethods.checkDateInput(To)
            if ( res2 != True):
                return res2
            if ((res1 is True) and (res2 is True)):                 # if the given dates format is OK
                if (AssistanceMethods.checkDateRange(From, To)):    # checks if the given date range is OK
                    return AssistanceMethods.fromListToString(DiaryActions.searchBetweenDates(From, To, eventsList))
                else:  # if date range is incorrect
                    return "Date Range is Incorrect"

    #*****************************************************************************************************
    #  this is an assistant method. searches for events between date. used by searchByDateRange() method
    #*****************************************************************************************************
    @staticmethod
    def searchBetweenDates(From, To, eventsList):                   # returns all events between given 2 dates!
        foundEvents = []
        res1 = AssistanceMethods.checkDateInput(From)
        if ( res1 != True):
            return res1
        res2 = AssistanceMethods.checkDateInput(To)
        if ( res2 != True):
            return res2
        if ((res1 is True) and (res2 is True)):                     # if the given dates format is OK
            From = datetime.strptime(From, '%d-%m-%Y').date()       # transfer date from unicode into real value
            To = datetime.strptime(To, '%d-%m-%Y').date()
            for event in eventsList:
                eventDate = datetime.strptime(event["Date"], '%d-%m-%Y').date()
                if ((eventDate >= From) and (eventDate <= To)):
                    foundEvents.append(event)
            foundEvents = AssistanceMethods.sortListByDate(foundEvents)
            return foundEvents

    #**********************************************************************
    # this method searches for events by date range and event description
    #**********************************************************************
    @staticmethod
    def searchByDateAndDesc(From, To, txt, eventsList):            # search for events by given Dates and Description
        if (eventsList.__len__() == 0):
            return "Diary is Empty, No Events to Search For!"
        else:
            res1 = AssistanceMethods.checkDateInput(From)
            if (res1 != True):
                return res1
            res2 = AssistanceMethods.checkDateInput(To)
            if (res2 != True):
                return res2
            if ((res1 is True) and (res2 is True)):                 # if the given dates format is OK
                if (AssistanceMethods.checkDateRange(From, To)):    # checks if the given date range is OK
                    resList1 = DiaryActions.searchBetweenDates(From, To, eventsList)
                    resList2 = []
                    for event in resList1:
                        if ((txt in event["Description"]) or (txt in event["Title"])):
                            resList2.append(event)
                    resList2 = AssistanceMethods.sortListByDate(resList2)
                    return AssistanceMethods.fromListToString(resList2)
                else:                                               # if date range is incorrect
                    return "Dates Range is Incorrect"
