class employ :
    language ="Python"     #This is a class attribute 
    salary=1200000


    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}.")
    

   

akash =employ()
akash.language="JavaScript"          #This is an instance attribute 
print(akash.language,akash.salary)





