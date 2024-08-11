School ={
    "Name":"John",
    "Age":20,
    "Class":"5th"
}
# get by this we can get any value
b = School.get("Class")
print(b)

# items can fetch dictionary in form of tuples
c = School.items()
print(c)

# keys
d = School.keys()
print(d)
# values
e =School.values()
print(e)

# copy
f = School.copy()
print(f)