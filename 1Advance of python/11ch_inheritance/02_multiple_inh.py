class Employee:
    Company="ASK"
    name="Defult Name"

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.Company} .")

class Coder:
    Language="Pyhon"
    
    def printLenguage(self):
        print(f"All the language is here -your languafge is {self.Language} language")


class Programmer(Employee, Coder):
    Company="AKS Infotyech"
    def showLanguage(self):
         print(f"The name is {self.Company} and the salary is {self.Company}") 


a=Employee()  
b=Programmer()

b.show()
b.printLenguage()
b.showLanguage()
