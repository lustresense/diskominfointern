from pydantic import BaseModel, ConfigDict


class CollabCreateRequest(BaseModel):
  model_config = ConfigDict(extra="ignore")

  organizationName: str
  picName: str
  email: str
  supportType: str
  contributionScope: str = "kota"
  kecamatanId: int | None = None
  kelurahanId: int | None = None
  supportDescription: str


class CollabApprovalRequest(BaseModel):
  model_config = ConfigDict(extra="ignore")

  approved: bool = False


class CollabResponse(BaseModel):
  id: str
  organizationName: str
  picName: str
  email: str
  supportType: str
  contributionScope: str
  scopeKecamatanId: int | None = None
  scopeKelurahanId: int | None = None
  scopeKecamatanName: str | None = None
  scopeKelurahanName: str | None = None
  supportDescription: str
  status: str
  reviewedByName: str | None = None
  reviewedAt: str | None = None
  createdAt: str
