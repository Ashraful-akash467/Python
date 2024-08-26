# passwordcreak

from random import *
import os
u_pwd = input("Enter Password: ")
pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','1','2','3','4','5','6']

pw=""
while(pw!=u_pwd):
    for letter in range(len(u_pwd)):
        guess_pwd= pwd[randint(0,17)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Creaking Password....Please Wait few Minutes!")
        os.system("cls")

print("Your passprd is :",pw)

