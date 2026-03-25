from pydantic import BaseModel


class new_user(BaseModel):
    acc_email: str
    acc_name: str
    acc_dp: str


class user_information(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    address: dict | None = None
    linkedin: str | None = None
    github: str | None = None
    pic: str | None = None
    about: str | None = None


class user_edu(BaseModel):
    institute: str | None = None
    course: str | None = None
    department: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    grade: str | None = None


class user_experience(BaseModel):
    role: str | None = None
    org: str | None = None
    start: str | None = None
    end: str | None = None
    loc: str | None = None
    description: str | None = None
