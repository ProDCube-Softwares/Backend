from datetime import datetime

from beanie import Document, Insert, before_event


class BaseMongoModel(Document):
    createdAt: datetime = ""

    @before_event(Insert)
    def autoAddDate(self):
        self.createdAt = datetime.now()
