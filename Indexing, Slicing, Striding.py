Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#POSITIVE INDEXING
a = "simple is better than complex"
a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
'imple '
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
a[22]+a[23]+a[24]+a[25]+a[26]
'compl'
a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
b = "Yaswanth kumar Sirigiri is a Trainee"
c = "Python FullStack"
c[-5]+c[-4]+c[-3]+c[-2]+c[-1]
'Stack'
c[-9]+c[-8]+c[-7]+c[-6]
'Full'
c[-16]+c[-15]+c[-14]+c[-13]+c[-12]+c[-11]
'Python'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'Trainee'
b[-36]+b[-35]+b[-34]+b[-33]+b[-32]+b[-31]+b[-30]+b[-29]
'Yaswanth'
#NEGATIVE INDEXING>>>
#SLICING---->(Positive & Negative)
#POSITIVE SLICING
del a,b,c
a = "Time is very precious"
a[9:13]
'ery '
a[8:13]
'very '
a[0:4]
'Time'
a[14:22]
'recious'
a[13:22]
'precious'
a[:4]
'Time'
a[13:]
'precious'
b = "Work until you succeed"
b[15:]
'succeed'
b[5:10]
'until'
b[:4]
'Work'
b[11:14]
'you'
#NEGATIVE SLICING
>>> del a,b
>>> a = "Vizag is city of Destiny"
>>> a[-12:-16]
''
>>> a[-15:-11]
'city'
>>> a[-7:]
'Destiny'
>>> a[:-19]
'Vizag'
>>> b = "Hi Hello How are you"
>>> b[-17:-12]
'Hello'
>>> b[-11:-8]
'How'
>>> b[-7:-4]
'are'
>>> b[-3:]
'you'
>>> b[:-18]
'Hi'
>>> #STRIDING
>>> #----->(Positive & Negative)
>>> #variable_name(starting,ending,increment)
>>> del a,b
>>> a = "Data Science"
>>> a[::]
'Data Science'
>>> a[::1]
'Data Science'
>>> a[::2]
'Dt cec'
>>> a[1:5:1]
'ata '
>>> #POSITIVE STRIDING>>>
>>> #NEGATIVE STRIDING:
