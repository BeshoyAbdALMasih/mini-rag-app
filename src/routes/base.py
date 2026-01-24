from fastapi import FastAPI,APIRouter,Depends
from helper.config import get_settings, Settings


base_router=APIRouter(
    prefix="/api/v1",tags=["api_v1"]
)


@base_router.get('/')
async def welcome(app_settings: Settings =Depends(get_settings)):
    #app_settings=get_settings()
    App_Name=app_settings.APP_NAME
    App_Version=app_settings.APP_VERSION
    return {
        'App_Name':App_Name,
        "App_version":App_Version,
    }