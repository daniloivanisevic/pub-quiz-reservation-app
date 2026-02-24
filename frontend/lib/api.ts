const DEFAULT_LOCAL_API = "http://127.0.0.1:8000";

export function apiUrl(path: string) {
  const base = process.env.NEXT_PUBLIC_API_BASE_URL || DEFAULT_LOCAL_API;
  const cleanBase = base.replace(/\/+$/, "");
  const cleanPath = path.startsWith("/") ? path : `/${path}`;
  return `${cleanBase}${cleanPath}`;
}