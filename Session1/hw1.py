# 1. Boolean is the value that either true or false
#  Ex: 6==7 => False, 7==(4+3) => True, 5 != 5 => False 
#3. Nested conditional is a conditional that nested within another condition 
x = int(input("Type  "))
if  x <10 :
        print("small number")
else: 
    if x <20: 
        print("Tiny number")
    else :
        print("big number")