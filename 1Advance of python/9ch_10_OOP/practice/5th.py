from random import randint

class Train:

    def __init__(self, traino):
        self.traino = traino

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.traino} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.traino} is running on time .")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no : {self.traino} from {fro} to {to} is {randint(222, 5555)}")

w = Train(12399)
w.book("Dhaka" , "Tangail")
w.getStatus()
w.getFare("Mymenshing","Dhaka")


