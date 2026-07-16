#KEYWORD AND POSITIONAL ARGUMENTS
'''def Details(id,name,mailid):
    id = 10
    name = "pooja"
    mailid = "pooja@codegnan.com"
    print(id,name,mailid)                #Step-1
Details()  #Error
Details(id,name,mailid)  #Error
Details(id="id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="p@mail.com")
Details(id="10",name="Yaswanth",mailid="yaswanth@mail.com")   #Step-2
Details(id="11",name="Teja",mailid="teja@mail.com")

Details(40,"Swaroop","s@gmail.com")    #Step-3

Details("harika@gmail.com",50,"harika")   #Step-4

Details(name="Vysali",id="19",mailid="vy12@mail.com")'''   #Step-5



#DEFALUT ARGUMENTS
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''    


'''def Grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''    


'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''    


'''def Grocery(item="Ghee",price):
    #non default arg follows def arg ----> ERROR
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500) '''


#TASK-- cake_name,price,qty
'''def Bakery(c_name,price,qty):
    print("cake is %s cake." %c_name)
    print("price of cake is %.2f Rupees" %price)
    print("Quantity: %d" %qty)
    total = price*qty
    print("Your Total is: %.2f" %total)
Bakery("velvet",500,1)'''


'''def Bakery(c_name="strawberry",price=400,qty=3):
    print("cake is %s cake." %c_name)
    print("price of cake is %.2f Rupees" %price)
    print("Quantity: %d" %qty)
    total = price*qty
    print("Your Total is: %.2f" %total)
Bakery()'''


'''def Bakery(c_name,price,qty=5):
    print("cake is %s cake." %c_name)
    print("price of cake is %.2f Rupees" %price)
    print("Quantity: %d" %qty)
    total = price*qty
    print("Your Total is: %.2f" %total)
Bakery("velvet",500)'''


'''def Bakery(c_name,price=400,qty):     #ERROR
    print("cake is %s cake." %c_name)
    print("price of cake is %.2f Rupees" %price)
    print("Quantity: %d" %qty)
    total = price*qty
    print("Your Total is: %.2f" %total)
Bakery("velvet",1)'''


# * ARGUMENTS(* IS USED TO UNPACK THE ELEMENTS)
'''a = [10,20,30,40,50]
print(a)
print(*a)'''


'''b = (5,6,7,8,9,10)
print(b)
print(*b)'''


'''c = {6,7,8,9,10}
print(c)
print(*c)'''


'''d = {"name":"Teja","year":"2008","month":"10"}
print(d)
print(*d)
print(**d)'''


'''a,b,c = 2,3,5,8,10,12,18,21
print(a)
print(b)
print(c)'''    #ERROR


'''a,*b,c = 2,3,5,8,10,12,18,21
print(a)
print(*b)
print(c)'''


'''a,b,c = 3,4,5
print(a)
print(b)
print(c)'''


'''a,b,*c = 2,3,4,5,6,7,8,9,10,11
print(a)
print(b)
print(*c)'''



'''a = "Yaswanth"
print(a)
print(*a)'''


'''a,b,c = "Yaswanth"
print(a)
print(b)     #ERROR
print(c)'''


'''a,b,c ="cod"
print(a)
print(b)
print(c)'''


a,b,*c="yeswanth"
print(a)
print(b)
print(*c)


















