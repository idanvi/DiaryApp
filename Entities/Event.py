
class Event:
    def __init__(self, date, title, desc):
        self.date = date
        self.title = title
        self.desc = desc


    def getDate(self):
        return self.date

    def getTitle(self):
        return self.title

    def getDesc(self):
        return self.desc


