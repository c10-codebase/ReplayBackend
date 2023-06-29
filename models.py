from mongoengine import Document, StringField ,IntField

class User_data(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    mobile = IntField(required=True)