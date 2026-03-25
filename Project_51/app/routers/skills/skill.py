from fastapi import APIRouter, Response, status, Query
from fastapi.responses import JSONResponse
from app.db.skills_db import (
    get_skills_of_user,
    get_skills_of_user_by_catagory,
    add_a_skill,
    edit_a_skill,
    remove_a_skill,
)
from app.models.skills_schema import new_skill, update_skill, delete_skill

router = APIRouter(prefix="/skills", tags=["Skills"])


@router.post("/")
def add_skill(payload: new_skill):
    try:
        skill_id = add_a_skill(payload)
    except Exception as err:
        print("Error while user skills add route: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not skill_id:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(skill_id, status_code=status.HTTP_201_CREATED)


@router.put("/")
def edit_skill(payload: update_skill):
    try:
        modified_count = edit_a_skill(payload)
    except Exception as err:
        print("Error while user skills edit route: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not modified_count:
        return Response(status_code=status.HTTP_304_NOT_MODIFIED)

    return Response(status_code=status.HTTP_200_OK)


@router.delete("/")
def del_skill(payload: delete_skill):
    try:
        deleted = remove_a_skill(payload)
    except Exception as err:
        print("Error while user skills delete route: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not deleted:
        return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/catagories")
def skills_in_catagory(user_id: str, catagories: list[str] = Query(...)):
    try:
        user_skills = get_skills_of_user_by_catagory(
            user_id=user_id, catagories=catagories
        )
    except Exception as err:
        print("Error while user skills by catagory route: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not user_skills:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(user_skills)
    # print(catagories)
    # return "ok"


@router.get("/")
def skills(user_id: str):
    try:
        user_skills = get_skills_of_user(user_id)
    except Exception as err:
        print("Error while user skills route: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not user_skills:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(user_skills)
