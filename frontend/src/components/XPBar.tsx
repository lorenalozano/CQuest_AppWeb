"use client";
import { Star } from "lucide-react";

const XP_PER_LEVEL = 500;

interface XPBarProps {
  xp: number;
  username: string;
}

export function XPBar({ xp, username }: XPBarProps) {
  const level = Math.floor(xp / XP_PER_LEVEL) + 1;
  const xpInLevel = xp % XP_PER_LEVEL;
  const pct = Math.min((xpInLevel / XP_PER_LEVEL) * 100, 100);

  return (
    <div className="flex items-center gap-3">
      <div className="flex items-center gap-1.5 bg-amber-500/20 rounded-full px-3 py-1.5">
        <Star className="w-4 h-4 text-amber-400 fill-amber-400" />
        <span className="text-amber-300 font-bold text-sm">{xp} XP</span>
      </div>
      <div className="hidden sm:flex items-center gap-2">
        <span className="text-slate-400 text-sm">Lv.{level}</span>
        <div className="w-24 bg-slate-700 rounded-full h-2">
          <div
            className="bg-gradient-to-r from-indigo-500 to-purple-500 h-2 rounded-full transition-all duration-500"
            style={{ width: `${pct}%` }}
          />
        </div>
      </div>
      <span className="text-slate-300 font-semibold text-sm hidden sm:block">{username}</span>
    </div>
  );
}
