from typing import Union
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from app.core.config import templates

dashboard_router = APIRouter()

@dashboard_router.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )