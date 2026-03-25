from app.db.connection import user_collection
from app.models.user_schema import user_information, user_edu, user_experience
from bson import ObjectId
from app.utils.mongo_handeler import convert_objectid_in_doc, convert_objectid_in_list


# add userinfo
def add_user_info(data: user_information, user_id: str):
    info_data = data.dict()

    if not info_data:
        raise ValueError("No data provided for insert")

    try:
        status = user_collection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": info_data}
        )

        if status.modified_count == 0:
            print("No Changes made")
            return False

        return True

    except UserExistsError:
        raise UserExistsError("User already exists")

    except Exception as err:
        raise Exception(f"error while adding user_info: {err}")


# read user info
def show_user_info(data: str):

    try:
        status = user_collection.find_one({"_id": ObjectId(data)})

        if not status:
            print("No Data found")
            return None

        return convert_objectid_in_doc(status)

    except Exception as err:
        raise Exception(f"error while getting user_info: {err}")


# update user info
def update_user_info(data: user_information, user_id: str):
    info_data = data.dict(exclude_unset=True, exclude_none=True)

    if not info_data:
        raise ValueError("No data provided for update")

    try:
        status = user_collection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": info_data}
        )

        if status.matched_count == 0:
            raise Exception("User Not Found")

        if status.modified_count == 0:
            print("No Changes made")
            return False

        return True

    except Exception as err:
        raise Exception(f"error while update user_info: {err} ")


# delete user info
def remove_user_info(data: str):

    try:
        status = user_collection.delete_one({"_id": ObjectId(data)})

        if status.deleted_count == 0:
            # print("No Data found")
            return False

        return True

    except Exception as err:
        raise Exception(f"error while delete user_info: {err}")


# add edu
def add_user_edu(user_id: str, data: user_edu):
    try:
        edu_data = data.dict(exclude_unset=True)

        if not edu_data:
            raise ValueError("Education data not provided")

        edu_data["_id"] = ObjectId()

        status = user_collection.update_one(
            {"_id": ObjectId(user_id)}, {"$push": {"education": edu_data}}
        )

        if status.matched_count == 0:
            raise Exception("User not Found")

        if status.modified_count == 0:
            return False

        return True

    except Exception as err:
        raise Exception(f"Error while adding user education: {err}")


# view edu
def show_user_edu(data: str):

    try:
        status = user_collection.find_one(
            {"_id": ObjectId(data)}, {"education": 1, "_id": 0}
        )

        if not status:
            print("No Data found")
            return None

        education = status.get("education", [])

        if not education:
            # print("No Data found")
            return None

        return convert_objectid_in_list(education)

    except Exception as err:
        raise Exception(f"error while getting user_education: {err}")


# update edu
def update_user_edu(user_id: str, edu_id: str, data: user_edu):
    try:
        edu_data = data.dict(exclude_unset=True, exclude_none=True)

        if not edu_data:
            raise ValueError("Education data not provided")

        update_fields = {f"education.$.{k}": v for k, v in edu_data.items()}

        status = user_collection.update_one(
            {"_id": ObjectId(user_id), "education._id": ObjectId(edu_id)},
            {"$set": update_fields},
        )

        if status.matched_count == 0:
            raise Exception("User not Found")

        if status.modified_count == 0:
            return False

        return True

    except Exception as err:
        raise Exception(f"Error while updateing user education: {err}")


# delete edu
def remove_user_edu(data: str, edu_id: str):

    try:
        status = user_collection.update_one(
            {"_id": ObjectId(data)}, {"$pull": {"education": {"_id": ObjectId(edu_id)}}}
        )

        if status.modified_count == 0:
            # print("No Data found")
            return False

        return True

    except Exception as err:
        raise Exception(f"error while delete user_edu: {err}")


# add exp
def add_user_exp(user_id: str, data: user_experience):
    try:
        exp_data = data.dict(exclude_unset=True)

        if not exp_data:
            raise ValueError("No experiense provided")

        exp_data["_id"] = ObjectId()

        status = user_collection.update_one(
            {"_id": ObjectId(user_id)}, {"$push": {"experience": exp_data}}
        )

        if status.matched_count == 0:
            raise Exception("User Not found")

        if status.modified_count == 0:
            return False

        return True

    except Exception as err:
        raise Exception(f"err while adding user exp {err}")


# view exp
def show_user_exp(user_id: str):
    try:
        status = user_collection.find_one(
            {"_id": ObjectId(user_id)}, {"experience": 1, "_id": 0}
        )

        experience = status.get("experience", [])

        if not experience:
            return None

        return convert_objectid_in_list(experience)

    except Exception as err:
        raise Exception(f"err while getting user exp: {err}")


# update exp
def update_user_exp(user_id: str, exp_id: str, data: user_experience):
    try:
        exp_data = data.dict(exclude_unset=True, exclude_none=True)

        if not exp_data:
            raise ValueError("No experiense provided")

        update_fields = {
            f"experience.$.{key}": value for key, value in exp_data.items()
        }

        status = user_collection.update_one(
            {"_id": ObjectId(user_id), "experience._id": ObjectId(exp_id)},
            {"$set": update_fields},
        )

        if status.matched_count == 0:
            raise Exception("User Not found")

        if status.modified_count == 0:
            return False

        return True

    except Exception as err:
        raise Exception(f"err while updating user exp {err}")


# del exp
def remove_user_exp(data: str, exp_id: str):

    try:
        status = user_collection.update_one(
            {"_id": ObjectId(data)},
            {"$pull": {"experience": {"_id": ObjectId(exp_id)}}},
        )

        if status.modified_count == 0:
            # print("No Data found")
            return False

        return True

    except Exception as err:
        raise Exception(f"error while delete user_exp: {err}")
