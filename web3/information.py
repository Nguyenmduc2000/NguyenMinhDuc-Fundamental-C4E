from mongoengine import Document, StringField, IntField, BooleanField

class Information(Document):
    meta = {
        "strict" : False
    }
    name = StringField()
    city = StringField()
    yob = IntField()
    height = IntField()
    weight = IntField()
    available = BooleanField(default=False)
