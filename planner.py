import json


class Planner:
    def __init__(self, filePath):
        """
        Constructor of class
        Takes a filePath to file with data
        if filePath exists creates an object
        else returns nothing

        >>> a=Planner("dataagrbg.json")

        >>> a=Planner("test_data.json")

        """
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
        """
        Prints a dictionary of events

        >>> a=Planner("test_data.json")
        >>> a.printData()
        {'2017-04-23T18:25:43.511Z': '2', '2012-04-23T18:25:43.511Z': '3', '2011-04-23T18:25:43.511Z': 'blablabla'}

        """
        print(self.data)

    def get(self, date):
        """
        Returns string if date exists
        else returns nothing

        >>> a=Planner("test_data.json")
        >>> a.get("2012-04-23T18:25:43.511Z")
        '3'

        >>> a.get("2012-04-23T18:25:43.5Z")

        """
        return self.data.get(date)

    def getAll(self):
        """
        Returns a dictionary of events

        >>> a = Planner("test_data.json")
        >>> print(a.getAll())
        {'2017-04-23T18:25:43.511Z': '2', '2012-04-23T18:25:43.511Z': '3', '2011-04-23T18:25:43.511Z': 'blablabla'}

        """
        return self.data

    def add(self, date, note):
        """
        Returns True if date and note were added successfully
        else returns False

        >>> a=Planner("test_data.json")
        >>> a.add("2011-04-23T18:25:43.511Z","blablabla")
        True

        >>> a.add("2011-04-23T18:25:43.511Z","blablabla")
        False

        """
        if self.data.get(date) is not None:
            return False
        else:
            self.data[date] = note
            self.__save()
            return True

    def update(self, date, note):
        """
        Returns True if date and note were updated successfully
        else returns False

        >>> a=Planner("test_data.json")
        >>> a.update("2012-04-23T18:25:43.511Z","bla")
        True

        >>> a.update("2010-04-23T18:25:43.511Z","blablabla")
        False

        """
        if self.data.get(date) is not None:
            self.data.update({date: note})
            self.__save()
            return True
        else:
            return False

    def delete(self, date):
        """
        Returns True if date exists and event was deleted successfully
        else returns False

        >>> a=Planner("test_data.json")
        >>> a.delete("2012-04-23T18:25:47.511Z")
        True

        >>> a.delete("2010-04-23T18:25:43.511Z")
        False

        """
        try:
            self.data.pop(date)
            self.__save()
            return True
        except KeyError:
            return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
