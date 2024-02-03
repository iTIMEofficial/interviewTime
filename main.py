from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from starlette.responses import FileResponse 
app = FastAPI()
app.mount("/", StaticFiles(directory="ui",html = True), name="static")
@app.get("/")
async def read_index():
    return FileResponse('ui/index.html')