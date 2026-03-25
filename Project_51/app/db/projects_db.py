from app.db.connection import projects_collection
from bson import ObjectId
from app.models.projects_schema import new_project, update_project, delete_project
from app.utils.mongo_handeler import convert_objectid_in_list


def add_user_project(data: new_project) -> str | None:
    """add new project
    on success: doc id
    on failure: None"""
    try:
        doc_id = projects_collection.insert_one(
            {
                "user_id": data.user_id,
                "title": data.title,
                "desc": data.desc,
                "catagories": data.catagories,
                "last_modified": data.last_modified,
                "tech": data.tech,
                "source": data.source,
                "docs": data.docs,
                "project": data.project,
                "start_date": data.start_date,
                "end_date": data.end_date,
                "organization": data.organization,
            }
        ).inserted_id
    except Exception as err:
        print("Error while add project on db : ", err)
        return None

    if not doc_id:
        return None

    return str(doc_id)


def edit_user_project(data: update_project) -> bool | None:
    """update a project
    on success: True
    on failure: None"""
    try:
        status = projects_collection.update_one(
            {"_id": ObjectId(data.project_id), "user_id": data.user_id},
            {
                "$set": {
                    "title": data.title,
                    "desc": data.desc,
                    "catagories": data.catagories,
                    "last_modified": data.last_modified,
                    "tech": data.tech,
                    "source": data.source,
                    "docs": data.docs,
                    "project": data.project,
                    "start_date": data.start_date,
                    "end_date": data.end_date,
                    "organization": data.organization,
                }
            },
        ).acknowledged
    except Exception as err:
        print("Error while edit project on db : ", err)
        return None

    if not status:
        return False

    return True


def remove_user_project(data: delete_project) -> bool | None:
    """delete a project
    on success: True
    on failure: None"""
    try:
        count = projects_collection.delete_one(
            {"_id": ObjectId(data.project_id), "user_id": data.user_id},
        ).deleted_count
    except Exception as err:
        print("Error while delete project from db : ", err)
        return None

    if not count:
        return False

    return True


def get_projects_of_user(user_id: str) -> list | None:
    """get user projects
    on success: project data
    on failure: None"""
    try:
        data = projects_collection.find({"user_id": user_id})
    except Exception as err:
        print("Error while get projects from db : ", err)
        return None

    if not data:
        return False

    return convert_objectid_in_list(data)


def get_projects_of_user_by_catagory(user_id: str, catagories: list) -> list | None:
    """get all projects of user by catagories
    on success: list of all projects,
    on failure: None"""
    # print(list(catagories))
    try:
        data = projects_collection.find(
            {"user_id": user_id, "catagories": {"$in": catagories}}
        )
    except Exception as err:
        print("Error while getting all projects by catagory: ", err)
        return None

    data = convert_objectid_in_list(data)
    return data
