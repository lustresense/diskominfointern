from pydantic import BaseModel, ConfigDict, Field


class AssignRoleRequest(BaseModel):
  model_config = ConfigDict(extra="ignore")

  userId: str
  tier2Badge: str = "lurah"


class RemoveRoleRequest(BaseModel):
  model_config = ConfigDict(extra="ignore")

  userId: str


class TempPointsRequest(BaseModel):
  model_config = ConfigDict(extra="ignore")

  userId: str
  points: int = Field(ge=-500, le=500)
  reason: str


class TempBadgeRequest(BaseModel):
  model_config = ConfigDict(extra="ignore")

  userId: str
  badgeId: str
  reason: str
