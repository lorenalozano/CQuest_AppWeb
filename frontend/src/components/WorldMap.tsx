"use client";
import Link from "next/link";
import { Lock, CheckCircle, Star, ChevronRight } from "lucide-react";
import { World } from "@/lib/types";

interface WorldCardProps {
  world: World;
  unlocked: boolean;
  completedLessons: number;
  totalLessons: number;
}

export function WorldCard({ world, unlocked, completedLessons, totalLessons }: WorldCardProps) {
  const allDone = completedLessons === totalLessons && totalLessons > 0;
  const pct = totalLessons > 0 ? Math.round((completedLessons / totalLessons) * 100) : 0;

  return (
    <div
      className={`card p-5 transition-all duration-300 ${
        unlocked
          ? "hover:-translate-y-1 hover:shadow-xl cursor-pointer"
          : "opacity-50 cursor-not-allowed"
      }`}
      style={unlocked ? { borderColor: `${world.color}40` } : {}}
    >
      <div className="flex items-start justify-between mb-3">
        <div
          className="w-14 h-14 rounded-2xl flex items-center justify-center text-3xl shadow-lg"
          style={{ backgroundColor: `${world.color}25`, border: `2px solid ${world.color}50` }}
        >
          {unlocked ? world.icon : <Lock className="w-6 h-6 text-slate-500" />}
        </div>
        {allDone && (
          <div className="flex items-center gap-1 text-green-400 bg-green-500/10 rounded-full px-2 py-1">
            <CheckCircle className="w-4 h-4" />
            <span className="text-xs font-bold">Done!</span>
          </div>
        )}
      </div>

      <div className="mb-1">
        <span className="text-xs font-bold uppercase tracking-wider" style={{ color: world.color }}>
          World {world.number}
        </span>
        <h3 className="text-lg font-bold text-white mt-0.5">{world.title}</h3>
        <p className="text-slate-400 text-sm mt-1">{world.description}</p>
      </div>

      <div className="mt-3">
        <div className="flex justify-between text-xs text-slate-400 mb-1">
          <span>{completedLessons}/{totalLessons} lessons</span>
          <span>{pct}%</span>
        </div>
        <div className="w-full bg-slate-700 rounded-full h-2">
          <div
            className="h-2 rounded-full transition-all duration-500"
            style={{ width: `${pct}%`, backgroundColor: world.color }}
          />
        </div>
      </div>

      {unlocked && (
        <Link href={`/worlds/${world.number}`} className="block mt-4">
          <div
            className="flex items-center justify-center gap-2 rounded-xl py-2.5 font-bold text-white text-sm transition-all hover:brightness-110"
            style={{ backgroundColor: world.color }}
          >
            {allDone ? (
              <>
                <Star className="w-4 h-4 fill-white" />
                Review
              </>
            ) : (
              <>
                {completedLessons > 0 ? "Continue" : "Start"}
                <ChevronRight className="w-4 h-4" />
              </>
            )}
          </div>
        </Link>
      )}
    </div>
  );
}
