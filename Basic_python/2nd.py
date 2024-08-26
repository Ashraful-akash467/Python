s=6
print("The value is :",s) 

a='''hi,how are you 
   there is nothing to see.
   I want to watch Demon Slayer Anime .'''
b="Akash"   
print(a)

print("The lanth of a :",len(a))   

print(a[0:6])
   
# for character in b:
#     print(character)

# for c in a:
#     print(c)


print("Hi")
x=input("Your name ? ")
print("Welcome",x)
z=int(input("Number  ???"))
print("Number is :",z)

if(z==0) :
   print("It is Zero",z)
else :
   print("Its not zero.its : ",z)


print("Hope you will be class soon.")
# x is type of list ,we can change the value of x[0],x[1] 
x=[1,2,3,6,9,11]

# r is a type of tuple ,we can not change the value of r[0],r[1]


r=(11,12,15)
print(r)


y='HI'
z="Hello"
print(x)
print(y)
print (z)
print("Type is" , type(x))

print('Hello world')

name = input("Your name ")
print("\n Hi", name)
print("Hope you will be class soon.")
print('ok')

print("Hope you will be class soon.")
# x is type of list ,we can change the value of x[0],x[1] 
x=[1,2,3,6,9,11]

# r is a type of tuple ,we can not change the value of r[0],r[1]


r=(11,12,15)
print(r)

y='HI'
z="Hello"
print(x)
print(y)
print (z)
print("Type is" , type(x))


letter=['a','b','c','d']
stg=['get','certified','get','ahead']
conc=letter+stg
print(conc)


num=[1,2,3,4]
one,*other=num
print(one)
print(other)


var=list("Hey There")
print(var)


num=[1,2,3,4]
stg=['get','certified','get','ahead']

num.append(7)
print(num)

num.extend(stg)
print(num)

num.insert(5,"Akash")
print(num)

num.remove("Akash")
print(num)



n=[1,2,3,4]
print("len",len(n))
print("min",min(n))
print("max",max(n))
print("sum",sum(n))
print("avareg",sum(n)/len(n))






                             # string

stg="Welcome to Simplification"
print(stg.upper())
print(stg.lower())

print(stg.find('o'))
print(stg.index('o'))

x=stg.split(" ")#split the string into list
print(x)

print(stg.replace("Simplification","Python tutorials"))#replace the string

print(stg.rpartition(" to ")) #split the string into truple

str1="good"
str2="morning"
print(str1+" "+ str2)

s1="Hey"
s2="There"
s3="all"
#Hey There , all

st="{} {} , {}!".format(s1,s2,s3)
print(st)





s='''Akash
you are very poor 
'''
for character in s:
  print(character)



