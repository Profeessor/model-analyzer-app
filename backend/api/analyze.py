from fastapi import APIRouter
from schemas.analyze import AnalysisRequest
from models.lfm_infer import run_model
from db.supabase import supabase

router = APIRouter()

@router.post("/")
def analyze(request: AnalysisRequest):
    # Use your actual model function
    result = run_model(request.data)
    # Store in Supabase
    supabase.table("analysis_history").insert({
        "user_id": request.user_id,
        "data": request.data,
        "alpha": result["alpha"]
    }).execute()

    return {"params": result}
