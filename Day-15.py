#LIST COMPREHENSION
#a = ["codegnan","python","course"]
#print(a.upper())


'''b = str(a)
print(b.upper())'''


'''for i in a:
    print(i.upper(),end=" ")'''


'''b = []
for i in a:
    b.append(i.upper())
print(b)'''


#syntax
#a = [expr for var in collection/range]
'''a = [i.upper() for i in a]
print(a)'''


'''a = ["vja","hyd","vzg"]
b = [i.title() for i in a]
print(a)'''


'''a = [1,2,3,5,6,8,12,13]
b = [i*i for i in a]        #Method-1
b = [i**2 for i in a]       #Method-2
b = [pow(i,2) for i in a]   #Method-3
print(b)'''


#if-usage in list comprehension
'''a = [i for i in range(16) if i%2==0]
print(a)'''


'''a = [i for i in range(21) if i>0]
print(a)'''


'''fruits = ["apple","banana","grapes","kiwi","mango","dragon","berry"]
b = [i for i in fruits if "a" in i]
print(b)'''


'''a = [i*i for i in range(21) if i%2==0]
print(a)
a = [i*5 for i in range(21) if i%2!=0]      #Using two if statements
print(a)'''


'''a = [i*i if i%2==0 else i*5 for i in range(21) ]   #using if-else statements.
print(a)'''


'''a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = [a[i]+b[i] for i in range(5)]         #Without len()
c = [a[i]+b[i] for i in range(len(a))]    #With len()
print(c)'''


#~~~~~~~~~~~~~~~MINI-PROJECT~~~~~~~~~~~~~~~~
print("~~~~~~~~~~Account Registration~~~~~~~~~~")
card = input("Enter Card Name: ")
account_bal = int(input("Enter Amount(in Rupees), want to Deposit: "))
password = input("Enter the password: ")
print("~~~~~~~~~~Account Verification~~~~~~~~~~")
card_ver = input("Insert the card---> ")
pass_ver = input("Enter your Password: ")
if card_ver==card and pass_ver==password:
    print(f"Welcome {card.title()}!!!")
    print("Do you want to check: ")
    print("1. Balance Enquiry")
    print("2. withdraw")
    options = int(input("Enter your option(1 or 2): "))
    if options==1:
        print(f"Your Current Account Balance: {account_bal}")
    if options==2:
        withdraw = int(input("Enter Amount to Withdraw: "))
        if withdraw>account_bal:
            print("Insufficient Funds in the Account.")
        else:
            print(f"{withdraw}/- Rupees has been debited from your account.")
            account_bal-=withdraw
            print(f"Your Updated balance: {account_bal}/-")
    if options!=1 and options!=2:
        print("Invalid Option.")
else:
    print("Invalid Card Details, Please Review Card Details.")        
    
    
