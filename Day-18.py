#VARIABLE LENGTH ARGUMENT:
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b = [2,3,4,5,6,7]
check(*b)
c = {7,8,9,10,11}
check(*c)
d = {"year":2026,"month":7}
check(*d)'''


'''def check1(*a):
    d = 1 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        d = d+i
        print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5,2.3,4.3)
check1(2,3,4,5,4.2,2.5,"pooja")''' #Error


'''def check1(*a):
    d = 1 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) is int or type(i) is float:   
            d = d+i
            print(d)
    if type(i) is not int,float:
        print("Invalid")
check1(2,3,4,5,4.2,2.5,"pooja")'''  #Error solved


#KWARGS(**)----->KEYWORD ARGUMENTS:
'''def details(**a):
    print(a)
    print(type(a))
details()'''
d = {"names":["harsha","teja","sampath"],"marks":[60,70,80],
     "status":["p","a","p"]}
'''details(**d)'''


'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
details(**d)'''


#BOTH * & ** USAGE:
'''def final(*a,**b):
    d = 2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d = d+i
        print(d)
    for i,j in b.items():
        print("Key is ",i)
        print("Value is ",j)
final()
data=(2,3,4,5,2.3,4.3)
final(*data,**d)'''


#Railway Ticket Discount Task:
while True:
    def Rail_ticket():
        Name = input("Enter your Name: ")
        print("Hello {}".format(Name))
        Ticket_price = 1500
        Destination = input("Enter your Destination city: ")
        print("Actual Ticket Price for your Destination {} is {} Rupees".format(Destination,Ticket_price))
        Gender = input("Enter Gender(Male or Female): ").lower()
        Age = int(input("Enter your age: "))
        if Gender=="male":
            if Age>60:
                Discount = Ticket_price*0.30
                Ticket_price -= Discount
                print("Congrats!! You got 30% Discount on your Ticket.")
                print("Your Grand Total is: {}".format(Ticket_price))
            if Age<60:
                print("Sorry, we've got no discount on this ticket")
                print("Your Grand Total is: {}".format(Ticket_price))
        if Gender=="female":
            if Age>60:
                Discount = Ticket_price*0.50
                Ticket_price -= Discount
                print("Congrats!! You got 50% Discount on your Ticket.")
                print("Your Grand Total is: {}".format(Ticket_price))
            if Age<60:
                Discount = Ticket_price*0.30
                Ticket_price -= Discount
                print("Congrats!! You got 30% Discount on your Ticket.")
                print("Your Grand Total is: {}".format(Ticket_price))
        
    Rail_ticket()            
    
    














    





