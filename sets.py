mySet = set ()
myOtherSet = {}

st = {"Orange", "Watermelon", "Banana"}
print(st)
print("Does st contain Banana?", 'Banana' in st)
print(1 in st)
st1 = {1,2,3,4,5}
st1.add(7)
p = print
p(st1)
st1.add(6)
p(st1)
p(type(st1))
st1.add(1)
p(st1)
st1.add(10)
p(st1)
st1.update(['a','b','c','d'])
p(st1)
st1.add("hello world")
p(st1)
p(st1)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
p(type(fruits))
p(type(vegetables))
p(fruits)
p(fruits.remove('mango'))
p(fruits)
p(fruits.pop())
p(fruits)
st.clear()
p(st)
del fruits  
ls = ["a","b","c","d"]
p(type(ls))
set2 = set(ls)
p(set2, type(set2))

st1 = {'a','b','c','c','d'}
st2 = {1,3,2,4,7,6,5}
st3 = st1.union(st2)
p(st3)

st4 = {'a','b','c','c','d'}
st5 = {1,3,2,4,7,6,5}
st4.update(st5)
p(st4)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)
p(st1.intersection(st2))