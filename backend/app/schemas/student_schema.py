from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import date 

class StudentCreate(BaseModel):
    name_var: str = Field(..., min_length=1, max_length=15, description="Name must not be empty and should be between 1 and 15 characters.")
    date_of_birth_var: Optional[date]
    # id_var: int
    date_of_join_var: Optional[date]
    gender_var: Optional[int]
    email_var: Optional[str] = Field(..., max_length=30)
    phone_number_var: Optional[str] = Field(..., max_length=15)
    address_var: Optional[str] = Field(..., max_length=100)
    course_var: Optional[int]
    photo_path_blob: Optional[bytes] = Field(None, max_length=1000000)  # 1MB limit
    isactive: Optional[Union[str, int]] = None
    picturePreview: Optional[str] = Field(None, max_length=100)
    class Config:
        orm_mode = True

