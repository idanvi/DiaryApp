from DiaryActions.AssistanceMethods import *

class Search:

    # ===============================================================#
    # this method searches for events by their description           #
    # ===============================================================#
    @staticmethod
    def searchEventByDesc(Desc, eventsList):
        if ( eventsList.__len__() == 0 ):
            return "Diary is Empty, No Events to Search For!"
        else:
            resList = []
            for event in eventsList:
                if ( Desc in event["Description"] ):
                    resList.append(event)
            resList = AssistanceMethods.sortListByDate(resList)
            return AssistanceMethods.fromListToString(resList)

            return "Event not Found!"

    # ===============================================================#
    # this method searches for events by date range                  #
    # ===============================================================#
    @staticmethod
    def searchByDateRange(From, To, eventsList):
        if ( eventsList.__len__() == 0 ):
            return "Diary is Empty, No Events to Search For!"
        else:
            res1 = AssistanceMethods.checkDateInput(From)
            res2 = AssistanceMethods.checkDateInput(To)
            if (( res1 is True ) and (res2 is True )):                  # if the given dates format is OK
                if (AssistanceMethods.checkDateRange(From, To)):        # checks if the given date range is OK
                    return AssistanceMethods.fromListToString( Search.searchBetweenDates( From, To, eventsList) )
                else:                                                   # if date range is incorrect
                    return "Dates Range is Incorrect"
            else:                                                       # if the given dates are not Ok, i check which one is incorrect
                str = ''
                if (res1 != "" and res1 != True):
                    str = "First Date Value: " + res1
                if (res2 != "" and res2 != True):
                    str += " ,Second Date Value: " + res2
                return str

    # ===================================================================================================#
    #  this is an assistant method. searches for events between date. used by searchByDateRange() method #                #
    # ===================================================================================================#
    @staticmethod
    def searchBetweenDates(From, To, eventsList):       #returns all events between given 2 dates!
        foundEvents = []
        res1 = AssistanceMethods.checkDateInput(From)
        res2 = AssistanceMethods.checkDateInput(To)
        if ((res1 is True) and (res2 is True)):                 # if the given dates format is OK
            From = datetime.strptime(From, '%d-%m-%Y').date()   #transfer date from unicode into real value
            To = datetime.strptime(To, '%d-%m-%Y').date()
            for event in eventsList:
                eventDate = datetime.strptime(event["Date"], '%d-%m-%Y').date()
                if ( ( eventDate >= From) and (eventDate <= To ) ):
                    foundEvents.append(event)
            foundEvents = AssistanceMethods.sortListByDate(foundEvents)
            return foundEvents
        else:                                                   # if the given dates are not Ok, i check which one is incorrect
            str=''
            if ( res1 != "" and res1 != True):
                str = "First Date Value: " + res1
            if (res2 != "" and res2 != True):
                str +=  " ,Second Date Value: " + res2
            return str

    # ====================================================================#
    # this method searches for events by date range and event description #
    # ====================================================================#
    @staticmethod
    def searchByDateAndDesc(From, To, Desc, eventsList):  # search for events by given Dates and Description
        if (eventsList.__len__() == 0):
            return "Diary is Empty, No Events to Search For!"
        else:
            res1 = AssistanceMethods.checkDateInput(From)
            res2 = AssistanceMethods.checkDateInput(To)
            if ((res1 is True) and (res2 is True)):                     # if the given dates format is OK
                if (AssistanceMethods.checkDateRange(From, To)):        # checks if the given date range is OK
                    resList1 = Search.searchBetweenDates(From, To, eventsList)
                    resList2 = []
                    for event in resList1:
                        if (Desc in event["Description"]):
                            resList2.append(event)
                    resList2 = AssistanceMethods.sortListByDate(resList2)
                    return AssistanceMethods.fromListToString(resList2)
                else:                                                   # if date range is incorrect
                    return "Dates Range is Incorrect"
            else:                                                       # if the given dates are not Ok, i check which one is incorrect
                str = ''
                if (res1 != "" and res1 != True):
                    str = "First Date Value: " + res1
                if (res2 != "" and res2 != True):
                   str += " ,Second Date Value: " + res2
                return str