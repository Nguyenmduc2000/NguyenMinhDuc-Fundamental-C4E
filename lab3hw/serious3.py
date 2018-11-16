
def is_inside(x,y,x1,y1,h,w):
    if x1 <= x <= x1+h and y1 <= y <= y1+h: 
        print("Inside")
    else: 
        print("no")
is_inside(10,20,9,10, 10,20)