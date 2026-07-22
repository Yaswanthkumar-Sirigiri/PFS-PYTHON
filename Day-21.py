#BUILT-IN FUCNTIONS
'''print(dir())
print(dir("___builtins___"))'''

'''a = "codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))'''

#print(dict(a)) #Error

#FROMKEYS()
'''b = dict.fromkeys(a)
print(b)

c = dict.fromkeys(a,"Yaswanth")
print(c)

c["d"] = "sam"
print(c)'''


#EVAL()
'''while True:
    a = int(input("a value: "))
    b = int(input("b value: "))
    print(a+b)'''#Only accepts int

'''while True:
    a = float(input("a value: "))
    b = float(input("b value: "))
    print(a+b)'''  #accepts both int and float but not string

'''while True:
    a = str(input("a value: "))
    b = str(input("b value: "))
    print(a+b)'''   #accepts all datatypes but concatenates instead of addition.

'''while True:
    a = eval(input("a value: "))
    b = eval(input("b value: "))
    print(a+b)'''    #accepts all the datatypes along with suitable operations.

#ZIP() -> we can combine multiple.
#ONE COLLECTION
'''a = [10,20,30,40,50]
names = ["Fine","You","Are","How","Hello"]
print(a+names) #merges two lists

b = zip(a,names)
print(b)       #Return logic error in binary format.

c = list(zip(a,names))
print(c)       #zipping list

c = tuple(zip(a,names))
print(c)       #zipple tuple

c = set(zip(a,names))
print(c)       #zipping set

c = dict(zip(a,names))
print(c)'''    #zipping dictionary.


#ENUMERATE()
#names = ["fine","vanakkam","namaste","hi","hello"]
'''for i in range(len(names)):
    print(i,names[i])''' #we can give the count to list using for loop.

'''b = dict(enumerate(names)) #we can use enumerate built-in function.
print(b)

b = dict(enumerate(names,100))
print(b)

b = list(enumerate(names))
print(b)

b = tuple(enumerate(names))'''


#ASCII()-->American standard code for information interchange.
#used for converting letters to binary -->chr() / ord()

#chr()
'''print(chr(65))

print(chr(90))

print(chr("a"))'''  #Error

#ord()
'''print(ord("a"))

print(ord("z"))

print(ord(67))'''  #Error


#Task-1
'''for i in range(ord("A"),ord("Z")+1):
    print(chr(i),end=" ")

print("\n")

for i in range(ord("a"),ord("z")+1):
    print(chr(i),end=" ")'''


#Task-2
'''inp = input("Enter your name: ")
a = list(inp)
for i in a:
    print(i,ord(i))'''


#MAX(),MIN(),SUM()
'''print(max(2,3,4,5,1,67,8,1))

print(min(2,3,4,5,1,67,8,1))'''

#print(sum(2,3,4,5,1,67,8,1))  #error

#print(sum(2,3))  #error

'''a = 2,3,4,5,1,67,8,1
print(sum(a))'''


#Task-3:
n = int(input("Enter student count: "))
a = []
for i in range(1,n+1):
    score = int(input(f"Student {i} marks: "))
    a.append(score)
print("~~~~~~~~Marks Report~~~~~")
print("Maximum: ",max(a))
print("Minimum:",min(a))
print("Sum of all marks:",sum(a))
print("Average: ",sum(a)/n)

