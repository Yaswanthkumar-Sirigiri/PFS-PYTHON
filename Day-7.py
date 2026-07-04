Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DICTIONARY
a = {"name":"pooja","year":"2026","month":06}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a = {"name":"pooja","year":"2026","month":6}
print(a)
{'name': 'pooja', 'year': '2026', 'month': 6}
type(a)
<class 'dict'>
a = {2027:7}
print(type(a))
<class 'dict'>
print(a)
{2027: 7}
#~~~~~~~~~~~~~DICT METHODS~~~~~~~~~~~~~~~`
#UPDATE()
a = {"year":2026,"month":"july"}
a.update({"time":7})
a
{'year': 2026, 'month': 'july', 'time': 7}
a.update({"name":"yaswanth"},{"city":"vij"})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.update({"name":"yaswanth"},{"city":"vij"})
TypeError: update expected at most 1 argument, got 2
a.update({"name":"yaswanth","city":"vij"})
a
{'year': 2026, 'month': 'july', 'time': 7, 'name': 'yaswanth', 'city': 'vij'}
#SET DEFAULT()
a = {"course":"python"}
a.setdefault("duration",4)
4
a
{'course': 'python', 'duration': 4}
#ACCESSING
a = {"color":"black","food":"biryani"}
a["color"]
['color']
#GET()
a.get("food")
'biryani'
a.get("biryani")
#KEYS()
a.keys()
dict_keys(['color', 'food'])
#VALUES()
a.values()
dict_values(['black', 'biryani'])
#ITEMS()
a.items()
dict_items([('color', 'black'), ('food', 'biryani')])
#POP()
a = {"city":"vja","country":"india","state":"ap"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("city")
'vja'
a
{'country': 'india', 'state': 'ap'}
#POPITEM()
a.popitem()
('state', 'ap')
#LEN()
a = {"name":"yaswanth","mail":"yaswanth@gmail.com"}
len(a)
2
#COPY()
b = a.copy()
b
{'name': 'yaswanth', 'mail': 'yaswanth@gmail.com'}
#CLEAR()
a.clear()
a
{}
#NO DUPLICATES
>>> a = {"name":"yaswanth","year":"2026","name":"yaswanth"}
>>> print(a)
{'name': 'yaswanth', 'year': '2026'}
>>> b = {"name":"yaswanth","year":"2026","name":"sirigiri"}
>>> b
{'name': 'sirigiri', 'year': '2026'}
>>> c = {"name1":"yaswanth","year":2026,"name2":"sirigiri"}
>>> a
{'name': 'yaswanth', 'year': '2026'}
>>> c
{'name1': 'yaswanth', 'year': 2026, 'name2': 'sirigiri'}
>>> #1 KEY -----> NO. OF VALUES WE CAN PASS
>>> a = {"idnos":[10,20,30],"names":["raju","gopi","sita"],"marks":[60,70,80]}
>>> a.key()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['raju', 'gopi', 'sita'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['raju', 'gopi', 'sita']), ('marks', [60, 70, 80])])
>>> #~~~~~~~~~~~~~~~~~~~TASK~~~~~~~~~~~~~~~~~~~~~~
>>> #input a = ["codegnan","python","course"]
... 
>>> #output ['CODEGNAN','PYTHON','COURSE']
>>> a = ["codegnan","python","course"]
>>> b = str(a)
>>> b.upper()
"['CODEGNAN', 'PYTHON', 'COURSE']"
