"use client";
import { useState } from "react";
import { Bot, Lightbulb, AlertCircle, Sparkles, X } from "lucide-react";
import { api } from "@/lib/api";

interface AITutorProps {
  lessonId: number;
  code: string;
  errorMessage?: string;
  onClose: () => void;
}

type Mode = "hint" | "error" | "idle";

export function AITutor({ lessonId, code, errorMessage, onClose }: AITutorProps) {
  const [mode, setMode] = useState<Mode>("idle");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  async function fetchHint() {
    setLoading(true);
    setMode("hint");
    try {
      const res = await api.ai.getHint(lessonId, code, errorMessage);
      setMessage(res.hint);
    } catch {
      setMessage("Oops! The AI tutor is taking a break. Try again soon!");
    } finally {
      setLoading(false);
    }
  }

  async function fetchErrorExplanation() {
    if (!errorMessage) return;
    setLoading(true);
    setMode("error");
    try {
      const res = await api.ai.explainError(errorMessage, code);
      setMessage(res.explanation);
    } catch {
      setMessage("Oops! The AI tutor is taking a break. Try again soon!");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="card p-4 border-indigo-500/30 animate-slide-up">
      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 bg-indigo-500/20 rounded-full flex items-center justify-center">
            <Bot className="w-5 h-5 text-indigo-400" />
          </div>
          <span className="font-bold text-indigo-300">AI Tutor</span>
          <Sparkles className="w-4 h-4 text-yellow-400 animate-pulse" />
        </div>
        <button onClick={onClose} className="text-slate-500 hover:text-slate-300 transition-colors">
          <X className="w-5 h-5" />
        </button>
      </div>

      <div className="flex gap-2 mb-3">
        <button
          onClick={fetchHint}
          disabled={loading}
          className="flex items-center gap-1.5 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 rounded-xl px-3 py-2 text-sm font-semibold transition-all disabled:opacity-50"
        >
          <Lightbulb className="w-4 h-4" />
          Get a Hint
        </button>
        {errorMessage && (
          <button
            onClick={fetchErrorExplanation}
            disabled={loading}
            className="flex items-center gap-1.5 bg-red-500/20 hover:bg-red-500/30 text-red-300 rounded-xl px-3 py-2 text-sm font-semibold transition-all disabled:opacity-50"
          >
            <AlertCircle className="w-4 h-4" />
            Explain Error
          </button>
        )}
      </div>

      {loading && (
        <div className="flex items-center gap-2 text-slate-400 text-sm py-2">
          <div className="w-4 h-4 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin" />
          Thinking...
        </div>
      )}

      {!loading && message && (
        <div
          className={`rounded-xl p-3 text-sm leading-relaxed ${
            mode === "error"
              ? "bg-red-500/10 text-red-200 border border-red-500/20"
              : "bg-indigo-500/10 text-indigo-100 border border-indigo-500/20"
          }`}
        >
          <div className="flex gap-2">
            {mode === "error" ? (
              <AlertCircle className="w-4 h-4 text-red-400 mt-0.5 shrink-0" />
            ) : (
              <Lightbulb className="w-4 h-4 text-amber-400 mt-0.5 shrink-0" />
            )}
            <p>{message}</p>
          </div>
        </div>
      )}

      {!loading && !message && (
        <p className="text-slate-400 text-sm">
          Stuck? I&apos;m here to help! Click a button above for a hint or error explanation. 🤖
        </p>
      )}
    </div>
  );
}
