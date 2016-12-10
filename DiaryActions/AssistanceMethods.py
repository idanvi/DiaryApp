from datetime import datetime

class AssistanceMethods:

    # ==================================================================#
    # this method converts a given list of events to one long string    #
    # ==================================================================#
    @staticmethod
    def fromListToString(eList):
        if (eList.__len__() == 0 ):
            return "No Events were Found Between those Dates!"
        else:
            tmpStr = ""
            for event in eList:
                eStr = "Date: " + event["Date"] + " Title: " + event["Title"] + " Description: " + event["Description"] + "<br />"
                tmpStr += eStr
            return tmpStr

    # ==================================================================#
    # this method validates date format                                 #
    # ==================================================================#
    @staticmethod
    def checkDateInput(Date):
        if (Date is "" ):
            return "Date is empty, Can't Add Event to Diary!"
        else:
                tmpDate = Date.split('-')
                if ( len(tmpDate) != 3):
                    return "Date is not Valid!"
                try:
                    datetime.strptime(Date, '%d-%m-%Y').date()
                except ValueError:
                    return "Incorrect Data Format OR Invalid Date !"
        return True

    # ======================================================================#
    # this method sorts a given events list by their date (earlier to later #
    # ======================================================================#
    @staticmethod
    def sortListByDate(eveList):
        return sorted(eveList)

    # ===============================================================#
    # this method checks if 2 given dates are in chronological order #
    # ===============================================================#
    @staticmethod
    def checkDateRange(From, To):
         return ( datetime.strptime(From, '%d-%m-%Y') < datetime.strptime(To, '%d-%m-%Y') )
