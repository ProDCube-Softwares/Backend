from Models.BaseMongoModel import BaseMongoModel


class ContactUsModel(BaseMongoModel):
    name: str
    email: str
    message: str
    location: str = "Base Locations"
