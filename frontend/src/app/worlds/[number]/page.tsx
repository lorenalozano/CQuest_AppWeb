"use client";
import { useEffect, useState } from "react";
import { useRouter, useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft, CheckCircle, Lock, Star, ChevronRight, Trophy } from "lucide-react";
import { useAuth } from "@/lib/auth";
import { api } from "@/lib/api";
import { World, ProgressSummary } from "@/lib/types";
import { XPBar } from "@/components/XPBar";

export default function WorldDetailPage() {
  const { user } = useAuth();
  const router = useRouter();
  const params = useParams();
  const worldNumber = Number(params.number);

  const [world, setWorld] = useState<World | null>(null);
  const [progress, setProgress] = useState<ProgressSummary | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!user) { router.push("/"); return; }
    if (user.current_world < worldNumber) { router.push("/worlds"); return; }

    Promise.all([
      api.lessons.getWorld(worldNumber),
      api.progress.getSummary(),
    ])
      .then(([w, p]) => { setWorld(w); setProgress(p); })
      .finally(() => setLoading(false));
  }, [user, worldNumber, router]);

  if (!user || loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="w-10 h-10 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (!world) return null;

  const worldProgressData = progress?.worlds_progress.find(
    (wp) => wp.world_number === worldNumber
  );
  const completedCount = worldProgressData?.completed ?? 0;
  const totalCount = world.lessons.length;

  const sortedLessons = [...world.lessons].sort((a, b) => a.order - b.order);

  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-50 bg-slate-900/90 backdrop-blur border-b border-slate-700/50">
        <div className="max-w-3xl mx-auto px-4 py-3 flex items-center justify-between">
          <Link href="/worlds" className="flex items-center gap-2 text-slate-400 hover:text-white transition-colors">
            <ArrowLeft className="w-5 h-5" />
            <span className="font-semibold">World Map</span>
          </Link>
          {user && <XPBar xp={user.xp} username={user.username} />}
        </div>
      </header>

      <main className="max-w-3xl mx-auto px-4 py-8">
        {/* World header */}
        <div
          className="card p-6 mb-6 animate-slide-up"
          style={{ borderColor: `${world.color}40` }}
        >
          <div className="flex items-center gap-4">
            <div
              className="w-16 h-16 rounded-2xl flex items-center justify-center text-4xl shadow-lg"
              style={{ backgroundColor: `${world.color}25`, border: `2px solid ${world.color}50` }}
            >
              {world.icon}
            </div>
            <div className="flex-1">
              <p className="text-sm font-bold uppercase tracking-wider" style={{ color: world.color }}>
                World {world.number}
              </p>
              <h1 className="text-2xl font-black text-white">{world.title}</h1>
              <p className="text-slate-400 text-sm mt-0.5">{world.description}</p>
              <div className="mt-2">
                <div className="flex justify-between text-xs text-slate-400 mb-1">
                  <span>{completedCount}/{totalCount} lessons</span>
                  <span>{totalCount > 0 ? Math.round((completedCount / totalCount) * 100) : 0}%</span>
                </div>
                <div className="w-full bg-slate-700 rounded-full h-2">
                  <div
                    className="h-2 rounded-full transition-all duration-500"
                    style={{
                      width: `${totalCount > 0 ? (completedCount / totalCount) * 100 : 0}%`,
                      backgroundColor: world.color,
                    }}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Lessons */}
        <div className="space-y-3 animate-slide-up">
          {sortedLessons.map((lesson, idx) => {
            const prevCompleted = idx === 0 || true;
            const locked = !prevCompleted;
            return (
              <div key={lesson.id}>
                {lesson.is_final_project && idx > 0 && (
                  <div className="flex items-center gap-3 my-4">
                    <div className="flex-1 h-px bg-slate-700" />
                    <span className="text-xs text-slate-500 font-bold uppercase tracking-wider flex items-center gap-1">
                      <Trophy className="w-3 h-3" /> Final Challenge
                    </span>
                    <div className="flex-1 h-px bg-slate-700" />
                  </div>
                )}
                <Link href={locked ? "#" : `/lesson/${lesson.id}`} className={locked ? "pointer-events-none" : "block"}>
                  <div
                    className={`card p-4 flex items-center gap-4 transition-all duration-200 ${
                      !locked
                        ? "hover:border-indigo-500/40 hover:-translate-y-0.5 hover:shadow-lg cursor-pointer"
                        : "opacity-50 cursor-not-allowed"
                    } ${lesson.is_final_project ? "border-amber-500/30" : ""}`}
                  >
                    <div
                      className={`w-10 h-10 rounded-xl flex items-center justify-center font-black text-lg shrink-0 ${
                        locked
                          ? "bg-slate-700 text-slate-500"
                          : lesson.is_final_project
                          ? "bg-amber-500/20 text-amber-400"
                          : "bg-slate-700 text-slate-300"
                      }`}
                    >
                      {locked ? <Lock className="w-4 h-4" /> : idx + 1}
                    </div>

                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2">
                        <h3 className="font-bold text-white">{lesson.title}</h3>
                        {lesson.is_final_project && (
                          <span className="text-xs bg-amber-500/20 text-amber-300 rounded-full px-2 py-0.5 font-bold">
                            Boss
                          </span>
                        )}
                      </div>
                      <p className="text-slate-400 text-sm mt-0.5 truncate">{lesson.description}</p>
                    </div>

                    <div className="flex items-center gap-2 shrink-0">
                      <div className="flex items-center gap-1 text-amber-400">
                        <Star className="w-3.5 h-3.5 fill-amber-400" />
                        <span className="text-xs font-bold">{lesson.xp_reward}</span>
                      </div>
                      {!locked && <ChevronRight className="w-4 h-4 text-slate-500" />}
                    </div>
                  </div>
                </Link>
              </div>
            );
          })}
        </div>
      </main>
    </div>
  );
}
