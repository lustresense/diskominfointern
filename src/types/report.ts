export type ReportStatus = "pending" | "verified" | "rejected";

export interface Report {
  id: string;
  eventId: string;
  userId: string;
  participants: number;
  outcomeTags: string[];
  photoUrl: string | null;
  status: ReportStatus;
  points: number;
  createdAt: string;
}
