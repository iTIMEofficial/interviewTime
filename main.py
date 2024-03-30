from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from starlette.responses import FileResponse 
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/", StaticFiles(directory="ui",html = True), name="static")
@app.get("/")
async def read_index():
    return FileResponse('ui/index.html')

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)