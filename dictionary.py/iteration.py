School ={
    "Name":"John",
    "Age":20,
    "Class":"5th"
}

# iteration of only Keys
# for i in School:
#     print(i)    #Acess of all Keys

# Acess of all VAlues
# for i in School:
#     print(School[i])

# for i in School.values():
#     print(i)

# for both Ek sath
for i,j in School.items():
    print(i,":",j)