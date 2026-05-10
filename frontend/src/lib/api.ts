import { AuthToken, World, Lesson, CodeRunResult, ProgressSummary, UserProgress, Exercise } from "./types";

const BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

function getToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("cquest_token");
}

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const token = getToken();
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(options.headers as Record<string, string>),
  };
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const res = await fetch(`${BASE_URL}${path}`, { ...options, headers });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: "Request failed" }));
    throw new Error(err.detail || "Request failed");
  }
  return res.json();
}

export const api = {
  auth: {
    register: (username: string, email: string, password: string) =>
      request<AuthToken>("/auth/register", {
        method: "POST",
        body: JSON.stringify({ username, email, password }),
      }),
    login: (username: string, password: string) =>
      request<AuthToken>("/auth/login", {
        method: "POST",
        body: JSON.stringify({ username, password }),
      }),
  },

  lessons: {
    getWorlds: () => request<World[]>("/lessons/worlds"),
    getWorld: (number: number) => request<World>(`/lessons/worlds/${number}`),
    getLesson: (id: number) => request<Lesson>(`/lessons/${id}`),
  },

  code: {
    run: (code: string, opts: { lesson_id?: number; exercise_id?: number }) =>
      request<CodeRunResult>("/code/run", {
        method: "POST",
        body: JSON.stringify({ code, ...opts }),
      }),
  },

  progress: {
    getSummary: () => request<ProgressSummary>("/progress/summary"),
    complete: (lesson_id: number) =>
      request<UserProgress>(`/progress/complete/${lesson_id}`, { method: "POST" }),
  },

  ai: {
    getHint: (lesson_id: number, code: string, error_message?: string) =>
      request<{ hint: string }>("/ai/hint", {
        method: "POST",
        body: JSON.stringify({ lesson_id, code, error_message }),
      }),
    explainError: (error_message: string, code: string) =>
      request<{ explanation: string }>("/ai/explain-error", {
        method: "POST",
        body: JSON.stringify({ error_message, code }),
      }),
    generateExercise: (world_number: number, topic: string) =>
      request<{ title: string; description: string; starter_code: string; expected_output: string; hint: string }>(
        "/ai/generate-exercise",
        {
          method: "POST",
          body: JSON.stringify({ world_number, topic }),
        }
      ),
  },
};
