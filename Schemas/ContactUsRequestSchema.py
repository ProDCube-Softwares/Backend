import pydantic


class ContactUsRequestSchema(pydantic.BaseModel):
    name: str
    email: str
    message: str
    contact: str
    country: str | None
    region: str | None
