class Employee1:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute a is {cls.a} .")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]        
        self.lname = value.split(" ")[1]        

b= Employee1()
b.a =45

b.name= "Ashraful Akash"
print(b.fname, b.lname)

b.show()


#abstructionn and incapsulation 

#incapsulation -> we can not see the implementetion details @name.setter  .....
#  we do so many work and pack them in Employee class

#abstruction ->we hide incapsulation details
