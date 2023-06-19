greeting = "good morning, "
name = "karan"
print(type(name))
c = greeting + name # with the help of + operator we can concatenate the string
print(c)

# how to access a string by its index
name = "karan"
print(name[0])
print(name[4])

# this means that we want to print the strings from the index 0 to 3 from the string name
# this is called as string slicing
print(name[0:4])
print(name[:4]) # is the same as name[0:4]
print(name[0:]) # if we want to print the while name by string slicing

# string slicing by negative index's
c = name[-4:-1] # is same as name [1:4]
print(c)

# slicing with skip value
d = name[0::2] #this means it will skip every second string
print(d)