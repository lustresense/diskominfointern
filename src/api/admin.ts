import { apiGet, apiPost } from "@/api/client";

export const getAdjustments = (token?: string | null) => apiGet("/admin/temporary-adjustments", token);
export const assignRole = (payload: unknown, token?: string | null) => apiPost("/admin/assign-role", payload, token);
export const removeRole = (payload: unknown, token?: string | null) => apiPost("/admin/remove-role", payload, token);
export const addPoints = (payload: unknown, token?: string | null) =>
  apiPost("/admin/add-temporary-points", payload, token);
export const addBadge = (payload: unknown, token?: string | null) => apiPost("/admin/add-temporary-badge", payload, token);
