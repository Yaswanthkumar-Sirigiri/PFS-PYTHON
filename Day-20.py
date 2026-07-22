#GENERATOR
#(expr for var in collection/range)
#a=(i for i in range(21))
'''print(*a)
print(type(a))'''

#print(list(a))
#print(tuple(a))
#print(set(a))

'''a,b = (int(x) for x in input("Enter The values:").split(","))
def check(a,b):
    while a<b:
        yield a
        a = a+1
        yield a
print(*check(a,b))'''

'''a,b = (int(x) for x in input("Enter The values:").split(","))
def check(a,b):
    while a<b:
        a = a+1
        return a
print(*check(a,b))'''
        


#yield v/s return
'''def mygen():
    #return "vja"
    #return "hyd"
    #return "vzg"
    return "vja","hyd","vzg"
print(*mygen())'''


'''def mygen():
    yield "python"
    yield "java"
    yield "DSA"
print(*mygen())'''


#next()
'''d = mygen()
print(next(d))
print(next(d))
print(next(d))'''
#print (next(d)) stop iteration.y

