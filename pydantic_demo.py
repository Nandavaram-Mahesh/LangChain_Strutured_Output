from pydantic import BaseModel
from typing import Optional

# Pydantic is a Data Validation and Serialization/parsing Framework for Python. 
# It ensures that the data you are working with is correct,structured and type-safe.

class Student(BaseModel):
    name:str='Nandavaram Mahesh'
    age:Optional[int]=None    
    
new_student = {'age':29}

student = Student(**new_student)    

print(student)
