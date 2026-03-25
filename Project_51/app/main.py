from fastapi import FastAPI, Response, status
from fastapi.responses import RedirectResponse, JSONResponse
from app.db.connection import is_db_a_connected
from app.middleware.cors import cors_middleware
from app.routers.auth.google_auth import router as GoogleAuth
from app.routers.skills.skill import router as Skills
from app.routers.project.project import router as Projects
from app.routers.user.user import info as UserInfo

app = FastAPI(title="Torkoal Portfolio Manager", version="0.0.1")

cors_middleware(app)

app.include_router(Skills)  # skill routes
app.include_router(Projects)
app.include_router(UserInfo)
app.include_router(GoogleAuth)  # handel g auth


@app.get("/")
def root():
    """Root redirects to swagger"""
    return RedirectResponse("/docs", status_code=status.HTTP_308_PERMANENT_REDIRECT)


@app.get("/health")
def health():
    """check API and DB Helth"""
    try:
        db_status = is_db_a_connected()
    except:
        print("Error while health check")
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse({"API": True, "DB": db_status})
