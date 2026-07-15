#FUNCTIONS
'''a = 100
b = 200
print("The sum is: ",a+b)
print("The diff is: ",a-b)
print("The product is: ",a*b)'''
'''a = 200
b = 500
print("The sum is: ",a+b)
print("The diff is: ",a-b)
print("The product is: ",a*b)'''        #Without using Functions
'''a = 1000
b = 4000
print("The sum is: ",a+b)
print("The diff is: ",a-b)
print("The product is: ",a*b)'''


'''def calculate(a,b):
    print("The sum is: ",a+b)
    print("The diff is: ",a-b)
    print("The product is: ",a*b)        #With using Functions.
calculate(100,200)
calculate(200,500)
calculate(1000,4000)'''


'''def calc(a,b):
    print("The Power value: ",a**b)
    print("The modulus value: ",a%b)     #**,%,//
    print("The Division value: ",a//b)
calc(5,2)
calc(8,3)
calc(4,5)'''


'''while True:
    def add():
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))     #Runtime input
        print(a+b)
    add()'''


'''def fullname():
    a = input("Enter First name: ")
    b = input("Enter Last name: ")       #Use-case:1
    print(("HELLO "+a+" "+b).title())
fullname() '''


#print v/s return
'''def mul(a,b):
    print(a*b)
mul(4,6)'''


'''def mul(a,b):
    return a*b
print(mul(7,3))'''


'''def cal(a,b):
    c = a+b
    d = a-b
    e = a*b
    print(c)
    print(d)
    print(e)
cal(56,65)'''


'''def cal(a,b):
    c = a+b
    d = a-b
    e = a*b
    #return c          #Return terminates the function,
    #return d           no multiple return's per function.
    #return e
    return c,d,e
print(cal(56,65))'''


#SPLITBILL TASK:
'''while True:
    def splitbill():
        bill = int(input("Enter bill: "))
        people = int(input("How many people are there to split bill?? "))
        splitted = bill/people
        return splitted
    print(splitbill())'''


'''while True:
    def splitbill():
        bill = int(input("Enter bill: "))
        people = int(input("How many people are there to split bill?? "))
        splitted = bill/people
        print(f"bill:{bill} is splitted for {people} members equally results:")
        print("{} rupees per head".format(splitted))
    splitbill()'''


#Calculator using Functions:
while True:
    def calc():
        a = int(input("Enter the 'a' value: "))
        b = int(input("Enter the 'b' value: "))
        print("Enter your option:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
        option = int(input("Your option---> "))
        if option==1:
            print("Addition value: ",a+b)
        if option==2:
            print("Subtraction value: ",a-b)
        if option==3:
            print("Multiplication value: ",a*b)
        if option==4:
            print("Division Value: ",a/b)
        if option!=1 and option!=2 and option!=3 and option!=4:
            print("Invalid Option!!")
    calc()        
    



    
