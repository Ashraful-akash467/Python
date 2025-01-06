class Employee:
    Company="ASK"
    def show():
        print(f"The name of the Employee is {self.name} and the salary is {self.salary} .")

# class Programmer:
#     Company="AKS Infotyech"

#     def show():
#         print(f"The name is {self.name} and the salary is {self.salary}")        

#     def showLanguage():
#         print(f"The name is {self.name} and the salary is {self.salary}") 


class Programmer(Employee):
    Company="AKS Infotyech"

    def show():
         print(f"The name is {self.name} and the salary is {self.salary}") 

    def showLanguage():
         print(f"The name is {self.name} and the salary is {self.salary}") 

a=Employee()        
b=Programmer()
print(a.Company, b.Company)

