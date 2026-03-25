from bson import ObjectId
from app.db.connection import skills_collection
from app.utils.mongo_handeler import convert_objectid_in_list
from app.models.skills_schema import new_skill, update_skill, delete_skill


def add_a_skill(data: new_skill) -> None | str:
    """add new skill
    on success: inserted id,
    on failure: None"""
    try:
        status = skills_collection.insert_one(
            {
                "user_id": data.user_id,
                "title": data.title,
                "desc": data.desc,
                "catagories": data.catagories,
                "last_modified": data.last_modified,
            }
        ).inserted_id

    except Exception as err:
        print("Error while add new skill: ", err)
        return None

    return str(status)


def edit_a_skill(data: update_skill) -> None | str:
    """update a skill
    on success: Modified count,
    on failure: None"""
    try:
        status = skills_collection.update_one(
            {"_id": ObjectId(data.skill_id), "user_id": data.user_id},
            {
                "$set": {
                    "title": data.title,
                    "desc": data.desc,
                    "catagories": data.catagories,
                    "last_modified": data.last_modified,
                }
            },
        ).modified_count
    except Exception as err:
        print("Error while update a skill: ", err)
        return None

    return str(status)


def remove_a_skill(data: delete_skill) -> None | str:
    """Delete a skill
    on success: Deleted count,
    on failure: None"""
    try:
        status = skills_collection.delete_one(
            {"_id": data.skill_id, "user_id": data.user_id}
        ).deleted_count
    except Exception as err:
        print("Error while Delete a skill: ", err)
        return None

    return str(status)


def get_skills_of_user(user_id: str) -> list | None:
    """get all skills of user
    on success: list of all skills,
    on failure: None"""
    try:
        data = skills_collection.find({"user_id": user_id})
    except Exception as err:
        print("Error while getting all skills: ", err)
        return None

    data = convert_objectid_in_list(data)
    return data


def get_skills_of_user_by_catagory(user_id: str, catagories: list) -> list | None:
    """get all skills of user by catagories
    on success: list of all skills,
    on failure: None"""
    # print(list(catagories))
    try:
        data = skills_collection.find(
            {"user_id": user_id, "catagories": {"$in": catagories}}
        )
    except Exception as err:
        print("Error while getting all skills by catagory: ", err)
        return None

    data = convert_objectid_in_list(data)
    return data
