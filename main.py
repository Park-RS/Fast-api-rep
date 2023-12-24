from fastapi import APIRouter, Body, FastAPI, Response, Path, Query, Header
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse, FileResponse
from users import users_router
from fastapi.openapi.utils import get_openapi
import uuid

app = FastAPI()
router = APIRouter()
app.include_router(users_router, prefix="/api/v1")

@app.get("/openapi.json")
def get_open_api_endpoint():
    return get_openapi(title="Your API Title", version="1.0.0", routes=app.routes)
