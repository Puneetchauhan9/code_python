def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
print(fact(4))

# 
#lambda function
a = lambda b: b+5
print(a(5))

