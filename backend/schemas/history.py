from pydantic import BaseModel
from typing import List
from datetime import datetime

class HistoryRecord(BaseModel):
    user_id: str
    data: List[float]
    alpha: float
    created_at: datetime
