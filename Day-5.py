Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#CONCATENATION
a = "code"
b = "gnan"
print(a+b)
codegnan
a = "python"
b = "course"
print(a+" "+b)
python course
print(a.title()+" "+b.title())
Python Course
#~~~~~EXAMPLE~~~~~~
fname = "Yaswanth"
lname = "kumar"
print(fname+" "+lname)
Yaswanth kumar
print((fname+" "+lname).title())
Yaswanth Kumar
#FORMATTING
a = 2
b = 4
print(a+b)
6
print("The sum is: ",a+b)
The sum is:  6
city = "vijayawada"
print("The city is: ",city)
The city is:  vijayawada
#FORMATTING METHOD()
a = "motu"
b = "pathlu"
print("hello {}{}".format(a,b))
hello motupathlu
print("hello {} {}".format(a,b))
hello motu pathlu
print("hello {} hello {}".format(a,b))
hello motu hello pathlu
#f-STRING
a = "sita"
b = "ram"
print(f"hello {a}{b}")
hello sitaram
print(f"hello {a} {b}")
hello sita ram
print(f"hello {a} hello {b}")
hello sita hello ram
#~~~~~~~~TASK~~~~~~~~~
#MULTIPLICATION PROGRAM USING FORMAT()
a = 5
b = 7
mul = a * b
print("The multiplication of {} and {} is: {}".format(a,b,mul))
The multiplication of 5 and 7 is: 35
#MULTIPLICATION PROGRAM USING f-STRING
print(mul)
35
print(f"The multiplication of {a} and {b} is: {mul}")
The multiplication of 5 and 7 is: 35
#WE CAN ALSO DO..
print("The multiplication of {} and {} is: {}".format(a,b,a*b))
The multiplication of 5 and 7 is: 35
print(f"The multiplication of {a} and {b} is: {a*b}")
The multiplication of 5 and 7 is: 35
#LIST[]
a = [3,5.6,"python",9+7j,True,False]
print(a)
[3, 5.6, 'python', (9+7j), True, False]
type(a)
<class 'list'>
#<--------------LIST METHODS-------------->
#APPEND()
a = ["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
#EXTEND()
a = ["java","html","css"]
a.extend(["js","bs"])
a
['java', 'html', 'css', 'js', 'bs']
#INSERT()
a = ["apple","banana","grapes"]
a.insert(1,"mango")
a
['apple', 'mango', 'banana', 'grapes']
#SORT()
a = ["apple","kiwi","mango","dragon"]
a.sort()
a
['apple', 'dragon', 'kiwi', 'mango']
b = [2,3,1,5,7]
b.sort()
b
[1, 2, 3, 5, 7]
#REVERSE()
a = ["c","java","html","css"]
a.reverse()
a
['css', 'html', 'java', 'c']
b = [1,23,2,45,6,23]
b.reverse()
b
[23, 6, 45, 2, 23, 1]
#POP()
a = ["black","white","purple","megenta"]
a.pop()
'megenta'

a
['black', 'white', 'purple']
a.pop(1)
'white'
a
['black', 'purple']
a.pop("black")
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.pop("black")
TypeError: 'str' object cannot be interpreted as an integer
#REMOVE()
a = ["black","white","purple","megenta"]
a.remove()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
a.remove("white")
a
['black', 'purple', 'megenta']
>>> #COPY()
>>> a = ["pooja","priya","riya","ruth"]
>>> a
['pooja', 'priya', 'riya', 'ruth']
>>> b = a.copy()
>>> b
['pooja', 'priya', 'riya', 'ruth']
>>> #CLEAR()
>>> a = ["pooja","priya","riya","ruth"]
>>> a.clear()
>>> a
[]
>>> a.append("white")
>>> a
['white']
>>> #LEN()
>>> a = ["hi","hello","how"]
>>> a.len()
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a.len()
AttributeError: 'list' object has no attribute 'len'
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> len(a)
3
>>> a.count("hello")
1
>>> #INDEX()
>>> a.index("hello")
1
