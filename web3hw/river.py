from mongoengine import Document, StringField, IntField

class river(Document):
    name = StringField()
    continent = StringField()
    length = IntField()