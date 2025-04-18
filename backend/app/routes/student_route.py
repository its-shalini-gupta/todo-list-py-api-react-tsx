from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.services.student_service import get_stud, create_stud, delete_stud, stud_by_id, update_stud
from app.database import get_db
from app.schemas.student_schema import StudentCreate
from app.models.course_model import CourseModel
from app.models.student_model import StudentModel
import os
import base64
import imghdr


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("")
async def get_stud_route(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    search: str = Query(None, description="Search keyword for Student Name")
):
    return get_stud(db, skip, limit, search)

@router.post("/create")
async def create_stud_route(data: StudentCreate, db: Session = Depends(get_db)):

    base64_data = data.photo_path_blob  
    if base64_data:
        if isinstance(base64_data, bytes):
            base64_data = base64_data.decode("utf-8")  # Convert bytes to string

        if base64_data.startswith("data:image"):
            base64_data = base64_data.split(",")[1]

        image_bytes = base64.b64decode(base64_data)

        if base64_data.startswith("data:image"):
            mime_type = base64_data.split(";")[0].split(":")[1]  # Extract MIME type
            file_extension = mime_type.split("/")[-1]  # Get extension (e.g., jpeg, png)
            base64_data = base64_data.split(",")[1]

        image_bytes = base64.b64decode(base64_data)

        detected_ext = imghdr.what(None, h=image_bytes)
        if detected_ext:
            file_extension = detected_ext  # Update if a valid type is detected

        folder_path = os.path.join("images", "Student")
        file_path = os.path.join(folder_path, f"{data.name_var}.{file_extension}")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(image_bytes)
    else:   
        file_path = ''
    return create_stud(data, db, file_path)

@router.put("/delete/{id}")
async def delete_route(id: int , db: Session = Depends(get_db) ):
    return delete_stud(id,db)

@router.get("/by-id/{id}")
async def get_stud_by_id(id: int, db: Session = Depends(get_db)):
    return stud_by_id(id,db)

@router.put("/updated/{id}")
async def updated_route(id: int , data: StudentCreate, db: Session = Depends(get_db) ):

    base64_data = data.photo_path_blob  
    if base64_data:
        if isinstance(base64_data, bytes):
            base64_data = base64_data.decode("utf-8")  # Convert bytes to string

        if base64_data.startswith("data:image"):
            base64_data = base64_data.split(",")[1]

        image_bytes = base64.b64decode(base64_data)

        if base64_data.startswith("data:image"):
            mime_type = base64_data.split(";")[0].split(":")[1]  # Extract MIME type
            file_extension = mime_type.split("/")[-1]  # Get extension (e.g., jpeg, png)
            base64_data = base64_data.split(",")[1]

        image_bytes = base64.b64decode(base64_data)

        detected_ext = imghdr.what(None, h=image_bytes)
        if detected_ext:
            file_extension = detected_ext  # Update if a valid type is detected

        folder_path = os.path.join("images", "Student")
        file_path = os.path.join(folder_path, f"{data.name_var}.{file_extension}")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(image_bytes)
    else:   
        file_path = ''
    return update_stud(id,data,db,file_path)

@router.get("/courses")
def search_courses(search: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(CourseModel)
    
    if search:
        query = query.filter(CourseModel.course_name.ilike(f"%{search}%"))
    
    courses = query.all()
    return courses


@router.get("/check-duplicate")
async def check_duplicate(name: str, db: Session = Depends(get_db)):
    # Check if a student with the same name already exists
    existing_student = db.query(StudentModel).filter(StudentModel.stud_name == name).first()
    
    if existing_student:
        return {"exists": True}  # Student with the same name exists
    else:
        return {"exists": False}  # No duplicate found