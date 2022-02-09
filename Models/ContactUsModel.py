from datetime import datetime

from beanie import Document


class ContactUsModel(Document):
    name: str
    email: str
    message: str
    country: str | None = None
    region: str | None = None
    createdAt: datetime | None = None

    def assignDate(self):
        self.createdAt = datetime.now().utcnow()

    class Config:
        arbitrary_types_allowed = True

    class Collection:
        name = "Contact Us"
