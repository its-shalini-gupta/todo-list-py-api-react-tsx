from sqlalchemy.orm import Session
from app.models.student_model import StudentModel
from fastapi import HTTPException
from typing import Optional

def get_stud(db: Session, skip: int = 0, limit: int = 10, search: Optional[str] = None):
    query = db.query(StudentModel).filter(StudentModel.isactive == True)

    if search:
        query = query.filter(StudentModel.stud_name.ilike(f"%{search}%"))
    query = query.order_by(StudentModel.stud_id.asc())

    total = query.count()
    stud_data = query.offset(skip).limit(limit).all()

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": stud_data
    }


def create_stud(data ,db: Session, file_path):
    existing_stud = db.query(StudentModel).filter(StudentModel.stud_name == data.name_var).first()
    if existing_stud:
        raise HTTPException(status_code = 400, detail=f"Student '{data.name_var}' already exists.")
        
    try:
        new_stud = StudentModel(
            stud_name =  data.name_var,
            stud_dob =  data.date_of_birth_var,
            stud_doj =  data.date_of_join_var,
            stud_gender_id =  data.gender_var,
            stud_email =  data.email_var,
            stud_phone_no =  data.phone_number_var,
            stud_address =  data.address_var,
            stud_course_id =  data.course_var,
            stud_photo =  file_path,
            isactive =  1,
        )

        db.add(new_stud)
        db.commit()
        db.refresh(new_stud)
        return {"message": f"Student '{data.name_var}' added successfully!", "sorg_id": new_stud.stud_id}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)} ")
    

def delete_stud(id: int, db : Session):
    existing_stud = db.query(StudentModel).filter(StudentModel.stud_id == id).first()

    if existing_stud:
        existing_stud.isactive = 0
        db.commit()
        db.refresh(existing_stud)
        return {"message": f"Student '{existing_stud.stud_name}' Deleted successfully! "}

def stud_by_id(id: int, db: Session):
    studData = db.query(StudentModel).filter(StudentModel.stud_id == id).first()

    return {
        "id_var": studData.stud_id,
        "name_var": studData.stud_name,
        "date_of_birth_var": studData.stud_dob,
        "date_of_join_var": studData.stud_doj,
        "gender_var": studData.stud_gender_id,
        "email_var": studData.stud_email,
        "phone_number_var": studData.stud_phone_no,
        "address_var": studData.stud_address,
        "course_var": studData.stud_course_id,
        "picturePreview": studData.stud_photo,
    }


def update_stud(id: int, data, db: Session, file_path):
    existing_stud = db.query(StudentModel).filter(StudentModel.stud_id == id).first()

    if existing_stud:
   
        existing_stud.stud_name = data.name_var,
        existing_stud.stud_dob = data.date_of_birth_var,
        existing_stud.stud_doj = data.date_of_join_var,
        existing_stud.stud_gender_id = data.gender_var,
        existing_stud.stud_email = data.email_var,
        existing_stud.stud_phone_no = data.phone_number_var,
        existing_stud.stud_address = data.address_var,
        existing_stud.stud_course_id = data.course_var,
        existing_stud.stud_photo = file_path,

        db.commit()
        db.refresh(existing_stud)
        return {"message": f"Student '{existing_stud.stud_name}' Updated Successfully! "}