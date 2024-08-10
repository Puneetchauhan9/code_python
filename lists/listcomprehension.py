a = [40,50,60]
# b = a.copy()
# print(b)
b =[]
for i in a:
 if i>40:
  b.append(i)

print(b)

# list comprehension Method()
c = [i for i in a if i > 40]
print(c)