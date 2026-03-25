from pydantic import BaseModel


class new_skill(BaseModel):
    user_id: str
    title: str
    desc: str
    catagories: list[str]
    last_modified: str


class update_skill(new_skill):
    skill_id: str


class delete_skill(BaseModel):
    skill_id: str
    user_id: str


class user_for_get(BaseModel):
    user_id: str
    user_email: str
