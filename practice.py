'''if 5 > 2:
    print("true")
    print("true")
    print("true")

#This is a comment
''''''This is a multiline

 comment
 
 and all that you write here will be ignore
 as
 x = 5
 '''
''''p = print
t = type
x = 5
p(t(x))
x = "x"
p(t(x))
z = int(4)
p(t(z))
z = str("z")
p(t(z))

z = x = y = 5

p(y)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
  global z
  z = "Hi there"

myfunc()

print("Python is " + x) 
print(z)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print(x)

myfunc()

print("Python is " + x)
a = "Hello world"
p(a[0:4])

#SETS

mySet = set()
ms = {}
p(t(mySet))
p(t(ms))

thisset = {"apple", "banana", "cherry"}
p("apple" in thisset)
for x in thisset:
   p(x)
thisset.add("lemon")
p(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
p(thisset)
thisset.remove("kiwi")
p(thisset)
thisset.discard("kiwi")
p(thisset)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

a  = "Hello world!"
p(a.replace("!","?"))
z = "This is a format string {}"
p(z.format("FUCK U"))

i = "I AM"
y = "You were"
h = "He will"
tenses = "Here are some tenses {} present {} past {} future"
p(tenses.format(i,y,h))
illegalString = "This is an \"illegal\" string "
p(illegalString)
a = "Hola"

myFamily = {
   "child1" : {
      "name": "teo",
      "age": 25
   },
     "child2" : {
      "name": "leo",
      "age": 26
   },
     "child3" : {
      "name": "feo",
      "age": 250
   }
}
p(myFamily["child1"].values())
p(myFamily)


chlid1 = {
   "name":"leo",
   "age": 26
}
chlid2 = {
   "name":"aleo",
   "age": 26
}
chlid3 = {
   "name":"bleo",
   "age": 26
}

myFamily = {
   "child1": chlid1,
   "child2":chlid2,
   "child3": chlid3}

p(t(myFamily))
p(myFamily.get("child1"))
p(myFamily["child1"]["age"])

p(len(myFamily))

p(myFamily["child3"])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

p(person["skills"][1])
p(person["country"],person["age"])
p(person["address"]["zipcode"])
#print(person['city'])  #error
p(person.get("city")) #none because city doesn't exist in the current dictionary 
p(person.get("age"))

#Adding Items to a Dictionary
#We can add new key and value pairs to a dictionary I'M HERE
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct["key5"] = "value5"
p(dct)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person["job"] = "Programmer"
person["pet?"] = True
person["cars"] = ("Toyota","Audi","Tesla")
x = person["cars"]
p(t(x),x)
p(t(person["skills"]))
p(person)

person["skills"].append("HTML")

p(person)

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct["key2"] = "value222"
p(dct)
dct["key2"] = "keyXXX"  
p(dct)
p("key1" in dct)#true
p("key6" in dct)#false

dct.pop("key2")
p(dct)
p(dct.popitem())

del dct["key3"]
p(dct)

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
p(dct.items())
p(dct.clear())
p(dct)
del dct
# p(dct) Error because dct doesn't exist 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct1 = dct.copy()
p(dct1)
p(dct.keys())
p(dct.values())


''''''dog = {}
p(t(dog))
dog["color"]
dog = {"color","breed","legs","age"}
p(t(dog))
'''
'''
dekstop = {
         'PC' : "Personal computer",
         'Keyboard': "Redragon",
         'Mouse': "Logitech",
         "Monitor": "Samsung"
         }

p(dekstop.values())
p(dekstop["Mouse"])
p(len(dekstop))
p(len(dekstop.values()))
p(len(dekstop.items()))


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
p(t(thisdict["electric"]))
p(t(thisdict["colors"]))
p(thisdict)
thisdict["topSpeed"] = 205
p(thisdict)
p(thisdict.values())
x = thisdict.values()
p(t(x))

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x, " after") #after the change

thisdict["year"] = "1970"
p(thisdict)
thisdict.update({"year" : 2024})

p(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

p(thisdict)

thisdict.pop("year")
p(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.popitem()
p(thisdict)

del thisdict["brand"]
p(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict #This delete the dict  completly 
#p(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "eletric": True
}

for x in thisdict:
   p(x)
for x in thisdict.values():
   p(x)
for x in thisdict.items():
   p(x)

#COPY DICTIONARIES

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

myOtherDict = thisdict.copy()
p(myOtherDict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
p(myfamily["child1"]["name"])
p(myfamily["child2"].values())
p(myfamily["child3"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

a = 223
b = 34
if a > b: print("a is greater than b") 

a = 330
b = 330
print("A") if a > b else print("B") 

p("A ",a) if a>b else p("B ",b) if b>a else p("=")


a = 34
b = -12

if a>b and b >= 0 : p("a is greater than b") 
p("a is greater than b") if a > b and b >=0 else p("b isn't greater than 0", b) 

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a = 33
b = 200

if b > a:
  pass
x = 0
while x < 10:
  p("xd ", x)
  if x == 4:
    break
  x+=1 

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

x = 0 
while x <10:
  p(x)
  x+=1
else:
  print("There are not more numbers to print ", 10)  '''
