class Programmer :
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Akash",22000,1996)
print(p.company,p.name,p.pin,p.salary)

r=Programmer("Rohan",12000,1996)
print(r.company,r.name,r.pin,r.salary)
