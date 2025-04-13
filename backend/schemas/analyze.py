from pydantic import BaseModel
from typing import List

class AnalysisRequest(BaseModel):
    user_id: str
    data: List[float]
