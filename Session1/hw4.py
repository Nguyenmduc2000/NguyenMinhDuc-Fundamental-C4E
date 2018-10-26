x = float(input("Type in height ?  "))
w = float(input("Type in weight ? "))
BMI = (w/(x*x))
print("BMI:",BMI)
if BMI < 16 :
    print ("severely underweight")
elif BMI < 18.5 :
    print(" Underweight")
elif BMI <25 :
    print("Overweight")
else :
    print("obese")
    