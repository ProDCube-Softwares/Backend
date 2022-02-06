from beanie import Document
from passlib.context import CryptContext

passwordContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


class InternalUserModel(Document):
    name: str
    email: str
    password: str
    role: str

    def setPassword(self) -> None:
        self.password = passwordContext.hash(self.password)

    def verifyPassword(self, password: str) -> bool:
        return passwordContext.verify(password, self.password)

    class Collection:
        name = "InternalUsers"

    class Config:
        arbitrary_types_allowed = True
