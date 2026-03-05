from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class EventCreateRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    title: str = Field(default="", max_length=200)
    description: str = Field(default="", max_length=3000)
    pillar: int = Field(default=1)
    date: str = ""
    time: str = Field(default="", max_length=16)
    location: str = Field(default="", max_length=220)
    quota: int = 0
    scopeType: str = "kelurahan"
    kecamatanId: int | None = None
    kelurahanId: Optional[int] = None


class EventApprovalRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    approved: bool = False


class EventCompleteRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    outputSummary: str = ""


class EventResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    pillar: int
    date: str
    time: Optional[str]
    location: Optional[str]
    quota: int
    scopeType: str
    status: str
    kelurahan: Optional[str]
    kecamatan: Optional[str]
    participants: List[str]
