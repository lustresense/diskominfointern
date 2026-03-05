export type CollabSupportType = "dana" | "konsumsi" | "peralatan" | "media_partner" | "lainnya";
export type CollabScope = "kota" | "kecamatan" | "kelurahan";
export type CollabStatus = "pending" | "approved" | "rejected";

export interface CollabRequest {
  id: string;
  organizationName: string;
  picName: string;
  email: string;
  supportType: CollabSupportType;
  contributionScope: CollabScope;
  scopeKecamatanId: number | null;
  scopeKelurahanId: number | null;
  scopeKecamatanName: string | null;
  scopeKelurahanName: string | null;
  supportDescription: string;
  status: CollabStatus;
  reviewedByName: string | null;
  reviewedAt: string | null;
  createdAt: string;
}
