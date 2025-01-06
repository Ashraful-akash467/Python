# 7. Write a python function to remove a given word from a list ad strip it at the same 
#     time.


l=["Akash","Harry","Rohan","Shubham","an"]

def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

    for item in l:
         l.remove(word)
         return l
print(rem(l,"an"))        


