from fastapi import APIRouter, Query
from db.supabase import supabase
from schemas.history import HistoryRecord
from typing import List

router = APIRouter()

@router.get("/", response_model=List[HistoryRecord])
def get_user_history(user_id: str = Query(..., description="The ID of the user")):
    print("🚀 /history/ endpoint triggered for", user_id)
    result = supabase \
        .table("analysis_history") \
        .select("*") \
        .eq("user_id", user_id) \
        .order("created_at", desc=True) \
        .execute()

    return result.data
