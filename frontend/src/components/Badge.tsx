"use client";

const BADGE_INFO: Record<string, { name: string; icon: string; color: string }> = {
  world1: { name: "Hello Hero", icon: "🌟", color: "#6366f1" },
  world2: { name: "Variable Voyager", icon: "🔢", color: "#8b5cf6" },
  world3: { name: "Decision Maker", icon: "🔀", color: "#ec4899" },
  world4: { name: "Loop Legend", icon: "🔄", color: "#f59e0b" },
  world5: { name: "Function Fighter", icon: "⚡", color: "#10b981" },
  world6: { name: "C Master", icon: "🏆", color: "#ef4444" },
};

interface BadgeProps {
  badgeId: string;
  size?: "sm" | "md" | "lg";
}

export function Badge({ badgeId, size = "md" }: BadgeProps) {
  const info = BADGE_INFO[badgeId];
  if (!info) return null;

  const sizes = {
    sm: "w-10 h-10 text-xl",
    md: "w-14 h-14 text-2xl",
    lg: "w-20 h-20 text-4xl",
  };

  return (
    <div className="flex flex-col items-center gap-1 animate-pop">
      <div
        className={`${sizes[size]} rounded-full flex items-center justify-center shadow-lg`}
        style={{ backgroundColor: `${info.color}33`, border: `2px solid ${info.color}` }}
      >
        <span>{info.icon}</span>
      </div>
      {size !== "sm" && (
        <span className="text-xs text-slate-400 text-center">{info.name}</span>
      )}
    </div>
  );
}

export function BadgeGrid({ earnedBadgeIds }: { earnedBadgeIds: string[] }) {
  return (
    <div className="flex flex-wrap gap-3">
      {Object.keys(BADGE_INFO).map((id) => {
        const earned = earnedBadgeIds.includes(id);
        const info = BADGE_INFO[id];
        return (
          <div key={id} className="flex flex-col items-center gap-1">
            <div
              className={`w-14 h-14 rounded-full flex items-center justify-center shadow-lg transition-all ${
                earned ? "opacity-100" : "opacity-20 grayscale"
              }`}
              style={{ backgroundColor: `${info.color}33`, border: `2px solid ${info.color}` }}
            >
              <span className="text-2xl">{info.icon}</span>
            </div>
            <span className="text-xs text-slate-400 text-center">{info.name}</span>
          </div>
        );
      })}
    </div>
  );
}