p = print
t = type
l = len

for x in "String":
  p(x.upper())

fruits = ["apple", "banana", "cherry"]

for i in fruits:
  p(i.capitalize(), l(i), t(i))

fuck = ["Orange", "Banana", "Strewberry"]
p(t(fuck))
for x in fuck[1]:
  p(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  p(x)
  if x == "banana":
    break
p("----------")
for x in fruits:
  
  if x == "banana":
    continue
  p(x)

  for x in range(1,11,2):
    p(x)
  else:
    p("it's all, what do u need ?")


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  for j in adj:
    p(x,j)
p("---------")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass

for i in ["a","b","c",1,4,56,True]:
  p(i)

for x in "banana":
  if x == "n":
    break
  p(x)

for x in range(50,100,10):
  p(x)

for x in range(0,10,1):
  p(x)
else:
  p(10)

def myFunction(name):
  p("Hello world, this is my first function in Python and I'm", name)

myFunction("Leo")

def sum(a,b):
  return a + b

p(sum(2,4))

def my_function(*kids):
  print("The youngest child is " + kids[4])

my_function("Emil", "Tobias", "Linus","Leo1", "leo2", "leo3")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def mfunc(a,b,c):
  p(c, " it's the best")

mfunc(c = "CCC", a = "AAA", b = "BBB")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def mkFunc(**var):
  p("I can't understand this shit ", var["loc"])

mkFunc(lac = "What is this shit", lec = "Really man, i can't understand it, i have to learn from other pages, fuck", luc = "Luc?", loc = "Loc? really? Im done dude")

def ope(**x):
  return x["mult"]

p(ope(sum = 2+2, rest = 4-2, div = 4/2, mult = 2*4))

def myNameIs(fname = "Leo"):
  p("Hello my name is ", fname)

myNameIs("Juan")
myNameIs()

#Passing a List as an Argument

def func(food):
  for x in food:
    p(x)  

fruits = ["Orange","Lemon","Watermelon"]
num = {2,5,6,74,51,2323,55}
numt = ("2",2,"aa",True,1.2)
func(num)
p(t(num))
func(numt)
p(t(numt))

def aFun(x,y):
  for i in range(x,y):
    p(i)

aFun(0,10)

def RFun(x,y):
  return (x+y)

p(RFun(2,5)) 

def passFunc():
  pass

passFunc()

def posicionalArgument(x,/):
  p(x*10)

posicionalArgument(2)
#posicionalArgument(x=2) This will throw an error because with ,/ we can't specifed the position of the aurgument

def posicionalArgument1(x,y,/):
  p(x*10+y)

posicionalArgument1(10,2)
#posicionalArgument1(x=10,y=2) It doesn't care wheter or not the posicion of the argument is correct 

def onlyKeyAurguments(*,x):
  p(x)

onlyKeyAurguments(x = 3)

def onlyKeyAurguments1(*,x,y,z):
  p("x ",x," y ",y," z ",z)

onlyKeyAurguments1(x = 3, z = 5, y= 4)
#onlyKeyAurguments1(3,4,5) #Error because it's only accept key aurments

def combineOKAandPA(a,b,/,c,d,*,e):
  p(a,b,c,d,e)

combineOKAandPA(1, 2,c = 3, d = 4,e = 5)
combineOKAandPA(1, 2,3, d = 4,e = 5)
combineOKAandPA(1, 2,3,4,e = 5)


def tri_recursion(k):
  if(k > 0):
    result =  k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

'''def tri_recursion(k):
  if(k > 0):
    result = k=-1
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)'''


#ITERATIVE 
'''def walk(steps):
  for setp in range(1,steps+1):
    p(f"You take step #{steps}")
'''

#RECURSIVE
'''
def walk(steps):
  if steps > 0:
    walk(steps-1)
    p(f"You take step #{steps}")
  

walk(100)
'''

libros = [120,20,40,200,60]
total = 0
for i in libros:
  total+=i
p(total)

def factorial(x):
  if x == 1:
    return 1
  
  return x * factorial(x-1)

print(factorial(5))

def sumRecur(x):
  if x == 1:
    return 1
  
  return x + sumRecur(x-1)

print(sumRecur(5))

def mostrarList(lista,index):
  if index != len(lista):
    p(lista[index])
    mostrarList(lista, index + 1)

lista = ["a","b","c","d"]

mostrarList(lista,0)

def func(*t):
  p("HELLO", t[1])

func("a","b","c","d")

def my_function(*kids):
  #print("The youngest child is " + kids[2])
  return kids[1]
p(my_function(4,5,6))

def func(a1,a2,a3):
  p("You are awesome! ", a2)

func(a3 = "A3", a1 = "A1", a2 = "A2")

func("A3","A1","A2")
#func("a2") error, this func required 3 aurmements but only recive one 

def func(**t):
  p("Hello ! ", t["a1"])

func(a1 = "XA1", b1 = "XB1", c1 = "XC1", d1 = "XD1")

def func(var = "XA1"):
  p("You are ", var )

func("XA2")
func()
func("XA32")

def func(list):
  for x in list:
    p(x)

l = [1,2,3,4,5]
func(l)

def func(x = True):
  return x

p(func(False))
p(func(True))
p(func(False))
p(func())


def func(x):
  return x*x*x*x*x

p(func(5))

def func(x):
  return "hi there " ,x 

p(func(5))

def func():
  pass
#later I will complete this function, remeber me on January 31


def my_function(x, /):
  print(x)

my_function(3)

def my_function(x,y,z,/,a,b):
  print(x,y,z,a,b)

my_function(1,2,3,a=4,b=5)

def myFunc(*,x,y,z):
  p(x,y,z)

myFunc(z=1,x=2,y=3)


def myCombineFunction(x,y,/,*,z,a="xd"):
  p(x,y,z,a)

myCombineFunction(1,2,z=3)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

x = lambda a : a + 10 
p(x(5))

z = lambda x,b : x*b 
p(z(2,4))
za = lambda a,b,c : a+b+c
p(za(2,4,8))

z = lambda a,b,c : (a*b+c)+(a/b)
p(z(2,4,6))




def myfunc(n):
  return lambda a : a * n
p(myfunc(2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
p(t(mydoubler(2)))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

Data = lambda fname,lname,age,country = "Argentina": fname + " " + lname + " " + str(age) + " " + country 
p(Data("Leo", "Tag",26,"Argentia"))
AGE = lambda a : True if a > 18 else False
p(AGE(2))
