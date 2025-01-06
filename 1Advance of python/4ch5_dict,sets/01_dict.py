mark = {
     "Akash":98,
     "Fuad":78,
     "Harry":89,
     "Rohan":56 ,
     0:"Harry"   
}

#mark=[["Akash",98],] list of list.  its ok but we can not find the index result

print(mark,type(mark))

# print(mark[0])   It will not work here

print(mark["Akash"])

print(mark.get("Akash"))
print(mark.get("Akash2"))