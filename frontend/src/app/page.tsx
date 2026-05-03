"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth";
import { Code2, Star, Zap, Trophy } from "lucide-react";

export default function HomePage() {
  const { user, login, register } = useAuth();
  const router = useRouter();
  const [mode, setMode] = useState<"login" | "register">("login");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (user) router.push("/worlds");
  }, [user, router]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      if (mode === "login") {
        await login(username, password);
      } else {
        await register(username, email, password);
      }
      router.push("/worlds");
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#0f0f1a] via-[#13132b] to-[#0f0f1a] flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-md animate-slide-up">
        {/* Hero */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-20 h-20 bg-indigo-500/20 rounded-3xl mb-4 border-2 border-indigo-500/40 shadow-xl shadow-indigo-500/20">
            <Code2 className="w-10 h-10 text-indigo-400" />
          </div>
          <h1 className="text-5xl font-black text-white mb-2">
            C<span className="text-indigo-400">Quest</span>
          </h1>
          <p className="text-slate-400 text-lg">Learn C programming like a hero! 🦸</p>
        </div>

        {/* Feature pills */}
        <div className="flex justify-center gap-3 flex-wrap mb-8">
          {[
            { icon: Star, text: "XP & Levels", color: "text-amber-400" },
            { icon: Zap, text: "AI Tutor", color: "text-indigo-400" },
            { icon: Trophy, text: "Badges", color: "text-green-400" },
          ].map(({ icon: Icon, text, color }) => (
            <div key={text} className="flex items-center gap-1.5 bg-slate-800/60 rounded-full px-3 py-1.5 border border-slate-700/50">
              <Icon className={`w-4 h-4 ${color}`} />
              <span className="text-slate-300 text-sm font-semibold">{text}</span>
            </div>
          ))}
        </div>

        {/* Auth card */}
        <div className="card p-6 shadow-2xl">
          {/* Tabs */}
          <div className="flex bg-slate-900 rounded-xl p-1 mb-6">
            {(["login", "register"] as const).map((m) => (
              <button
                key={m}
                onClick={() => { setMode(m); setError(""); }}
                className={`flex-1 py-2.5 rounded-lg font-bold text-sm transition-all ${
                  mode === m
                    ? "bg-indigo-500 text-white shadow-lg"
                    : "text-slate-400 hover:text-white"
                }`}
              >
                {m === "login" ? "Sign In" : "Join Now"}
              </button>
            ))}
          </div>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-slate-300 text-sm font-bold mb-1.5">Username</label>
              <input
                className="input-field"
                placeholder="CoolCoder123"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
                autoComplete="username"
              />
            </div>

            {mode === "register" && (
              <div>
                <label className="block text-slate-300 text-sm font-bold mb-1.5">Email</label>
                <input
                  type="email"
                  className="input-field"
                  placeholder="you@example.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  autoComplete="email"
                />
              </div>
            )}

            <div>
              <label className="block text-slate-300 text-sm font-bold mb-1.5">Password</label>
              <input
                type="password"
                className="input-field"
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                autoComplete={mode === "login" ? "current-password" : "new-password"}
              />
            </div>

            {error && (
              <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-3 text-red-300 text-sm">
                {error}
              </div>
            )}

            <button
              type="submit"
              disabled={loading}
              className="btn-primary w-full flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? (
                <>
                  <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                  Loading...
                </>
              ) : mode === "login" ? (
                "🚀 Let's Go!"
              ) : (
                "⚔️ Start Adventure!"
              )}
            </button>
          </form>
        </div>

        <p className="text-center text-slate-500 text-sm mt-4">
          Free to learn · No credit card needed 🎮
        </p>
      </div>
    </div>
  );
}
