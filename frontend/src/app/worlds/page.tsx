"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { LogOut, Map } from "lucide-react";
import { useAuth } from "@/lib/auth";
import { api } from "@/lib/api";
import { World, ProgressSummary } from "@/lib/types";
import { WorldCard } from "@/components/WorldMap";
import { XPBar } from "@/components/XPBar";
import { BadgeGrid } from "@/components/Badge";

export default function WorldsPage() {
  const { user, logout } = useAuth();
  const router = useRouter();
  const [worlds, setWorlds] = useState<World[]>([]);
  const [progress, setProgress] = useState<ProgressSummary | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!user) {
      router.push("/");
      return;
    }
    Promise.all([api.lessons.getWorlds(), api.progress.getSummary()])
      .then(([w, p]) => {
        setWorlds(w);
        setProgress(p);
      })
      .finally(() => setLoading(false));
  }, [user, router]);

  function getWorldProgress(worldNumber: number) {
    if (!progress) return { completed: 0, total: 0 };
    const wp = progress.worlds_progress.find((w) => w.world_number === worldNumber);
    return { completed: wp?.completed ?? 0, total: wp?.total ?? 0 };
  }

  if (!user) return null;

  return (
    <div className="min-h-screen">
      {/* Header */}
      <header className="sticky top-0 z-50 bg-slate-900/90 backdrop-blur border-b border-slate-700/50">
        <div className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 bg-indigo-500/20 rounded-xl flex items-center justify-center border border-indigo-500/30">
              <Map className="w-5 h-5 text-indigo-400" />
            </div>
            <span className="font-black text-xl text-white">C<span className="text-indigo-400">Quest</span></span>
          </div>
          <div className="flex items-center gap-4">
            {user && <XPBar xp={user.xp} username={user.username} />}
            <button
              onClick={() => { logout(); router.push("/"); }}
              className="flex items-center gap-1.5 text-slate-400 hover:text-white transition-colors text-sm"
            >
              <LogOut className="w-4 h-4" />
              <span className="hidden sm:block">Logout</span>
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-8">
        {/* Welcome */}
        <div className="mb-8 animate-slide-up">
          <h2 className="text-3xl font-black text-white">
            Welcome back, <span className="text-indigo-400">{user.username}</span>! 👋
          </h2>
          <p className="text-slate-400 mt-1">
            {progress
              ? `${progress.completed_lessons} of ${progress.total_lessons} lessons completed`
              : "Continue your coding adventure!"}
          </p>
        </div>

        {/* Overall progress bar */}
        {progress && (
          <div className="card p-4 mb-8 animate-slide-up">
            <div className="flex items-center justify-between mb-2">
              <span className="text-slate-300 font-bold">Overall Progress</span>
              <span className="text-indigo-400 font-bold">
                {Math.round((progress.completed_lessons / Math.max(progress.total_lessons, 1)) * 100)}%
              </span>
            </div>
            <div className="w-full bg-slate-700 rounded-full h-3">
              <div
                className="bg-gradient-to-r from-indigo-500 to-purple-500 h-3 rounded-full transition-all duration-700"
                style={{
                  width: `${(progress.completed_lessons / Math.max(progress.total_lessons, 1)) * 100}%`,
                }}
              />
            </div>
          </div>
        )}

        {loading ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="card p-5 h-52 animate-pulse" />
            ))}
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 animate-slide-up">
            {worlds.map((world) => {
              const { completed, total } = getWorldProgress(world.number);
              const wp = progress?.worlds_progress.find((w) => w.world_number === world.number);
              const unlocked = wp?.unlocked ?? world.number === 1;
              return (
                <WorldCard
                  key={world.id}
                  world={world}
                  unlocked={unlocked}
                  completedLessons={completed}
                  totalLessons={total}
                />
              );
            })}
          </div>
        )}

        {/* Badges */}
        {progress && progress.badges.length > 0 && (
          <div className="card p-5 mt-8 animate-slide-up">
            <h3 className="text-lg font-bold text-white mb-4">🏅 Your Badges</h3>
            <BadgeGrid earnedBadgeIds={progress.badges.map((b) => b.badge_id)} />
          </div>
        )}
      </main>
    </div>
  );
}
