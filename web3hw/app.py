import mlab 
from river import river 
mlab.connect()

r = river.objects(continent = "Africa")
for i in r:
    print(i.name)
print("_____________________________________")
a = river.objects(continent = "S. America",length__lt = 1000)
for i in a:
    print(i.name)