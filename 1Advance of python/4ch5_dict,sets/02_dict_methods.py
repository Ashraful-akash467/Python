mark = {
     "Akash":98,
     "Fuad":78,
     "Harry":89,
     "Rohan":56,
     0:"Harry"    
}
print("MArks :   ",mark)

print("Items :  ",mark.items())
print("Keys  :  ",mark.keys())
print("Values:  ",mark.values())

mark.update({"Akash":99,"Alip":87})
print("New mark:  ",mark)

print(mark.get("Akash"))
print(mark.get("Akash2"))
print(mark["Akash2"])


