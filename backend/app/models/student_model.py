from sqlalchemy import Column, Integer, String, Boolean, Date , BigInteger , ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship
from app.models.course_model import CourseModel

class StudentModel(Base):
    __tablename__ = 'mst_students'

    stud_id = Column(Integer, primary_key=True, autoincrement=True)
    stud_name = Column(String(15), nullable=False , index=True)
    stud_dob = Column(Date, nullable=True)
    stud_doj = Column(Date, nullable=True)
    stud_gender_id = Column(Integer,  nullable=False)
    stud_email = Column(String(50), nullable=True)
    stud_phone_no = Column(String(15), nullable=True)
    stud_address = Column(String(100), nullable=True)
    stud_course_id = Column(BigInteger, ForeignKey("mst_courses.course_id"), nullable=False)
    stud_photo = Column(String(100), nullable=True)
    isactive = Column(Boolean, default=True, nullable=False)


    stud_course_join = relationship(
    "CourseModel",
    primaryjoin="foreign(StudentModel.stud_course_id) == CourseModel.course_id",
    lazy="joined",
    viewonly=True
    )