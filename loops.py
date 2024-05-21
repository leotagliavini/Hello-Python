# x = 0
# while x < 10:
#     print(x)
#     x+=1
#     if x == 8:
#         break
# else:
#     print(x)
 



# count = 0
# while count < 5:
#     if count == 3:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1


# lst = ["a","b","c","d","e"]
# for x in lst:
#     print(x)

# for i in "String":
#     print("letter: " + i)
# for i in range(len("String")):
#     print(i)

# tpl = (0,1,2,3,4,5)
# print(type(tpl))
# for t in tpl:
#     print(t+0.01)

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }

# for x in person.keys():
#     print(x)
#     if x == "country":
#         print("The country is : " +  person['country'])
#     if x == "skills":
#         print("favorite: "+person['skills'][-1])

# for y in person.values():
#     print(y)

# for key, value in person.items():
#     print(key, value)

# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)
#     print(type(company))
# print(type(it_companies))

# lst = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# for i in lst:
#     if i == "Apple":
#         print("XD")
#         break   
#     print(i)

# for i in lst:
#     if i == "IBM":
#         continue
#     print(i)

# numbers = (0,1,2,3,4,5)
# for i in numbers:
#     if i == 2:
#         continue
#     print(i)

# # numbers = (0,1,2,3,4,5)
# # for number in numbers:
# #     print(number)
# #     if number == 3:
# #         continue
# #     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# # print('outside the loop')


# # for x in range(0,100,5):
# #     print(x)
# #     if x == 50:
# #         for y in range(60,100,10):
# #             print(y)
# #         break

# # lst = list(range(0,11))
# # tpl = tuple(range(0,100,10))
# # st = set(range(100,105,1))
# # for x in st:
# #     print(x)

# # person = {
# #     'first_name': 'Asabeneh',
# #     'last_name': 'Yetayeh',
# #     'age': 250,
# #     'country': 'Finland',
# #     'is_marred': True,
# #     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
# #     'address': {
# #         'street': 'Space street',
# #         'zipcode': '02210'
# #     }
# # }

# # for x in person.keys():
# #     print(x)
# #     if x == "skills":
# #         for y in person['skills']:
# #             print(y)

# # for i in range (11):
# #     print(i)
# # else:
# #     print("The loop ends at number ", i)

# # for x in range(10000000):
# #     pass

# #EXERCISES 

# for x in range(11):
#     print(x)
# print("------------")

# i = 0
# while i <= 10 in range(11):
#     print(i)
#     i+=1
# print("------------")

# for y in range (10,0,-1):
#     print(y)
# print("------------")

# z = 10
# while z >= 0:
#     print(z)
#     z-=1
# print("The end")
# x = "#"

# while len(x) <= 7:
#     print(x)
#     x+="#"

# # Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # cha = "# # # # # # # #"
# # for x in range(8):
# #     for y in range(8):
# #         print(cha)
# rows = 8
# columns = 8
# for i in range(rows):
#     for j in range(columns):
#         print("#", end=" ")
#     print()

# resultado = 0
# num1 = 0
# num2 = 0

# while num1 <= 10:
#     print(str(num1) + " x " + str(num2)  + " = " + str((num1*num2)) )
#     num1+=1
#     num2+=1

# lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
# #Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

# for l in lst:
#     print(l)

# #Use for loop to iterate from 0 to 100 and print only even numbers

# # for x in range(0,100,2):
# #     print(x)

# # for x in range(100):
# #     if x % 2 == 0:
# #         print(x)
# # else:   
# #     print("THE END")

# # for x in range(100,0,-3):
# #     print(x)

# for x in range(100):
#     if x % 2 != 0:
#         print(x)
    
    
# for num in range(1, 101, 2):
#     print(num)

# #Exercises: Level 2
# #Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# #The sum of all numbers is 5050.

# sum = 0
# start = 0
# end = 101
# odd = 0
# even = 0
# for x in range(start,end,1):
#     sum+=x

# print("The sum of all number is ", sum)


# #Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# odd = 0
# even = 0
# for x in range(0,101,1):
#     if x % 2 == 0:
#         even += x
#     else:
#         odd += x

# print("The sum of all evens is {} and the sum of all odds is {}".format(even,odd) )

