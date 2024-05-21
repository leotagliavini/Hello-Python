
'''age = int(input("Enter your age: "))

if age > 18:
    print("You are old enough to drive")
else:
    print("You need "+ str(18-age) +" more years to learn to drive.")
'''

'''age = int(input("Enter your age: "))
myAge = 26
if age > myAge:
    print("You are older than me for " + str(age-myAge) + " years" )
    if age-myAge <= 5:
        print("But it's not for much")
    elif age-myAge >5 and age-myAge <= 10:
        print("Ok you are really greater than me")
    else:
        print("You are really older than me")
elif age < myAge:
    print("You are younger than me for " + str(myAge-age) + " years")
else:
    print("We have the same age")'''

'''numOne = int(input("Enter number one: "))
numTwo = int(input("Enter number two: "))

if numOne > numTwo:
    print(str(numOne) + " is greater than " + str(numTwo) )
elif numOne < numTwo:
    print(str(numOne) + " smaller than " + str(numTwo) )
else:
    print(str(numOne) + " is equal to " + str(numTwo))    
'''
'''s = str(input("What is the month?: "))

if s == "September" or s == "October " or s == "November":
    print("Autumn")
elif s == "December" or s == "January" or s == "February":
    print("Winter")
elif s == "March" or s == "April" or s == "May":
    print("Spring")
elif s == "June" or s == "July" or s == "August":
    print("Summer")
else: 
    print("Incorrect month.")
    '''

#If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
#If the fruit exists print('That fruit already exist in the list')

# fruits = ['banana', 'orange', 'mango', 'lemon']

# nFruit = str(input("Insert a  new fruit: "))

# if fruits.__contains__(nFruit):
#     print("Existe")
# else:
#     print("no existe")
#     fruits.append(nFruit)
# print(fruits)

#IT WORKS!!!! 


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ["Node","Python","MongoDB"],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

'''
* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), 
 if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
'''

# if "skills" in person:
#     xd = person['skills'][2]
#     print(xd)    
#     if "Python" in person['skills']:
#         print("Yes, the dictionary has Python in skills")
    
# if person['skills'] != [""]:
#     if person['skills'] == ["JavaScript", "React"]:
#         print("He is a front end developer")
#     elif person['skills'] == ["Node","Python","MongoDB"]:
#         print("He is a backend developer")
#     elif person["skills"] == ["React","Node","MongoDB"]:
#         print("He is a fullstack developer")
#     else:
#         print("Unknown title")
    
# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

# s = int(input("Insert student's score: "))
# p = print
# if s >= 80 and s <= 100:
#     p="A"
# elif s >= 70 and s <=89:
#     p("B")
# elif s >= 60 and s <=69:
#     p("c")
# elif s >= 50 and s <=59:
#     p("B")
# else:
#     p("F")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

# If the person is married and if he lives in Finland, print the information in the following format:  Asabeneh Yetayeh lives in Finland. He is married.
inn = person['country']
inn = inn[1:3]
hee = person['first_name'][-2:]
he = hee[::-1]


i = 0

if person["is_marred"] == True and person['country'] == "Finland":
    print(person['first_name'] + " " + person['last_name'] + " lives " + inn + " " + person['country'] + " and " + he + " is " + " married")


    

