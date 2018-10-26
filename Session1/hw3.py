from turtle import *
speed(0)
shape("turtle")
for i in range(3,7):
    if i % 2 == 1:
        pencolor("red")
    else:
        pencolor("blue")
    for x in range(i):
        forward(100)
        left(180- 180*(i-2)/i)
mainloop()