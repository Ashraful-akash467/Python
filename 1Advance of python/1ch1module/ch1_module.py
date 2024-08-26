#pip install pyttsx3  its for speak from computer 
#
#pip install pyjokes

import pyjokes

print("Print jokes")
joke = pyjokes.get_joke()
print(joke)

#speak
p=input("Enter your word : ")
import pyttsx3
e = pyttsx3.init()
e.say(p)
e.runAndWait()


import os
#Select the context whose content you want to list 
directory_path='/'
#use the os module to list the directory context
contents=os.listdir(directory_path)

print(contents)



p=input("Enter your word : ")
import pyttsx3
e = pyttsx3.init()
e.say(p)
e.runAndWait()
