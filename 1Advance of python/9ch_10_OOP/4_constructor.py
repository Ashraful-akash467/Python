class employ :
    language ="Python"     #This is a class attribute 
    salary=1200000

    def __init__(self,name,language,salary):   #dundur method which is autometically called 
        self.name=name
        self.language=language
        self.salary=salary
        print("Iam creating an object.")


    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}.")
    

    @staticmethod
    def greet():
        print("Good Morning .")


akash =employ("Akash",1300000,"C++")
       
print(akash.name,akash.language,akash.salary)

# akash.getInfo()#employ.getInfo(akash)
# akash.greet()



