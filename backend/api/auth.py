from fastapi import APIRouter
from schemas.auth import LoginRequest

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "👋 Hello"}

@router.post("/login")
def login(request: LoginRequest):
    return {"status": "Logged in!", "user": request.username}
