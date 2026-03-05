const API_BASE = (
  import.meta.env.VITE_API_BASE_URL ||
  "http://127.0.0.1:8000/make-server-32aa5c5c"
).replace(/\/+$/, "");

let onUnauthorized: (() => void) | null = null;

export interface ApiError {
  status: number;
  message: string;
}

export function setOnUnauthorized(handler: () => void): void {
  onUnauthorized = handler;
}

function resolveToken(explicitToken?: string | null): string | null {
  if (explicitToken !== undefined) {
    return explicitToken;
  }
  return localStorage.getItem("simrp_auth_token");
}

function extractErrorMessage(data: any, status: number): string {
  if (typeof data?.error === "string" && data.error) {
    return data.error;
  }
  if (typeof data?.detail === "string" && data.detail) {
    return data.detail;
  }
  return `Request gagal (${status})`;
}

function handleUnauthorized(): void {
  if (onUnauthorized) {
    onUnauthorized();
    return;
  }
  if (window.location.pathname !== "/login") {
    window.history.pushState({}, "", "/login");
    window.dispatchEvent(new PopStateEvent("popstate"));
  }
}

export async function apiRequest<T = any>(
  path: string,
  options: {
    method?: string;
    body?: unknown;
    token?: string | null;
    anonymous?: boolean;
  } = {},
): Promise<T> {
  const { method = "GET", body, token, anonymous = false } = options;

  const headers: Record<string, string> = {};
  if (body !== undefined) {
    headers["Content-Type"] = "application/json";
  }

  const authToken = resolveToken(token);
  if (!anonymous && authToken) {
    headers["Authorization"] = `Bearer ${authToken}`;
  }

  let response: Response;
  try {
    response = await fetch(`${API_BASE}${path}`, {
      method,
      headers,
      body: body !== undefined ? JSON.stringify(body) : undefined,
    });
  } catch {
    throw { status: 0, message: "Tidak bisa terhubung ke server lokal API." } as ApiError;
  }

  const data = await response.json().catch(() => ({}));
  if (response.status === 401) {
    handleUnauthorized();
    throw { status: 401, message: extractErrorMessage(data, 401) } as ApiError;
  }
  if (!response.ok) {
    throw { status: response.status, message: extractErrorMessage(data, response.status) } as ApiError;
  }

  return data as T;
}

export function apiGet<T = any>(path: string, token?: string | null): Promise<T> {
  return apiRequest<T>(path, { method: "GET", token });
}

export function apiPost<T = any>(path: string, body: unknown, token?: string | null): Promise<T> {
  return apiRequest<T>(path, { method: "POST", body, token });
}

export function apiPut<T = any>(path: string, body: unknown, token?: string | null): Promise<T> {
  return apiRequest<T>(path, { method: "PUT", body, token });
}

export function apiPublicGet<T = any>(path: string): Promise<T> {
  return apiRequest<T>(path, { method: "GET", anonymous: true });
}

export function apiPublicPost<T = any>(path: string, body: unknown): Promise<T> {
  return apiRequest<T>(path, { method: "POST", body, anonymous: true });
}
