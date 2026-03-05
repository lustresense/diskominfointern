import { apiGet, apiPublicGet } from "@/api/client";

export const getGeoOptions = (token?: string | null) => apiGet("/geo/options", token);
export const getGeoStats = () => apiPublicGet("/geo/stats");
export const lookupKodepos = (code: string) => apiPublicGet(`/kodepos/${encodeURIComponent(code)}`);
export const getKampung = (token?: string | null) => apiGet("/kampung", token);
export const getLandingLeaderboard = () => apiPublicGet("/landing/leaderboard");
