#EXCEPTION HANDLING:
'''while True:
    try:
        a = float(input("a value: "))
        b = float(input("b value: "))
        c = a//b
        print(c)
    except:
        print("Exception is raised.")
    else:
        print("No Exceptions")
    finally:
        print("Programs Ends.")'''


#Regular Expressions(regex):
'''a = "codegnan is in vja"
print(a)'''

'''a = "codegnan\nis\tin\nvij"
print(a)'''

#rstring:
'''a = r"codegnan\nis\tin\nvja"
print(a)'''


#compile(),search(),findall(),split(),sub()

#sequence characters:
'''\w -> it matches alphanumeric
\W -> it matches non-alphanumeric
\d -> it matches any digit
\D -> it matches non-digit
\s -> it matches white-spaces
\S -> it matches non-white-spaces'''

#compile():
import re
a = "mat map cap cup money cash cat dog mug donkey maths"
'''b = re.compile(r"m\w\w\w\w")
print(b)'''

#Search():
'''c = b.search(a)
print(c)'''

'''c = re.search(r"m\w+",a)
print(c)'''

#findall():
'''d = re.findall(r"m\w+",a)
print(*d)'''

#split():
'''e = re.split(r"m",a)
print(e)

f = re.split(r"\s",a)
print(f)

h = re.split("\S",a)
print(h)'''

#sub():
'''g = re.sub(r"m","a",a)
print(g)'''

#\d:
'''a = "year 2026 month 7 date 30"
b = re.findall(r"\d",a)
print(b)

d = re.findall(r"\d+",a)
print(d)

e = re.findall(r"\D+",a)
print(e)'''
