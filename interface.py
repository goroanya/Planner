from planner import Planner
import io
import sys
import os
import pprint

planner = Planner('data.json')

# windows
# def clear():
#     return os.system('cls')

# linux
def clear():
    return os.system('clear')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


clear()
print("Welcome to your diary!!!")

while(input != "E\n" and input != "e\n"):

    print("Please choose one of the folowing actions")
    print(bcolors.BOLD + "\n(C)reate ")
    print("(R)ead ")
    print("(U)pdate ")
    print("(D)elete ")
    print("(E)xit" + bcolors.ENDC)

    input = sys.stdin.readline()

    clear()

    if(input == "C\n" or input == "c\n"):
        print(
            "Input your  date in format (ISO 8601) [yyyy/mm/dd/Thr:min:secondsZ] {space} your actual notation\n")
        print('All notes: ')

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(planner.getAll())

        inputSTR = sys.stdin.readline()

        print(bcolors.WARNING + ("There is already exist this date", "Added")[planner.add(inputSTR[0:inputSTR.find(
            " ")], inputSTR[inputSTR.find(" ")+1: -1])] + bcolors.ENDC)

        sys.stdin.readline()

    elif(input == "R\n" or input == "r\n"):
        print(
            "Input your date in format (ISO 8601) [yyyy/mm/dd/Thr:min:secondsZ]\n")
        print('All notes: ')

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(planner.getAll())

        inputSTR = sys.stdin.readline()

        value = planner.get(inputSTR.replace("\n", ""))

        print(bcolors.WARNING + ("Date doesnt exist", "Note: ")
              [value is not None] + bcolors.ENDC, value)

        sys.stdin.readline()

    elif(input == "U\n" or input == "u\n"):
        print(
            "Input your date in format (ISO 8601) [yyyy/mm/dd/Thr:min:secondsZ] {space} your new notation\n")
        print('All notes: ')

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(planner.getAll())

        inputSTR = sys.stdin.readline()
        print(bcolors.WARNING + ("Not updated (date doesnt exist)", "Updated")[planner.update(inputSTR[0:inputSTR.find(
            " ")], inputSTR[inputSTR.find(" ")+1: -1])] + bcolors.ENDC)

        sys.stdin.readline()

    elif(input == "D\n" or input == "d\n"):
        print(
            "Input your date in format (ISO 8601) [yyyy/mm/dd/Thr:min:secondsZ]\n")
        print('All notes: ')

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(planner.getAll())

        inputSTR = sys.stdin.readline()

        print(bcolors.WARNING + ("Not deleted (date doesnt exist)", "Deleted")
              [planner.delete(inputSTR.replace("\n", ""))] + bcolors.ENDC)

        sys.stdin.readline()

    clear()

print("Good bye!")
