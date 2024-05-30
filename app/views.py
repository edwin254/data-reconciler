from typing import Union
from fastapi import Request, APIRouter, UploadFile, File
from fastapi.responses import HTMLResponse
from app.core.config import templates
from app.utils import read_csv_data

dashboard_router = APIRouter()

@dashboard_router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="pages/upload.html", context={"id": id}
    )


@dashboard_router.post("/upload", response_class=HTMLResponse)
async def upload_files(request: Request, files: list[UploadFile]= File(...)):

    source, target = files  #Set the target and source values
    source_df = await read_csv_data(source)
    columns = source_df.columns 
    return templates.TemplateResponse(
        request=request, name="pages/upload.html", context={"columns": columns}
    )