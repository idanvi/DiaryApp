import unittest
from DiaryActions.AssistanceMethods import *


#***********************************************************************
# this class contains all the unit testing methods for the date parsing 
#***********************************************************************
class DateInputTest(unittest.TestCase):

    def setUp(self):
        self.date1 = '10-10-1985'
        self.date2 = '18-09-1987'
        self.date3 = '37-10-1995'   #incorrect data
        self.date4 = '-1-11-1990'   #incorrect  data
        self.date5 = '08-09-201'    #incorrect  data
        self.date6 = 'xxx'          #incorrect  data
        self.date7 = ''             # incorrect  data

    def testCorrectDateInput1(self):
        self.assertEqual(AssistanceMethods.checkDateInput(self.date1), True)

    def testCorrectDateInput2(self):
        self.assertEqual(AssistanceMethods.checkDateInput(self.date2), True)

    def testIncorrectDateInput3(self):
        self.assertEqual(AssistanceMethods.checkDateInput(self.date3), "Incorrect Data Format OR Invalid Date !")

    def testIncorrectDateInput4(self):
        self.assertEqual(AssistanceMethods.checkDateInput(self.date4), "Date is not Valid!")

    def testIncorrectDateInput5(self):
        self.assertEqual(AssistanceMethods.checkDateInput(self.date5), "Incorrect Data Format OR Invalid Date !")

    def testIncorrectDateInput6(self):
        self.assertEqual(AssistanceMethods.checkDateInput(self.date6), "Incorrect Data Format OR Invalid Date !")

    def testIncorrectDateInput6(self):
        self.assertEqual(AssistanceMethods.checkDateInput(self.date7), "Date is empty, Can't Add Event to Diary!")



#*************************************************************************************
# this class contains all the unit testing methods of sorting list of events by date 
#*************************************************************************************
class sortList(unittest.TestCase):

    def setUp(self):
        self.List1 = [{"Date" : "10-10-2016", "Title" : "Meeting with noa at the mall", "Description" : "be there at 4pm"}, {"Date" : "18-09-2016", "Title" : "Dentist appointment at 7:30pm", "Description" : "brush my teeth!"}, {"Date" : "21-12-2016", "Title" : "I'm getting married!", "Description" : "be there at 6pm"}]
        self.resList = [{"Date" : "18-09-2016", "Title" : "Dentist appointment at 7:30pm", "Description" : "brush my teeth!"}, {"Date" : "10-10-2016", "Title" : "Meeting with noa at the mall", "Description" : "be there at 4pm"}, {"Date" : "21-12-2016", "Title" : "I'm getting married!", "Description" : "be there at 6pm"}]

    def testsortList1(self):
        self.assertEqual(AssistanceMethods.sortListByDate(self.List1), self.resList)

if __name__ == '__main__':
    unittest.main()