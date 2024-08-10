a = ["Shiv","parvati","Maa gora","lakshmi","Vishnu","Shiv"]
# print(a)

# # for length of list
# print(len(a))
# # for add new element in last
# (a.append("panch Veer"))
# print(a)

# # add new element in specific position

# a.insert(1,"Ganesh")
# print(a)

# # to count occurance of particular Element
# print(a.count("Shiv"))

# # remove from list
# (a.remove("parvati"))
# print(a)

# # Remove From specific Index

# a.pop(1)
# print(a)

# Part 2 of Function of list

# to copy Same list
# b = a.copy()
# print(b)

# # TO find index of element

# print(a.index("Vishnu"))

# # TO extend the list
# c =["ganesh","Maa Parvati"]
# a.extend(c)
# print(a)

# REVERSE THE LIST WITHOUT SLICING

# print(a[::-1])  with slicing

a.reverse()
print(a)

# to sort the list
a.sort()
print(a)


# to clear all the data of list

a.clear()
print(a)
