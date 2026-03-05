export const API_PREFIX = "/make-server-32aa5c5c";

export const ROLE_CODES = {
  USER: "user",
  KSH: "ksh",
  MODERATOR_T1: "moderator_t1",
  MODERATOR_T2: "moderator_t2",
  MODERATOR_T3: "moderator_t3",
  ADMIN: "admin",
} as const;

export const PILLAR_LABELS: Record<number, string> = {
  1: "Lingkungan",
  2: "Ekonomi",
  3: "Sosial Budaya",
  4: "Kemasyarakatan",
};

export const STATUS_LABELS: Record<string, string> = {
  draft: "Draft",
  approved: "Approved",
  published: "Published",
  completed: "Completed",
  pending: "Pending",
  verified: "Verified",
  rejected: "Rejected",
};
