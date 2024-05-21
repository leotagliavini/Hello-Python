'''empty_tuple = ()
#is like a list, but it has fewer options 
empty_tuple = (1,2,3, "helo", "leo",3.4)
print(empty_tuple)
print(len(empty_tuple))
print(empty_tuple[-3])
lstElem = len(empty_tuple) - 1
print(empty_tuple[lstElem])
print(empty_tuple[1:2])
print(empty_tuple[-3:-1])
print(type(empty_tuple))
lst = list(empty_tuple)
print(type(lst))
result = "helo" in empty_tuple
print(result)

tpl1 = (1,2,3,4)
tpl2 = (5,6,7,8)
tpls = tpl1 + tpl2
print(tpls)'''

#exercise 

tpl = ()
tpl = tuple()
brothers = ('Facundo', 'Mayco','Alexis')
sisters = ('Jesica', 'Ana', 'Marta')
siblings = brothers + sisters
print(len(siblings))
parents = ('Jose', 'viviana')
familyMembers = siblings + parents
print(familyMembers)
tpl1 = familyMembers[:6]
print(tpl1)
tpl2 = familyMembers[6:]
print(tpl2)
fruits = ("Orange","Apple")
vegetables = ("Carrot", "Potato", "Tomato")
animalProd = ("Eggs", "Milk")
food_stuff_tp = fruits + vegetables + animalProd
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(food_stuff_lt[3:5])
print(food_stuff_lt[0:3], food_stuff_lt[-3:])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

