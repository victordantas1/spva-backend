from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


from api.v1.auth import auth_router
from api.v1.users import router as users_router
from api.v1.jobs import router as jobs_router
from api.v1.user_job import router as user_job_router
from api.v1.role_user import router as role_user_router
from api.v1.phone_number import router as phone_number_router
app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(jobs_router)
app.include_router(user_job_router)
app.include_router(role_user_router)
app.include_router(phone_number_router)
app.include_router(auth_router)