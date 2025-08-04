from pydantic import BaseModel,EmailStr,Field
from typing import Optional

# Pydantic is a Data Validation and Serialization/parsing Framework for Python. 
# It ensures that the data you are working with is correct,structured and type-safe.

class Student(BaseModel):
    name:str='Nandavaram Mahesh'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')
    
new_student = {'age':29,'email':'aDkCt@gmail.com'}

student = Student(**new_student)    

print(student)
# name='Nandavaram Mahesh' age=29 email='aDkCt@gmail.com' cgpa=5

# Converting from pydantic object to python dict
student_dict = dict(student)
print(student_dict['cgpa'])
# 5

# Converting from pydantic object to json
student_json = student.model_dump_json()
print(student_json)
# {"name":"Nandavaram Mahesh","age":29,"email":"aDkCt@gmail.com","cgpa":5.0}