# countries = [
#   'Afghanistan',
#   'Albania',
#   'Algeria',
#   'Andorra',
#   'Angola',
#   'Antigua and Barbuda',
#   'Argentina',
#   'Armenia',
#   'Australia',
#   'Austria',
#   'Azerbaijan',
#   'Bahamas',
#   'Bahrain',
#   'Bangladesh',
#   'Barbados',
#   'Belarus',
#   'Belgium',
#   'Belize',
#   'Benin',
#   'Bhutan',
#   'Bolivia',
#   'Bosnia and Herzegovina',
#   'Botswana',
#   'Brazil',
#   'Brunei',
#   'Bulgaria',
#   'Burkina Faso',
#   'Burundi',
#   'Cambodia',
#   'Cameroon',
#   'Canada',
#   'Cape Verde',
#   'Central African Republic',
#   'Chad',
#   'Chile',
#   'China',
#   'Colombi',
#   'Comoros',
#   'Congo (Brazzaville)',
#   'Congo',
#   'Costa Rica',
#   "Cote d'Ivoire",
#   'Croatia',
#   'Cuba',
#   'Cyprus',
#   'Czech Republic',
#   'Denmark',
#   'Djibouti',
#   'Dominica',
#   'Dominican Republic',
#   'East Timor (Timor Timur)',
#   'Ecuador',
#   'Egypt',
#   'El Salvador',
#   'Equatorial Guinea',
#   'Eritrea',
#   'Estonia',
#   'Ethiopia',
#   'Fiji',
#   'Finland',
#   'France',
#   'Gabon',
#   'Gambia, The',
#   'Georgia',
#   'Germany',
#   'Ghana',
#   'Greece',
#   'Grenada',
#   'Guatemala',
#   'Guinea',
#   'Guinea-Bissau',
#   'Guyana',
#   'Haiti',
#   'Honduras',
#   'Hungary',
#   'Iceland',
#   'India',
#   'Indonesia',
#   'Iran',
#   'Iraq',
#   'Ireland',
#   'Israel',
#   'Italy',
#   'Jamaica',
#   'Japan',
#   'Jordan',
#   'Kazakhstan',
#   'Kenya',
#   'Kiribati',
#   'Korea, North',
#   'Korea, South',
#   'Kuwait',
#   'Kyrgyzstan',
#   'Laos',
#   'Latvia',
#   'Lebanon',
#   'Lesotho',
#   'Liberia',
#   'Libya',
#   'Liechtenstein',
#   'Lithuania',
#   'Luxembourg',
#   'Macedonia',
#   'Madagascar',
#   'Malawi',
#   'Malaysia',
#   'Maldives',
#   'Mali',
#   'Malta',
#   'Marshall Islands',
#   'Mauritania',
#   'Mauritius',
#   'Mexico',
#   'Micronesia',
#   'Moldova',
#   'Monaco',
#   'Mongolia',
#   'Morocco',
#   'Mozambique',
#   'Myanmar',
#   'Namibia',
#   'Nauru',
#   'Nepal',
#   'Netherlands',
#   'New Zealand',
#   'Nicaragua',
#   'Niger',
#   'Nigeria',
#   'Norway',
#   'Oman',
#   'Pakistan',
#   'Palau',
#   'Panama',
#   'Papua New Guinea',
#   'Paraguay',
#   'Peru',
#   'Philippines',
#   'Poland',
#   'Portugal',
#   'Qatar',
#   'Romania',
#   'Russia',
#   'Rwanda',
#   'Saint Kitts and Nevis',
#   'Saint Lucia',
#   'Saint Vincent',
#   'Samoa',
#   'San Marino',
#   'Sao Tome and Principe',
#   'Saudi Arabia',
#   'Senegal',
#   'Serbia and Montenegro',
#   'Seychelles',
#   'Sierra Leone',
#   'Singapore',
#   'Slovakia',
#   'Slovenia',
#   'Solomon Islands',
#   'Somalia',
#   'South Africa',
#   'Spain',
#   'Sri Lanka',
#   'Sudan',
#   'Suriname',
#   'Swaziland',
#   'Sweden',
#   'Switzerland',
#   'Syria',
#   'Taiwan',
#   'Tajikistan',
#   'Tanzania',
#   'Thailand',
#   'Togo',
#   'Tonga',
#   'Trinidad and Tobago',
#   'Tunisia',
#   'Turkey',
#   'Turkmenistan',
#   'Tuvalu',
#   'Uganda',
#   'Ukraine',
#   'United Arab Emirates',
#   'United Kingdom',
#   'United States',
#   'Uruguay',
#   'Uzbekistan',
#   'Vanuatu',
#   'Vatican City',
#   'Venezuela',
#   'Vietnam',
#   'Yemen',
#   'Zambia',
#   'Zimbabwe',
# ];
# print(type(countries))

# #Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

# for x in countries:
#     if "land" in x:
#         print(x)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
from operator import contains


lst = ['banana', 'orange', 'mango', 'lemon']
# x = 0
# position = -1
# nl = []
# n = list()
# while x <= len(lst):
#     x +=1
#     nl += [position]
#     n += (lst[position])
#     position-=1
#     if position == -5:
#         break
    


#print(n)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
lst = ['banana', 'orange', 'mango', 'lemon']

list = []
y = -1
position = 0
for x in lst:
    position = (lst[y])
    y-=1
    list += [position]

print(list)

import countries 
#Go to the data folder and use the countries_data.py file.
#What are the total number of languages in the data
languages = 0
total = 0
languages = set()

for country in countries:
    languages.update(country['languages'])

print("Total number of languages: ", len(languages))