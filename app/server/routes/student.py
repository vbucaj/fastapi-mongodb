from bson.objectid import ObjectId
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

import sys

sys.path.append("C:\\Users\\Valmir&Ana\\Documents\\fastapi-mongodb")

from app.server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from app.server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()

#route to post/add student data to the database
@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully.")

#route to retreive ALL the students from the database
@router.get("/", response_description= 'All students retreived')
async def retreive_all_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, 'All student data retreived successfully')
    return ResponseModel(students, 'There are no records of students in the database. Empty list returned.')

#route to retreive a single student by id from the database
@router.get("/{id}", response_description=f"Student retreived successfully")
async def retreive_single_student(id: str):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, f'Student with id {id} retreived successfully')
    return ErrorResponseModel('An Error Occured!',404, f'There is no student with id {id} in the database')

#route to update student data
@router.put("/{id}")