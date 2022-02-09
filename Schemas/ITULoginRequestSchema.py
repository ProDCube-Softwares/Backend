import pydantic
from fastapi import Form


class ITULoginRequestSchema(pydantic.BaseModel):
    email: str
    password: str

    @classmethod
    def asForm(
            cls,
            email: str = Form(...),
            password: str = Form(...)
    ) -> "ITULoginRequestSchema":
        return cls(email=email, password=password)
