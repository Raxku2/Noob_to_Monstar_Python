from fastapi import APIRouter, status, Response
from app.db.users_db import add_user

# from app.models.user_schema import new_user

router = APIRouter(prefix="/gauth", tags=["Google Auth"])


@router.get("/verify")
def verify_google_auth_token():
    try:
        userid = add_user()
    except Exception as err:
        print("Error while verify google auth: ", err)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not userid:
        return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

    return Response(userid)
