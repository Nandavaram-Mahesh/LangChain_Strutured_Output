from pydantic import BaseModel

# Pydantic is a Data Validation and Serialization/parsing Framework for Python. 
# It ensures that the data you are working with is correct,structured and type-safe.

class Student(BaseModel):
    name:str
    
new_student = {'name':"Nandavaram Mahesh"}

student = Student(**new_student)    

print(student)
# name='Nandavaram Mahesh'
print(type(student))
# <class '__main__.Student'>  ----> Pydantic Object