import { apiGet, apiPut } from "@/api/client";

export const getUsers = (params: { role?: string; kampungId?: string | number } = {}, token?: string | null) => {
  const qs = new URLSearchParams();
  if (params.role) qs.set("role", params.role);
  if (params.kampungId !== undefined) qs.set("kampungId", String(params.kampungId));
  const suffix = qs.toString() ? `?${qs.toString()}` : "";
  return apiGet(`/users${suffix}`, token);
};

export const updateUser = (userId: string, payload: unknown, token?: string | null) =>
  apiPut(`/users/${userId}`, payload, token);
