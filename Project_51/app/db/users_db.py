from app.db.connection import user_collection


def add_user() -> None | str:
    """Create New user
    on success: User id,
    on failure: None"""

    try:
        status = user_collection.insert_one(
            {"name": "Rakesh", "email": "rakeshkund3355@gmail.com", "dp": None}
        ).inserted_id
    except Exception as err:
        print("Error while Creating New User: ", err)
        return None

    return str(status)


def update_user():
    pass


def delete_user():
    pass


def get_user():
    pass


def update_last_activity():
    pass
