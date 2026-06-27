Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print(3+8)

a = 10
print(a)

b = 20
print(b)

x = 40
print(x)

z = 50
print(z)

a3 = 80
print(a3)

#6a = 90  //error

#print(@) //error

_ = 100
print(_)


SyntaxError: multiple statements found while compiling a single statement
if = 20
SyntaxError: invalid syntax
a = 4; b = 9
print(a+b)
13
a,b=3,4
print(a,b)
3 4
a = 2,3,4
print(a)
(2, 3, 4)
a,b,c = 10
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a,b,c = 10
TypeError: cannot unpack non-iterable int object
a = b = c = 10
print(a,b,c)
10 10 10
a,b,c = (2,3,4)
print(a,b,c)
2 3 4
#Packing & unpacking
first name = "Yaswanth"
SyntaxError: invalid syntax
first_name = "Yaswanth"
print(first_name)
Yaswanth
a,b,c = 1,2,3,4,5,6,7
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a,b,c = 1,2,3,4,5,6,7
ValueError: too many values to unpack (expected 3)
fname = "Yaswanth"
lname = "Kumar"
print(fname," ",lname)
Yaswanth   Kumar
>>> print(fname,lname)
Yaswanth Kumar
>>> print(fname+""+lname)
YaswanthKumar
>>> print(fname+" "+lname)
Yaswanth Kumar
>>> name = "Yaswanth"
>>> print(name)
Yaswanth
>>> NAME = "Yaswanth"
>>> print(NAME)
Yaswanth
>>> print("name")
name
>>> city = "vja"
>>> print(city)
vja
>>> #DELETE KEYWORD
>>> a = 5
>>> print(a)
5
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> #CASE SENSITIVE
>>> name = "Yaswanth"
>>> print(name)
Yaswanth
>>> NAME = "Yaswanth"
>>> print(NAME)
Yaswanth
