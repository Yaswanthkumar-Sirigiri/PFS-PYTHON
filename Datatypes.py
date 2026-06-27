Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DATATYPES
a = 10
type(a)
<class 'int'>
>>> b = 5.6
>>> type(b)
<class 'float'>
>>> c = 'code'
>>> type(c)
<class 'str'>
>>> c = "Yaswanth"
>>> type(c)
<class 'str'>
>>> c = '''Sirigiri'''
>>> type(c)
<class 'str'>
>>> d = 5+6j
>>> type(d)
<class 'complex'>
>>> d = 5+6i
SyntaxError: invalid decimal literal
>>> d = 5j+6
>>> type(d)
<class 'complex'>
>>> a = True
>>> type(a)
<class 'bool'>
>>> b = False
>>> type(b)
<class 'bool'>
>>> a = true
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a = 'true'
>>> type(a)
<class 'str'>
