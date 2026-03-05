import { apiGet, apiPost } from "@/api/client";

export const getEvents = (status?: string, token?: string | null) =>
  apiGet(`/events${status ? `?status=${encodeURIComponent(status)}` : ""}`, token);

export const createEvent = (payload: unknown, token?: string | null) => apiPost("/events", payload, token);
export const approveEvent = (eventId: string, approved: boolean, token?: string | null) =>
  apiPost(`/events/${eventId}/approval`, { approved }, token);
export const joinEvent = (eventId: string, token?: string | null) => apiPost(`/events/${eventId}/join`, {}, token);
export const completeEvent = (eventId: string, outputSummary: string, token?: string | null) =>
  apiPost(`/events/${eventId}/complete`, { outputSummary }, token);
