export interface KampungInfo {
  id: number;
  name: string;
  kecamatan: string;
  xp: number;
  volunteers: number;
}

export interface UserBadge {
  id: string;
  temporary?: boolean;
}

export interface User {
  id: string;
  name: string;
  email: string;
  role: "user" | "moderator" | "admin";
  roleCode: string;
  isKsh: boolean;
  moderatorTier: number | null;
  tier2Badge: string | null;
  kelurahan: string | null;
  kecamatan: string | null;
  kampungId: number | null;
  kampung: KampungInfo | null;
  points: number;
  badges: UserBadge[];
  hasPendingReport?: boolean;
  developerNote?: string;
}
