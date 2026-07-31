#file handling():
#write()
'''a = open("Yaswanth.txt","w")
a.write("Yaswanth kumar sirigiri")
a.close()'''

'''a = open("Yaswanth.txt","w")
a.write("python")
a.close()'''

#append():
'''a = open("Yaswanth.txt","a")
a.write("\tYaswanth")
a.close()'''

'''a = open("Yaswanth.txt","w")
a.write(input("data"))
a.close()'''

'''a = open("Yaswanth.txt","w")
b = input("data: ")
a.write(b)
a.close()'''

#read():
'''a = open("Yaswanth.txt")'''
'''print(a.read())''' #It will display entire content.
'''print(a.readline())''' #It will display fisrt line.
'''print(a.readlines())''' #It will display with \n.
'''print(a.read(20))''' #It will displays upto specified string leantgh.

#writelines()->it makes every object side-by-side:
'''names = ["You","Are","How","HI","Hello"]
a = open("Yaswanth.txt","w")
a.writelines("\n".join(names))
a.close()'''

#File Reading:
'''a = open("D:\PYTHON\Day-23.py")
print(a.read())'''

