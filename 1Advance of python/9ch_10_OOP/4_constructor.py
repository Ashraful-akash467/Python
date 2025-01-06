class employ :
    language ="Python"     #This is a class attribute 
    salary=1300000

    def __init__(self,name,language,salary):   #dundur method which is autometically called 
        self.name=name
        self.language=language
        self.salary=salary
        print("I am creating an object.I am in Dundur method .")


    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}.")
    

    @staticmethod
    def greet():
        print("Good Morning .")


akash =employ("Akash","C++",1200000)
       
print(f"Name {akash.name},Language {akash.language},Salary {akash.salary}")

akash.getInfo()   #employ.getInfo(akash)
akash.greet()



