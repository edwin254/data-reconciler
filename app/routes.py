from fastapi import APIRouter

from app.views import dashboard_router

router = APIRouter()


router.include_router(dashboard_router)