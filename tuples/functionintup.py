a = ("Puneet","Ram","Shiv","Shakti")
# a.append("jai") functions cannot work on tupels we can covert it into list and then do what do and then convert  tuples
# b = list(a)
# print(type(b))
# b.append("Jai")
# print(type(b))
# print(b)
# a = tuple(b)
# print(type(a))
# print(a)

# all function are applicable tuple have also three functions 1) len 2) count 3)index
print(len(a))
print(a.count("Ram"))
print(a.index("Shiv"))