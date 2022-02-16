from mongoengine import Document, StringField
from passlib.context import CryptContext

passwordContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


class InternalUserModel(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    role = StringField(default="Admin")

    def verifyPassword(self, password: str) -> bool:
        return passwordContext.verify(password, self.password)

    meta = {"collection": "Internal Users"}
