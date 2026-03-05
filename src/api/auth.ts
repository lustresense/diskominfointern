import { apiGet, apiPost } from "@/api/client";

export const signup = (payload: unknown) => apiPost("/auth/signup", payload);
export const login = (payload: unknown) => apiPost("/auth/login", payload);
export const adminLogin = (payload: unknown) => apiPost("/auth/admin-login", payload);
export const logout = (token?: string | null) => apiPost("/auth/logout", {}, token);
export const getMe = (token?: string | null) => apiGet("/auth/me", token);
