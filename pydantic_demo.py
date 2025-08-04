from pydantic import BaseModel

# Pydantic is a Data Validation and Serialization/parsing Framework for Python. 
# It ensures that the data you are working with is correct,structured and type-safe.

class Student(BaseModel):
    name:str='Nandavaram Mahesh'
    
new_student = {}

student = Student(**new_student)    

print(student.name)
