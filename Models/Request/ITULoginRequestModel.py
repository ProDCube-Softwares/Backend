import pydantic
from fastapi import Form


class ITULoginRequestModel(pydantic.BaseModel):
    email: str
    password: str

    @classmethod
    def asForm(
            cls,
            email: str = Form(...),
            password: str = Form(...)
    ) -> "ITULoginRequestModel":
        return cls(email=email, password=password)
