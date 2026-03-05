from pydantic import BaseModel, ConfigDict, Field


class SignupRequest(BaseModel):
  model_config = ConfigDict(extra="ignore")

  email: str
  password: str
  name: str
  nik: str | None = ""
  rw: str | None = ""
  kelurahan: str


class LoginRequest(BaseModel):
  model_config = ConfigDict(extra="ignore")

  email: str
  password: str


class AdminLoginRequest(BaseModel):
  model_config = ConfigDict(extra="ignore")

  username: str
  password: str


class UserResponse(BaseModel):
  id: str
  name: str
  email: str
  role: str
  roleCode: str
  isKsh: bool
  moderatorTier: int | None = None
  tier2Badge: str | None = None
  kelurahan: str | None = None
  kecamatan: str | None = None
  kampungId: int | None = None
  kampung: dict | None = None
  points: int = Field(default=0)
  badges: list = Field(default_factory=list)
  hasPendingReport: bool = False
