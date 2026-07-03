Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#NEGATIVE STRIDING()
a = "python course"
a[-1:-11:-3]
'eu h'
a[-2:-12:-4]
'sch'
a[-5:-13:-5]
'oh'
#RULES TO FOLLOW WHILE STRIDING:
a[8:2:3]
''
a[-6:-2:-3]
''
a[::-1]
'esruoc nohtyp'
#~~~~~~~~~~~~~STRING METHODS~~~~~~~~~~~~~~~~~
#len()
a = "python"
len(a)
6
a = "python course"
len(a)
13
a = ""
len(a)
0
a = " "
len(a)
1
#COUNT()
a = "twinkle twinkle little star"
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
a.count("")
28
a.count(" ")
3
b = "twinkletwinkle"
b.count("twinkle")
2
b.count("twinkletwinkle")
1
#FIND()
a = "python"
a.find(t)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.find(t)
NameError: name 't' is not defined
a.find("t")
2
a.find("p")
0
a.find("o")
4
a.find("z")
-1
#ESCAPE SEQUENCES
# \n-->new line & \t-->tab space
a = "Name:\nMobileNo:\tMailId:\nCollege:\tBranch:"
a
'Name:\nMobileNo:\tMailId:\nCollege:\tBranch:'
print(a)
Name:
MobileNo:	MailId:
College:	Branch:
b = "Name: Yaswanth\nMobileNo: 1234567890\tMailId: yaswanth@gmail.com\nCollege: NRI\tBranch: CSE"
print(b)
Name: Yaswanth
MobileNo: 1234567890	MailId: yaswanth@gmail.com
College: NRI	Branch: CSE
#REPLACE()
a = "wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b = "i love java"
b.replace("java","python")
'i love python'
#UPPER()
a = "yaswanth kumar"
a.upper()
'YASWANTH KUMAR'
#LOWER()
a = "YASWANTH KUMAR"
a.lower()
'yaswanth kumar'
#CAPITALISE()
a = "eagle bear"
a.capitalise()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.capitalise()
AttributeError: 'str' object has no attribute 'capitalise'. Did you mean: 'capitalize'?
a.capitalize()
'Eagle bear'
b = "yaswanth kumar"
b.capitalize()
'Yaswanth kumar'
#TITLE()
a = "eagle bear"
a.title()
'Eagle Bear'
b = "yaswanth kumar"
b.title()
'Yaswanth Kumar'
#ISUPPER()
a = "python"
a.isupper()
False
b = "PYTHON"
b.isupper()
True
#ISLOWER()
a = "python"
a.islower()
True
b = "PYTHON"
b.islower()
False
#ISALPHA()
a = "Yaswanth"
a.isalpha()
True
b = "1234"
b.isalpha()
False
#ISDIGIT()
a = "Yaswanth"
a.isdigit()
False
b = "12345"
b.isdigit()
True
#ISALNUM()
a = "yaswanth05"
a.isalnum()
True
b = "yaswanth"
b.isalnum()
True
c = "12345"
c.isalnum()
True
#STARTSWITH()
a = "python"
a.startswith("p")
True
a.startswith("o")
False
>>> #ENDSWITH()
>>> a = "python"
>>> a.endswith("n")
True
>>> a.endswith("j")
False
>>> #STRIP()
>>> a = "     python        "
>>> a.strip()
'python'
>>> #LSTRIP()
>>> a.lstrip()
'python        '
>>> #RSTRIP()
>>> a.rstrip()
'     python'
>>> #SPLIT()
>>> a = "python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> #JOIN()
>>> a = "python","java","c","c++"
>>> ""join()
SyntaxError: invalid syntax
>>> "".join()
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    "".join()
TypeError: str.join() takes exactly one argument (0 given)
>>> "".join(a)
'pythonjavacc++'
>>> " ".join(a)
'python java c c++'
>>> "s".join(a)
'pythonsjavascsc++'
