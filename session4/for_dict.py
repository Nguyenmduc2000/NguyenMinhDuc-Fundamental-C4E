person = {'Name' : 'Duc',
'Game' : "Cs ",
'age' : 18

}
p2 = {'name':'Quan',
'age': 23,
'city': 'Ha Noi'

}
# for i in person.keys() : #tupple
#     print(i, person[i])
# for v in person.values():
#     print(v)
# for k, v in person.items():
#     print(k,v)

p_list = [{'name':'Quan',
'age': 23,
'city': 'Ha Noi'

}, {'Name' : 'Duc',
'Game' : "Cs ",
'age' : 18

}
]
#JSON
# print(p_list)
# print(p_list[0]['age'])
for p in p_list:
    print(p['age'])
