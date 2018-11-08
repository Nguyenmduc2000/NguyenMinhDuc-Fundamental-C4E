p1 = { 'Name': 'Huy',
'Hours':30 ,
'VND per hour':50
}
p2 = {'Name': 'Quan',
'Hours':20 ,
'VND per hour':40
}
p3={'Name': 'Duc',
'Hours':15,
'VND per hour':35
}
s = [p1,p2,p3]
print(s)
for p in s:
    print(p['Hours'], p['Name'])
print()
for p in s: 
    print(p['Name'], p['Hours']*p['VND per hour'])
x = 0
print()w'
for p in s: 
   a= p['Hours']*p['VND per hour']
   x += a 
print(x)