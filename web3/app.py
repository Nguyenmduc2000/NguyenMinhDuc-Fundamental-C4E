import mlab 
from movie import Movie
from information import Information
from faker import Faker 

faker = Faker("en_US")

# for _ in range(5):
#     print(faker.state())

mlab.connect()

# m = Movie.objects().with_id("5bf801aefb6fc0561fff7dd8")
# print(m.title)
# m.delete()

# movie_list = Movie.objects().first()
# i = movie_list[1]
# print(i)
# i.delete()
# for m in movie_list:
#     print(m)
#     # print(m.title)
#     # print(m.year)

# resource_list = Information.objects

# for i in resource_list:
#     print(i.name, i.yob, sep=" ,")



# m = Movie(title = "Batman", year = 2005, image = "data:image/jpeg;base64,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")
# r = Information(name="Duc", city="Hanoi", yob=2000, height=170, weight = 58) 
# m.save()
# from random import randint
# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     yob = randint(1953, 2000)
#     height = randint(150,190)
#     weight = randint(40,150)
#     r = Information(name=name, city=city, yob = yob, height=height, weight= weight)
#     r.save()

# records = Information.objects(name="Matthew Humphrey")
# print(len(records))
# for r in records:
#     print(r.city)
#     print(r.height)
#     print(r.weight)


# r = Information.objects(height=172)
# print(len(records))
# for i in r:
#     print(i.name)
#     print(i.city)
#     print(i.weight)

# records = Information.objects(height__gt=160,height__lt=170, name__icontains="Emily")
# print(len(records))
# records = Information.objects()

# for r in records: 
#     r. update(set__available=False)

r = Information.objects().with_id("5bf80d15249d370c0c315798")
r.update(set__available=True)