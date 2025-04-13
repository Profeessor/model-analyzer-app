import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_user_data(user_id):
    """Retrieve user data from Supabase"""
    response = supabase.table("user_data").select("*").eq("user_id", user_id).execute()
    return response.data

def save_analysis_result(user_id, result):
    """Save analysis results to Supabase"""
    return supabase.table("analysis_results").insert(
        {"user_id": user_id, "result": result}
    ).execute() 