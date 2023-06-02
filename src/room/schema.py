from pydantic import BaseModel, Field


class UpdatePosition(BaseModel):
    x: int = Field(..., ge=0, le=8)
    y: int = Field(..., ge=0, le=8)
    orientation: str = Field(..., regex='(top|right|bottom|left)')


class ToggleMute(BaseModel):
    user_id: str
    link: str
    muted: bool
