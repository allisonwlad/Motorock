import uvicorn
from fastapi import FastAPI
from routers.v1.file_process_router import router


app = FastAPI()


app.include_router(router)
