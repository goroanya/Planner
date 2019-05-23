import json

class Planner:
    def __readJson__(self, filePath):
        with open(filePath) as json_file:
            data = json.load(json_file)
            return data

    def __init__(self, filePath):
        self.data = dict(self.__readJson__(filePath))

    def printData(self):
        print(self.data)

    def getNote(self, date):
        return self.data[date]

    def addNote(self, date, note):
        self.data[date] = note
        return self.data.get(date)

    def updateNote(self, date, note):
        if self.data.get(date) is not None:
            self.data.update({date: note})
            return self.data[date]

    def deleteNote(self, date):
        if self.data.get(date) is not None:
            return self.data.pop(date)


planner = Planner('data.json')
planner.printData()
print(planner.deleteNote('2012-04-23T8:25:43.511Z'))
planner.printData()

