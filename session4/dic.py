dic = {
    "lm" : 'lam',
    'eat' : 'an',
    'learn' : 'hoc',

}
print("lm   eat     learn")



while True:
    v = input("Word u want to learn = ?? ")
    if v not in dic:
        a = input('not found ,contribute, Y/N').upper()
        if a == "Y":
            a =input("Nhap nghia")
            dic[v]= a
            print(dic)
        else :
            print("ok")
    else:
        print(dic[v])


