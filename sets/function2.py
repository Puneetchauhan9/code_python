a ={"puneet","Chauhan","Khushi","Jatin","Ritesh","Ruchika"}
b ={"Shiv","maa Sati","PArvati"}
c ={"puneet","Khushi","panch veer"}


# x = a.union(c)
# print(x)

# x = a.intersection(c)
# print(x)

# x = a.difference(c)
# print(x)

# a.difference_update(c)
# print(a)

x = a.symmetric_difference(c)
print(x)  #common ko chod ke sara

a.symmetric_difference_update(c)
print(a)