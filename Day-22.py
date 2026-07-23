#ANONYMOUS FUNCTIONS(NAMELESS FUNCTIONS):
#write a function to calculate 2*x+5 where x=5
'''def f():
    a = 2*x+5
    print(a)
calc(5)'''


'''def f():
    x = int(input())
    print(2*x+5)
f()'''  #Runtime


#SYNTAX
#a = lambda arg:expr
'''a = lambda x:2*x+5
print(a(5))'''


'''a = int(input())
b = lambda x:2*x+5
print(b(a))'''  #Runtime


#Task-1
'''a = lambda b,c:b*c
print(a(5,4))'''


'''b = int(input(""))
c = int(input(""))
a = lambda b,c:b*c
print(a(b,c))'''  #Runtime


#Task-2
'''a = input("")
b = lambda a:a.upper()
print(b(a))'''


#Task-3
'''a = input("")
b = lambda a:a.title()
print(b(a))'''


#Task-4
'''fname = input("")
lname = input("")
fullname = lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''


'''fname,lname = (str(x) for x in input("--->").split(","))
fullname = lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''   #using generator


#Task-5
a = [10,20,23,25,67,45,80,90,97,85,100]
'''for i in a:
    if i%2==0:
        print(i,end=" ")'''


#FILTER()
'''b = list(filter(lambda x:x%2==0,a))
print(b)'''

'''b = list(filter(lambda x:x%2!=0,a))
print(b)'''


#[],(),{}
'''a = []
print(type(a))

b = ()
print(type(b))

c = {}
print(type(c))

d = set()
print(type(d))'''


#Should skip all the Empty datatypes.
'''a = [[],(),set(),{}," ",None,3,5.6,"Yaswanth",4+9j,True,False]
print(list(filter(None,a)))'''
    
    
