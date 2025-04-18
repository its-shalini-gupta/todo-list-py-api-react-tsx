from sqlalchemy import Column, Integer, String
from app.database import Base

class CourseModel(Base):
    __tablename__ = 'mst_courses'
    
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_code = Column(String(15), nullable=False , index=True)
    course_name = Column(String(60), nullable=True, index=True)