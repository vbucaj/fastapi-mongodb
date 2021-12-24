from pydantic import BaseModel, EmailStr, Field
from bson import ObjectId
from typing import Optional

class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Valmir Bucaj",
                "email": "bucajvalmir@gmail.com",
                "course_of_study": "AI and Machine Learning",
                "year": 3,
                "gpa": "3.98",
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Daors Bucaj",
                "email": "daors.bucaj@gmail.com",
                "course_of_study": "Space engineering",
                "year": 1,
                "gpa": "4.0",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error, 
        "code": code, 
        "message": message
        }