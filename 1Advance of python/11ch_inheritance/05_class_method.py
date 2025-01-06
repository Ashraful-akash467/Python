class Employee:
    a = 1
    def show(self):
        print(f"The class attribute value is {self.a} .")
e= Employee()
e.a =45
e.show()

#------------------------------------------------------------------------------------------------------------------------------

class Employee1:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute value is {cls.a} .")
b= Employee1()
b.a =45
b.show()