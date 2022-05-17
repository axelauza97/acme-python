from company import Company
from file import File
from parser import Parser

from person import Person

class Main():
    def start():
        file=File("./salary.txt")
        file.read()
        parser=Parser(file.getContents())
        person=Person(list(parser.getData().keys())[0])
        company=Company()
        company.payEmployee(person,parser.getData()[person.getName()])
        print("La persona recibirá "+ person.getName()+" "+str(person.getPayment()))


if __name__ == "__main__":
    Main.start()