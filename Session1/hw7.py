n = int(input("Type in your number ? "))
s = int((n-1)/2)
v = int(n/2)
if n%2 == 1 : 
    for i in range(s+1):
        print ("x*", end = '')
    print("x")
    print()
else: 
    for i in range (v+1):
        print("x*", end = '')
    print()
