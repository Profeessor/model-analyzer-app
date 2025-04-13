from fastapi import APIRouter
from pydantic import BaseModel
from models.lfm_infer import run_model

router = APIRouter()

class AnalysisRequest(BaseModel):
    user_id: str
    data: list[float]

@router.post("/")
def analyze(request: AnalysisRequest):
    result = run_model(request.data)
    return {"params": result} 


@router.get("/hello")
def say_hello():
    return {"message": "👋 Hello from the backend!"}
