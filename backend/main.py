from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.student_route import router as student_router

app = FastAPI(title="Student API", version="1.0.0")
from fastapi.staticfiles import StaticFiles

# Allow CORS from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_router, prefix="/api")
# app.mount("/images", StaticFiles(directory="C:/desktop folder/py_react_tsx_todo/backend/images"), name="images")
app.mount("/images", StaticFiles(directory="backend/images"), name="images")


