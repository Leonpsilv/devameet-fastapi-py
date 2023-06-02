from typing import List
from pydantic import BaseModel, Field


class CreateMeet(BaseModel):
    name: str = Field(..., min_length=2)
    color: str = Field(..., regex="[0-9A-Fa-f]{6}")


class UpdateObjectMeet(BaseModel):
    id: int = None
    name: str
    x: int = Field(..., ge=0, le=7)
    y: int = Field(..., ge=0, le=7)
    zindex: int
    orientation: str = Field(..., regex='(back|right|front|left)')
    # orientation: str = Field(..., regex="(back|right|front|left)")


class UpdateMeet(BaseModel):
    name: str = Field(..., min_length=2)
    color: str = Field(..., regex="[0-9A-Fa-f]{6}")
    objects: List[UpdateObjectMeet] = []
