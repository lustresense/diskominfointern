from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class ReportCreateRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    eventId: str = ""
    participants: int = 1
    outcomeTags: List[str] = Field(default_factory=list)
    photoUrl: str = ""


class ReportVerifyRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    approved: bool = False


class ReportResponse(BaseModel):
    id: str
    eventId: str
    userId: str
    participants: int
    outcomeTags: List[str]
    photoUrl: Optional[str]
    status: str
    points: int
    createdAt: str
