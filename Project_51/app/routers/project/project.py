from fastapi import APIRouter, Response, status, Query
from fastapi.responses import JSONResponse
from app.models.projects_schema import new_project, update_project, delete_project
from app.db.projects_db import (
    add_user_project,
    edit_user_project,
    remove_user_project,
    get_projects_of_user,
    get_projects_of_user_by_catagory,
)

router = APIRouter(prefix="/projects", tags=["Project"])


@router.post("/")
def create_new_project(payload: new_project):
    try:
        project_id = add_user_project(payload)
    except Exception as err:
        print("Error while user project add route: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not project_id:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(project_id, status_code=status.HTTP_201_CREATED)


@router.put("/")
def edit_skill(payload: update_project):
    try:
        modified_count = edit_user_project(payload)
    except Exception as err:
        print("Error while user project edit route: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not modified_count:
        return Response(status_code=status.HTTP_304_NOT_MODIFIED)

    return Response(status_code=status.HTTP_200_OK)


@router.delete("/")
def del_skill(payload: delete_project):
    try:
        deleted = remove_user_project(payload)
    except Exception as err:
        print("Error while user project delete route: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not deleted:
        return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/catagories")
def skills_in_catagory(user_id: str, catagories: list[str] = Query(...)):
    try:
        user_projects = get_projects_of_user_by_catagory(
            user_id=user_id, catagories=catagories
        )
    except Exception as err:
        print("Error while user projects by catagory route: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not user_projects:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(user_projects)
    # print(catagories)
    # return "ok"


@router.get("/")
def skills(user_id: str):
    try:
        user_projects = get_projects_of_user(user_id)
    except Exception as err:
        print("Error while user project route: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not user_projects:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(user_projects)
