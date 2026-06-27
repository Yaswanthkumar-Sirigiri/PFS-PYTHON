Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DATATYPE CONVERSIONS
#INT
int(9)
9
eint(8.9)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    eint(8.9)
NameError: name 'eint' is not defined. Did you mean: 'int'?
int("Yaswanth")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("Yaswanth")
ValueError: invalid literal for int() with base 10: 'Yaswanth'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#FLOAT
float(6)
6.0
float(3.4)
3.4
float("python")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float(7+9j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(7+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
#STRING
str(6)
'6'
str(5.6)
'5.6'
>>> str("hi")
'hi'
>>> str(6+9j)
'(6+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #COMPLEX
>>> complex(5+9j)
(5+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #BOOLEAN
>>> bool(5)
True
>>> bool(8.9)
True
>>> bool("java")
True
>>> bool(5+9j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(0.1)
True
