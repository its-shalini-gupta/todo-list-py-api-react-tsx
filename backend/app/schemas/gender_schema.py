from pydantic import BaseModel, Field
from typing import Optional

class GenterCreate(BaseModel):
    code: str = Field(..., min_length=1, max_length=15, description="Gender code must not be empty and should be between 1 and 15 characters.")
    desc: Optional[str] = Field(..., max_length=30)


