
const DEFAULT_LOCAL_API = "http://127.0.0.1:8000";

export const API_BASE =
  process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, "") || DEFAULT_LOCAL_API;

export function apiUrl(path: string) {
  const p = path.startsWith("/") ? path : `/${path}`;
  return `${API_BASE}${p}`;
}