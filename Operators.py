Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#ARITHMATIC
a = 2
b = 4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a/b)
0.5
print(a//b)
0
print(a**b)
16
print(a&b)
0
#ASSIGNMENT
a = 10
b = 25
b += a
b
35
b -= 34
b
1
b *= 67
b
67
b /= 4
b
16.75
print(a+=b)
SyntaxError: invalid syntax
b //= a
b
1.0
b **= 3
b
1.0
b &= 2
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b &= 2
TypeError: unsupported operand type(s) for &=: 'float' and 'int'
a %= 4
b
1.0
a
2
b %= 4
b
1.0
#COMPARISION
a  = 20
b = 45
a < b
True
a > b
False
b < a
False
b > a
True
a != b
True
a == b
False
del b
b = 20
a == b
True
a <= b
True
a >= b
True
b <= b
True
b <= a
True
b >= a
True
del a,b
#LOGICAL
a = 5
b = 7
a < b and b > a
True
a <= b and b >=a
True
a != b and a==b
False
a<b and b>a
True
a<b or b>a
True
a>=b or a<=b
True
a!=b or a==b
True
not True
False
not False
True
#IDENNTIFY
a = 50
type(a) is int
True
type(a) is float
False
b = 50.01
type(b) is float
True
type(b) is int
False
c = 'Yaswanth'
type(c) is int
False
type(c) is float
False
type(c) is str
True
d = True
type(d) is int
False
type(d) is float
False
type(d) is str
False
type(d) is complex
False
type(d) is bool
True
e = 5+6j
type(e) is int
False
type(e) is float
False
type(e) is str
False
type(e) is bool
False
type(e) is complex
True
#MEMBERSHIP
a = 1,2,3,4,5,6,7,8,9
8 in a
True
20 in a
False
20 not in a
True
#BINARY
a = 5
b = 7
a & b
5
bin(1)
'0b1'
bin(2)
'0b10'
bin(3)
'0b11'
bin(4)
'0b100'
bin(5)
'0b101'
bin(6)
'0b110'
bin(7)
'0b111'
bin(8)
'0b1000'
bin(9)
'0b1001'
b & a
5
c = 7
a & c
5
b & c
7
#BINARY AND>>>
#<<<BINARY OR
a = 5
b = 9
a | b
13
c = 2
d = 5
c | d
7
#BINARY NOT
a = 2
--(a+1)
3
-(a+1) #NOT follows this formula by default
-3
>>> ~a
-3
>>> a = 30
>>> ~a
-31
>>> a = -24
>>> ~a
23
>>> b = -23
>>> ~b
22
>>> #BINARY XOR (TWO SAME-->0, TWO OPPOSITES-->1)
>>> a = 6
>>> b = 9
>>> a^b
15
>>> a = 5
>>> b = 2
>>> a^b
7
>>> #BINARY LEFT SHIFT (ADDING NO. OF ZEROES IN THE RIGHT SIDE OF BINARY NUMBER)
>>> a = 5
>>> a << 2 #adding 2 zeroes on the right side of 5 binary code
20
>>> a << 5
160
>>> #BINARY RIGHT SHIFT (ADDING NO. OF ZEROES IN THE LEFT SIDE OF BINARY NUMBER)
>>> a = 5
>>> a >> 2 #adding 2 zeroes on the left side of 5 binary code
1
>>> a >> 5 #we get maximum 0's & 1's in the right shift
0
