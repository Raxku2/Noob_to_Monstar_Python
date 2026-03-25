from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from app.db.user_info import (
    add_user_info,
    show_user_info,
    update_user_info,
    remove_user_info,
    add_user_edu,
    show_user_edu,
    update_user_edu,
    remove_user_edu,
    add_user_exp,
    show_user_exp,
    update_user_exp,
    remove_user_exp,
)
from app.models.user_schema import user_information, user_edu, user_experience


# work here for user info routes
info = APIRouter(prefix="/user")
edu = APIRouter(prefix="/education")
exp = APIRouter(prefix="/experience")


@info.get("/{user_id}", tags=["User Info"])
def get_user_info(user_id: str):
    try:
        res = show_user_info(user_id)

        if not res:
            return Response(status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse(res)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@info.post("/{user_id}", tags=["User Info"])
def post_user_info(user_id: str, payload: user_information):
    try:
        res = add_user_info(data=payload, user_id=user_id)

        if not res:
            return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

        return Response(status_code=status.HTTP_201_CREATED)

    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@info.put("/{user_id}", tags=["User Info"])
def put_user_info(user_id: str, payload: user_information):
    try:
        res = update_user_info(data=payload, user_id=user_id)

        if not res:
            return Response(status_code=status.HTTP_304_NOT_MODIFIED)

        return Response(status_code=status.HTTP_200_OK)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@info.delete("/{user_id}", tags=["User Info"])
def delete_user_info(user_id: str):
    try:
        res = remove_user_info(data=user_id)

        if not res:
            return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@edu.get("/{user_id}")
def get_user_edu(user_id: str):
    try:
        res = show_user_edu(user_id)

        if not res:
            return Response(status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse(res)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@edu.post("/{user_id}")
def post_user_edu(user_id: str, payload: user_edu):
    try:
        res = add_user_edu(data=payload, user_id=user_id)

        if not res:
            return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

        return Response(status_code=status.HTTP_201_CREATED)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@edu.put("/{user_id}/{edu_id}")
def put_user_edu(user_id: str, edu_id: str, payload: user_edu):
    try:
        res = update_user_edu(data=payload, user_id=user_id, edu_id=edu_id)

        if not res:
            return Response(status_code=status.HTTP_304_NOT_MODIFIED)

        return Response(status_code=status.HTTP_200_OK)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@edu.delete("/{user_id}/{edu_id}")
def delete_user_edu(user_id: str, edu_id: str):

    try:
        res = remove_user_edu(data=user_id, edu_id=edu_id)

        if not res:
            return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@exp.get("/{user_id}")
def get_user_exp(user_id: str):
    try:
        res = show_user_exp(user_id)

        if not res:
            return Response(status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse(res)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@exp.post("/{user_id}")
def post_user_exp(user_id: str, payload: user_experience):
    try:
        res = add_user_exp(data=payload, user_id=user_id)

        if not res:
            return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

        return Response(status_code=status.HTTP_201_CREATED)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@exp.put("/{user_id}/{exp_id}")
def put_user_exp(user_id: str, exp_id: str, payload: user_experience):
    try:
        res = update_user_exp(data=payload, user_id=user_id, exp_id=exp_id)

        if not res:
            return Response(status_code=status.HTTP_304_NOT_MODIFIED)

        return Response(status_code=status.HTTP_200_OK)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


@exp.delete("/{user_id}/{exp_id}")
def delete_user_exp(user_id: str, exp_id: str):

    try:
        res = remove_user_exp(data=user_id, exp_id=exp_id)

        if not res:
            return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as err:
        return Response(status_code=status.HTTP_417_EXPECTATION_FAILED)


info.include_router(edu, tags=["Education"])
info.include_router(exp, tags=["Experience"])
