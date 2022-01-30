from datetime import datetime

from beanie import Document


class BaseMongoModel(Document):
    createdAt: datetime

    @classmethod
    def autoAddDate(cls):
        self.