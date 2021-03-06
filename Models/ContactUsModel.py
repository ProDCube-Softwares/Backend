from datetime import datetime

from mongoengine import DateTimeField, Document, StringField


class ContactUsModel(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    message = StringField(required=True)
    country = StringField(required=True)
    region = StringField(required=True)
    createdAt = DateTimeField(default=datetime.utcnow)

    meta = {"collection": "Contact Us"}
