from pydantic import BaseModel

class User(BaseModel):
    name: str
    age:int

user_data={
    "name":"HR Anik",
    "age":"25"
}

user=User(**user_data)

#Print(User)
print(user)