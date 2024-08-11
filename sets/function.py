a ={"puneet","Chauhan","Khushi","Jatin","Ritesh","Ruchika"}
b ={"Shiv","maa Sati","PArvati"}
c ={"puneet","Khushi","panch veer"}
# a.add("Ram")
# print(a)

# a.pop()
# print(a)

# a.remove("puneet")
# print(a)

# isdisjoint matlab ek bhi similliar Element nhi hona
# print(a.isdisjoint(b))

# issubset
# print(a.issubset(b))
# print(c.issubset(a))

# issuperset
print(a.issuperset(c))

# update
a.update(c)
print(a)

a.update(b)
print(a)

c.update(b)
print(c)

a.clear()
print(a)

