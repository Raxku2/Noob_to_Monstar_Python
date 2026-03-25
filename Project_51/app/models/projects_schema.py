from pydantic import BaseModel


class new_project(BaseModel):
    user_id: str
    title: str
    desc: str
    catagories: list[str]
    last_modified: str
    tech: list[str] | None
    source: str | None
    docs: str | None
    project: str | None
    start_date: str | None
    end_date: str | None
    organization: str | None


class update_project(new_project):
    project_id: str


class delete_project(BaseModel):
    user_id: str
    project_id: str
