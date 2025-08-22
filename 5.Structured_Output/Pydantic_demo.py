from pydantic import BaseModel,EmailStr, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional

class Student(BaseModel):
    name: str="Shivam Singh"
    age:Optional[int] = None
    email: EmailStr 
    cgpa:float = Field(gt=0, le=10, description="CGPA must be between 0 and 10")


new_student ={"age":22, "email": "B6A7o@example.com","cgpa": 9}

student=Student(**new_student)

print(student)