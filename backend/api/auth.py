from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# GET route
@router.get("/hello")
def say_hello():
    return {"message": "👋 Hello from the auth router!"}

# POST route
class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    return {"status": "Logged in!", "user": request.username}
