from pydantic import BaseModel, EmailStr
from beanie import Document


#Estructura del documento Users
class User(Document):
    full_name : str
    email: EmailStr
    password : str

    class Collection:
        name = "users"

    class Config:
        schema_extra = {
            "ejemplo" : {
                "full_name" : " Juan Perez",
                "email" : "juan@solucionfactible.com",
                "password" : "shjb%&123"
            }
        }

#Estructura de la informacion del user

class UserData(BaseModel):
    full_name : str
    email : EmailStr

    class Config:
        schema_extra = {
            "ejemplo" : {
                "full_name" : " Juan Perez",
                "email" : "juan@solucionfactible.com"         
            }
        }
