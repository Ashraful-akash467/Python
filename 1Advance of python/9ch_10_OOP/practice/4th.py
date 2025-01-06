class Calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The sqare is {self.n*self.n}")

    def cube(self):
        print(f"The sqare is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The sqare is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello World .")

a= Calculator(4)
a.square()
a.cube()
a.hello()
a.squareroot()
