import { apiGet, apiPost, apiPublicPost } from "@/api/client";

export const getCollabRequests = (status?: string, token?: string | null) =>
  apiGet(`/collaboration-requests${status ? `?status=${encodeURIComponent(status)}` : ""}`, token);

export const createCollab = (payload: unknown) => apiPublicPost("/collaboration-requests", payload);
export const approveCollab = (requestId: string, approved: boolean, token?: string | null) =>
  apiPost(`/collaboration-requests/${requestId}/approval`, { approved }, token);
