import json


class Planner:
    def __init__(self, filePath):
        self.filePath = filePath
        self.data = dict(self.__load())

    def __load(self):
        try:
            with open(self.filePath, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return []

    def __save(self):
        with open(self.filePath, 'w') as json_file:
            json_file.write(json.dumps(self.data))

    def printData(self):
        print(self.data)

    def get(self, date):
        return self.data.get(date)

    def add(self, date, note):
        if self.data.get(date) is not None:
            return False
        else:
            self.data[date] = note
            self.__save()
            return True

    def update(self, date, note):
        if self.data.get(date) is not None:
            self.data.update({date: note})
            self.__save()
            return True
        else:
            return False

    def delete(self, date):
        try:
            self.data.pop(date)
            self.__save()
            return True
        except KeyError:
            return False
    
    def getAll(self):
        return self.data

