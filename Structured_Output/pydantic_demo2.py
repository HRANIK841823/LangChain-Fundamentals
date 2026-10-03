from pydantic import BaseModel,EmailStr,Field
from typing import Optional


class JobApplication(BaseModel):
    name: str ="Unknown" 

    experience:Optional[int]=None
    
    email:EmailStr

    expected_salary:int=Field(gt=0 ,description="Expected Annual Salary of the candidate")


newApplication={
     "email": "abc@gmail.com", 
    "experience": "3", 
    "expected_salary" : 50000
}

application=JobApplication(**newApplication)

#print(application)
#pydantic makes data into object 
# print(application.email)


#Object to dictionary
application_dict=application.model_dump()

print(application_dict)

print(application_dict['experience'])

#object to json format
application_json=application.model_dump_json()

print(application_json)