Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#TUPLE()
a = (4,5.6,"pooja",8+9j,True,False)
print(a)
(4, 5.6, 'pooja', (8+9j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.index(8+9j)
3
a.count(True)
1
#SETS{}
a = {3,6.7,"python",8+9j,True,False}
print(a)
{False, True, 'python', 3, (8+9j), 6.7}
type(a)
<class 'set'>
b = {6,9,3,5,6,10,9,20,5}
print(b)
{3, 20, 5, 6, 9, 10}
#~~No duplicates are allowed
a = {2,3,4,5,6,7,8,9}
b = {6,7,8,9}
b.issubset(a)
True
a.issubset(b)
False
#~~~~ISSUBSET()~~~~>>>
#<<<~~~~ISSUPERSET()~~~~~
a = {4,5,6,7,8,9}
b = {6,7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False
#UNION()
a = {1,2,3,4,5,6}
b = {5,6,7,8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#INTERSECTION()
a = {3,4,5,6,7,8,9}
b = {7,8,9,10,11,12}
a.intersection(b)
{8, 9, 7}
#DIFFERRENCE()
a = {10,11,12,13,14,15}
b = {6,7,8,12,13,14,15,16,17}
a.difference(a)
set()
a.difference(b)
{10, 11}
b.difference(a)
{6, 7, 8, 16, 17}
#SYMMETRIC_DIFFERENCE()
a = {2,3,4,5,6,7,8,9}
b = {5,6,7,8,9,10,11}
a.symmetric_difference(b)
{2, 3, 4, 10, 11}
#UPDATE()
a = {1,2,3,4,5,6}
b = {2,3,4,5,6,7}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7}
a
{1, 2, 3, 4, 5, 6, 7}
b
{2, 3, 4, 5, 6, 7}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7}
#INTERSECTION_UPDATE()
a = {1,3,5,7,8,9,10}
b = {2,4,6,7,10,11,12}
a
{1, 3, 5, 7, 8, 9, 10}
a.intersection_update(b)
a
{10, 7}
b.intersection_update(a)
b
{10, 7}
#difference_update()
a = {2,3,4,5,6,7,8}
b = {1,5,6,7,8,9,10}
a.difference_update(b)
a
{2, 3, 4}
b.difference_update(a)
b
{1, 5, 6, 7, 8, 9, 10}
#SYMMETRIC_DIFFERENCE_UPDATE()
a = {2,3,4,5,6,7,8,9}
b = {5,6,7,8,9,10,11}
a.symmetric_difference_update(b)
a
{2, 3, 4, 10, 11}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}
#ADD()
a = {1,2,3,4,5}
a.add(34)
a
{1, 2, 3, 4, 5, 34}
c = set()
c.add(39)
c
{39}
#COPY()
a = {1,2,3,4}
b = copy(a)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    b = copy(a)
NameError: name 'copy' is not defined. Did you forget to import 'copy'?
b.copy(a)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    b.copy(a)
TypeError: set.copy() takes no arguments (1 given)
b = a.copy()
b
{1, 2, 3, 4}
#POP()
a = {5,6,7,8,9}
a.pop()
5
a
{6, 7, 8, 9}
a.pop()
6
#REMOVE()
a = {5,6,7,8,9}
a.remove(7)
a
{5, 6, 8, 9}
a.remove(9)
a
{5, 6, 8}
#ISDISJOINT()
a = {1,2,3,4,5}
b = {2,3,4,5,6}
c = {7,8,9,10,11}
a.isdisjoint(b)
False
b.isdisjoint(c)
True
#LEN()
a = {4,5,6,7,8}
len(a)
5
#EXCLUDED!!!!
a.count()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
a.index()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a.index()
AttributeError: 'set' object has no attribute 'index'
#~~~~~~~~~~~~~~~TASK~~~~~~~~~~~~~
a = [9,1,5,2,8,4,6,3,7,0]
b = a[:6]
b
[9, 1, 5, 2, 8, 4]
c = a[6:]
>>> c
[6, 3, 7, 0]
>>> b.sort()
>>> b
[1, 2, 4, 5, 8, 9]
>>> c.sort()
>>> c
[0, 3, 6, 7]
>>> b.reverse()
>>> b
[9, 8, 5, 4, 2, 1]
>>> del b
>>> del c
>>> b = [:5]
SyntaxError: invalid syntax
>>> b = a[:5]
>>> b
[9, 1, 5, 2, 8]
>>> c = a[5:]
>>> c
[4, 6, 3, 7, 0]
>>> b.reverse()
>>> b
[8, 2, 5, 1, 9]
>>> b.sort()
>>> b
[1, 2, 5, 8, 9]
>>> b.reverse()
>>> b
[9, 8, 5, 2, 1]
>>> c.sort()
>>> c.reverse()
>>> c
[7, 6, 4, 3, 0]
>>> print(c+b)
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
