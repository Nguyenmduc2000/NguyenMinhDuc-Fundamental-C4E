size= [10, 20, 3, 45, 60, 150 , 200]
a = input('Start ?? Y/N ').upper()
d = 0
while a == 'Y':
    print('Month' )
    print("Hi these r my sheeps:")
    print(size)
    a = max(size)
    print('sheer sheep', a)
    z = (a - 8)
    b = size.index(max(size))
    size[b] = 8
    print(size)
    print('next month')
    for (i,v) in enumerate(size): 
        size[i] = v +50
    d += z
    print(d)
    print(size)
    a = input('Next month ? Y/N').upper()
else: 
    print("THks")
    print('Total money',d * 20 ,'$')