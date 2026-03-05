import { apiGet, apiPost } from "@/api/client";

export const getReports = (params: { status?: string; userId?: string } = {}, token?: string | null) => {
  const qs = new URLSearchParams();
  if (params.status) qs.set("status", params.status);
  if (params.userId) qs.set("userId", params.userId);
  const suffix = qs.toString() ? `?${qs.toString()}` : "";
  return apiGet(`/reports${suffix}`, token);
};

export const createReport = (payload: unknown, token?: string | null) => apiPost("/reports", payload, token);
export const verifyReport = (reportId: string, approved: boolean, token?: string | null) =>
  apiPost(`/reports/${reportId}/verify`, { approved }, token);
