export type EventScopeType = "kelurahan" | "kecamatan";
export type EventStatus = "draft" | "approved" | "published" | "completed";

export interface Event {
  id: string;
  title: string;
  description: string;
  pillar: number;
  date: string;
  time: string | null;
  location: string | null;
  quota: number;
  scopeType: EventScopeType;
  status: EventStatus;
  kelurahan: string | null;
  kecamatan: string | null;
  participants: string[];
}
