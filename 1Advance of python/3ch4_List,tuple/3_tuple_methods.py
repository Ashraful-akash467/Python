a=(1,2,5,76,7,False,"rohan",76,76,345,34,54,"Akash")#We can not change tuple like string
print(a)

no=a.count(76)
print(no)



#Indexing: Access elements by their index.
t = (1, 2, 3)
print(t[0])  # Output: 1


# Slicing: Access a range of elements.
t = (1, 2, 3, 4, 5)
print(t[1:3])  # Output: (2, 3)

# Length: Get the number of elements in a tuple.
t = (1, 2, 3)
print(len(t))  # Output: 3

# Concatenation: Combine two or more tuples.
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4)

# Repetition: Repeat a tuple a given number of times.
t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)

# Membership: Check if an element exists in a tuple.
t = (1, 2, 3)
print(2 in t)  # Output: True

# Count: Count the number of occurrences of an element in a tuple.
t = (1, 2, 2, 3)
print(t.count(2))  # Output: 2

# Index: Find the index of the first occurrence of an element.
t = (1, 2, 3)
print(t.index(3))  # Output: 2

# Unpacking: Assign elements of a tuple to multiple variables.
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Output: 1 2 3


# Tuple Methods: While tuples do not have methods to modify them (since they are immutable), you can use the following built-in functions that work with tuples.

# max(tuple): Returns the maximum value in the tuple.
# min(tuple): Returns the minimum value in the tuple.
# sum(tuple): Returns the sum of all elements in the tuple.
# sorted(tuple): Returns a sorted list of the tuple’s elements.
t = (3, 1, 2)
print(max(t))  # Output: 3
print(min(t))  # Output: 1
print(sum(t))  # Output: 6
print(sorted(t))  # Output: [1, 2, 3]