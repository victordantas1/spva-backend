from fastapi import FastAPI

from api.v1.users import router as users_router
from api.v1.jobs import router as jobs_router

app = FastAPI()

app.include_router(users_router)
app.include_router(jobs_router)
