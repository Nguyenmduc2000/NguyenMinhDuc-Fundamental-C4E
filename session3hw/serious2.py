inp = input("Choose type of program u want to do (C, R, U, D) ??").upper()
while inp==("R") or ("C") or ("U") or ("D") :
    if inp == ("R"):
        print("Welcome to our shop, what do you want (C, R, U, D)? R")
        buy = ["shirt", "t-shirt"]
        print("Your items:")
        for(i,v) in enumerate(buy):   
            print(i+1,".", v)
    elif inp == ("C"):
        print("Welcome to our shop, what do you want (C, R, U, D)? C")
        x= input("Enter new items? : ")
        buy.append(x)
        for(i,v) in enumerate(buy):   
            print(i+1,".", v)
    elif inp == ("U"):
        print("Welcome to our shop, what do you want (C, R, U, D)? U")
        n = int(input("items u wanna change ?? "))
        x = input("replace with ? : ")
        buy[n-1] = x 
        for(i,v) in enumerate(buy):   
            print(i+1,".", v)

    elif inp == ("D"):
        print("Welcome to our shop, what do you want (C, R, U, D)? D")
        a = int(input("Position u want to delete ? :"))
        del buy[a-1]
        for(i,v) in enumerate(buy):   
            print(i+1,".", v)
    inp = input("Choose type of program u want to do (C, R, U, D) ??")
