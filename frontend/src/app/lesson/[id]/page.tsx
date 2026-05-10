"use client";
import { useEffect, useState, useCallback } from "react";
import { useRouter, useParams } from "next/navigation";
import Link from "next/link";
import {
  ArrowLeft, Play, CheckCircle, XCircle, Bot, BookOpen,
  ChevronRight, ChevronLeft, Star, Trophy, RefreshCw, Terminal, Lock
} from "lucide-react";
import { useAuth } from "@/lib/auth";
import { api } from "@/lib/api";
import { Lesson, Exercise, CodeRunResult } from "@/lib/types";
import { CodeEditor } from "@/components/CodeEditor";
import { AITutor } from "@/components/AITutor";
import { XPBar } from "@/components/XPBar";

type Panel = "theory" | "output" | "ai";

function TheoryContent({ text }: { text: string }) {
  const lines = text.split("\n");
  const elements: React.ReactNode[] = [];
  let codeBuffer: string[] = [];

  const flushCode = (key: string) => {
    if (codeBuffer.length === 0) return;
    elements.push(
      <div key={key} className="overflow-x-auto my-2">
        <pre className="bg-slate-950 rounded-lg px-4 py-3 text-green-300 text-lg font-mono leading-relaxed border border-slate-700/40 whitespace-pre min-w-0">
          {codeBuffer.join("\n")}
        </pre>
      </div>
    );
    codeBuffer = [];
  };

  lines.forEach((line, i) => {
    const isIndented = line.startsWith("    ") || line.startsWith("\t");

    if (isIndented) {
      codeBuffer.push(line);
      return;
    }

    flushCode(`code-${i}`);

    if (/^━+$/.test(line.trim())) {
      elements.push(<hr key={i} className="border-slate-700/60 my-2" />);
    } else if (line === "") {
      elements.push(<div key={i} className="h-2" />);
    } else if (line.length > 0 && line.charCodeAt(0) > 127) {
      elements.push(
        <p key={i} className="font-black text-indigo-300 text-xl mt-4 mb-1">{line}</p>
      );
    } else if (line.startsWith("  ") && !isIndented) {
      elements.push(
        <p key={i} className="text-slate-400 text-lg font-mono pl-2">{line.trimStart()}</p>
      );
    } else {
      elements.push(
        <p key={i} className="text-slate-200 text-lg leading-relaxed">{line}</p>
      );
    }
  });

  flushCode("code-end");
  return <div className="space-y-1">{elements}</div>;
}

export default function LessonPage() {
  const { user, updateUser } = useAuth();
  const router = useRouter();
  const params = useParams();
  const lessonId = Number(params.id);

  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [worldNumber, setWorldNumber] = useState<number>(1);
  const [exerciseIndex, setExerciseIndex] = useState(0);
  const [code, setCode] = useState("");
  const [result, setResult] = useState<CodeRunResult | null>(null);
  const [running, setRunning] = useState(false);
  const [panel, setPanel] = useState<Panel>("theory");
  const [showSuccess, setShowSuccess] = useState(false);
  const [alreadyCompleted, setAlreadyCompleted] = useState(false);
  const [passedExercises, setPassedExercises] = useState<Set<number>>(new Set());

  useEffect(() => {
    if (!user) { router.push("/"); return; }
    api.lessons.getLesson(lessonId).then(async (l) => {
      setLesson(l);
      setExerciseIndex(0);
      setCode(l.exercises.length > 0 ? l.exercises[0].starter_code : l.starter_code);
      const worlds = await api.lessons.getWorlds();
      const w = worlds.find((ww) => ww.id === l.world_id);
      if (w) setWorldNumber(w.number);
    });
  }, [user, lessonId, router]);

  const currentExercise: Exercise | null = lesson?.exercises[exerciseIndex] ?? null;
  const hasExercises = (lesson?.exercises.length ?? 0) > 0;
  const totalExercises = lesson?.exercises.length ?? 0;

  const goToExercise = useCallback((idx: number) => {
    if (!lesson) return;
    setExerciseIndex(idx);
    setCode(lesson.exercises[idx].starter_code);
    setResult(null);
  }, [lesson]);

  const runCode = useCallback(async () => {
    if (!lesson || running) return;
    setRunning(true);
    setPanel("output");
    try {
      const opts = currentExercise
        ? { exercise_id: currentExercise.id }
        : { lesson_id: lessonId };
      const res = await api.code.run(code, opts);
      setResult(res);

      if (res.passed) {
        if (currentExercise) {
          const newPassed = new Set(passedExercises).add(exerciseIndex);
          setPassedExercises(newPassed);

          if (currentExercise.is_final && !alreadyCompleted) {
            const prog = await api.progress.complete(lessonId);
            if (prog.completed) {
              setAlreadyCompleted(true);
              setShowSuccess(true);
              const summary = await api.progress.getSummary();
              const newCurrentWorld = Math.max(...summary.worlds_progress.filter((w) => w.unlocked).map((w) => w.world_number));
              updateUser({ ...user!, xp: summary.xp, current_world: newCurrentWorld });
            }
          }
        } else if (!alreadyCompleted) {
          const prog = await api.progress.complete(lessonId);
          if (prog.completed) {
            setAlreadyCompleted(true);
            setShowSuccess(true);
            const summary = await api.progress.getSummary();
            const newCurrentWorld = Math.max(...summary.worlds_progress.filter((w) => w.unlocked).map((w) => w.world_number));
            updateUser({ ...user!, xp: summary.xp, current_world: newCurrentWorld });
          }
        }
      }
    } catch (err) {
      setResult({
        output: "",
        error: err instanceof Error ? err.message : "Run failed",
        success: false,
        passed: false,
        execution_time_ms: 0,
      });
    } finally {
      setRunning(false);
    }
  }, [lesson, running, code, lessonId, currentExercise, exerciseIndex, passedExercises, alreadyCompleted, user, updateUser]);

  useEffect(() => {
    function handleKey(e: KeyboardEvent) {
      if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
        e.preventDefault();
        runCode();
      }
    }
    window.addEventListener("keydown", handleKey);
    return () => window.removeEventListener("keydown", handleKey);
  }, [runCode]);

  if (!user || !lesson) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="w-10 h-10 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  const xpForThisStep = currentExercise ? currentExercise.xp_reward : lesson.xp_reward;

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="sticky top-0 z-50 bg-slate-900/95 backdrop-blur border-b border-slate-700/50">
        <div className="px-4 py-2.5 flex items-center justify-between gap-4">
          <div className="flex items-center gap-3 min-w-0">
            <Link
              href={`/worlds/${worldNumber}`}
              className="text-slate-400 hover:text-white transition-colors shrink-0"
            >
              <ArrowLeft className="w-5 h-5" />
            </Link>
            <div className="min-w-0">
              <h1 className="font-black text-white truncate">{lesson.title}</h1>
              <p className="text-xs text-slate-400 truncate hidden sm:block">{lesson.description}</p>
            </div>
          </div>
          <div className="flex items-center gap-3 shrink-0">
            <div className="flex items-center gap-1 text-amber-400">
              <Star className="w-4 h-4 fill-amber-400" />
              <span className="text-xs font-bold">{xpForThisStep} XP</span>
            </div>
            <XPBar xp={user.xp} username={user.username} />
          </div>
        </div>

        {/* Exercise progress bar */}
        {hasExercises && (
          <div className="px-4 pb-2 flex items-center gap-2">
            {lesson.exercises.map((ex, idx) => {
              const isPassed = passedExercises.has(idx);
              const isCurrent = idx === exerciseIndex;
              const isLocked = idx > 0 && !passedExercises.has(idx - 1) && !isPassed;
              return (
                <button
                  key={ex.id}
                  onClick={() => !isLocked && goToExercise(idx)}
                  disabled={isLocked}
                  title={isLocked ? "Complete the previous exercise first" : `Exercise ${idx + 1}`}
                  className={`flex items-center justify-center w-8 h-8 rounded-full text-xs font-black transition-all border-2 ${
                    isPassed
                      ? "bg-green-500 border-green-400 text-white"
                      : isCurrent
                      ? "bg-indigo-500 border-indigo-400 text-white"
                      : isLocked
                      ? "bg-slate-800 border-slate-700 text-slate-600 cursor-not-allowed"
                      : "bg-slate-700 border-slate-600 text-slate-300 hover:border-indigo-400"
                  }`}
                >
                  {isPassed ? <CheckCircle className="w-4 h-4" /> : isLocked ? <Lock className="w-3 h-3" /> : idx + 1}
                </button>
              );
            })}
            <span className="text-slate-500 text-xs ml-1">
              {passedExercises.size}/{totalExercises} done
            </span>
          </div>
        )}
      </header>

      {/* Main layout */}
      <div className="flex-1 flex flex-col lg:flex-row gap-0 overflow-hidden">
        {/* Left panel — code editor */}
        <div className="flex-1 flex flex-col p-4 gap-3 min-h-0">
          <CodeEditor
            value={code}
            onChange={setCode}
            height="calc(100vh - 310px)"
          />

          {/* Run button + navigation */}
          <div className="flex items-center gap-3">
            <button
              onClick={runCode}
              disabled={running}
              className="flex items-center gap-2 bg-green-500 hover:bg-green-400 active:bg-green-600 text-white font-black py-3 px-6 rounded-2xl transition-all shadow-lg hover:shadow-green-500/30 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed text-lg"
            >
              {running ? (
                <>
                  <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                  Running...
                </>
              ) : (
                <>
                  <Play className="w-5 h-5 fill-white" />
                  Run Code
                </>
              )}
            </button>
            <span className="text-slate-500 text-sm hidden sm:block">or Ctrl+Enter</span>

            {/* Next exercise button (shown when current is passed and not last) */}
            {hasExercises && passedExercises.has(exerciseIndex) && exerciseIndex < totalExercises - 1 && (
              <button
                onClick={() => goToExercise(exerciseIndex + 1)}
                className="flex items-center gap-1.5 bg-indigo-500 hover:bg-indigo-400 text-white font-black py-3 px-4 rounded-2xl transition-all text-sm ml-auto"
              >
                Next <ChevronRight className="w-4 h-4" />
              </button>
            )}

            <button
              onClick={() => setCode(currentExercise ? currentExercise.starter_code : lesson.starter_code)}
              className="flex items-center gap-1.5 text-slate-400 hover:text-white text-sm transition-colors ml-auto"
            >
              <RefreshCw className="w-4 h-4" />
              Reset
            </button>
          </div>
        </div>

        {/* Right panel */}
        <div className="lg:w-[500px] xl:w-[560px] flex flex-col border-t lg:border-t-0 lg:border-l border-slate-700/50">
          {/* Panel tabs */}
          <div className="flex border-b border-slate-700/50 bg-slate-900/50">
            {(["theory", "output", "ai"] as Panel[]).map((p) => {
              const icons = { theory: BookOpen, output: Terminal, ai: Bot };
              const labels = { theory: "Theory", output: "Output", ai: "AI Tutor" };
              const Icon = icons[p];
              return (
                <button
                  key={p}
                  onClick={() => setPanel(p)}
                  className={`flex-1 flex items-center justify-center gap-1.5 py-3 text-sm font-bold transition-all border-b-2 ${
                    panel === p
                      ? "text-indigo-400 border-indigo-400"
                      : "text-slate-500 border-transparent hover:text-slate-300"
                  }`}
                >
                  <Icon className="w-4 h-4" />
                  {labels[p]}
                  {p === "output" && result && (
                    <span className={`w-2 h-2 rounded-full ${result.passed ? "bg-green-400" : "bg-red-400"}`} />
                  )}
                </button>
              );
            })}
          </div>

          {/* Panel content */}
          <div className="flex-1 overflow-y-auto p-4">
            {panel === "theory" && (
              <div className="animate-slide-up">
                <h3 className="font-black text-white text-lg mb-3">📖 Theory</h3>
                <div className="bg-slate-900/60 rounded-xl p-4 border border-slate-700/50 mb-4">
                  <TheoryContent text={lesson.theory} />
                </div>

                {/* Current exercise task */}
                {currentExercise && (
                  <div className="bg-amber-500/10 border border-amber-500/30 rounded-xl p-3 mb-3">
                    <div className="flex items-center gap-2 mb-1">
                      <span className="bg-amber-500 text-white text-xs font-black px-2 py-0.5 rounded-full">
                        Exercise {exerciseIndex + 1}/{totalExercises}
                      </span>
                      <span className="text-amber-400 text-xs font-bold">+{currentExercise.xp_reward} XP</span>
                    </div>
                    <p className="text-slate-200 text-sm">{currentExercise.description}</p>
                  </div>
                )}

                {/* Exercise nav arrows */}
                {hasExercises && (
                  <div className="flex items-center gap-2 mb-3">
                    <button
                      onClick={() => exerciseIndex > 0 && goToExercise(exerciseIndex - 1)}
                      disabled={exerciseIndex === 0}
                      className="flex items-center gap-1 text-slate-400 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed text-sm transition-colors"
                    >
                      <ChevronLeft className="w-4 h-4" /> Prev
                    </button>
                    <span className="text-slate-600 text-sm flex-1 text-center">
                      {exerciseIndex + 1} / {totalExercises}
                    </span>
                    <button
                      onClick={() => exerciseIndex < totalExercises - 1 && goToExercise(exerciseIndex + 1)}
                      disabled={exerciseIndex === totalExercises - 1 || (!passedExercises.has(exerciseIndex) && exerciseIndex > 0)}
                      className="flex items-center gap-1 text-slate-400 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed text-sm transition-colors"
                    >
                      Next <ChevronRight className="w-4 h-4" />
                    </button>
                  </div>
                )}

                <div className="mt-1 bg-slate-900 rounded-xl p-3 border border-slate-700/50">
                  <p className="text-slate-400 text-xs font-bold mb-1 uppercase tracking-wider">Expected output:</p>
                  <pre className="text-green-400 text-sm font-mono">
                    {currentExercise ? currentExercise.expected_output : lesson.expected_output}
                  </pre>
                </div>
              </div>
            )}

            {panel === "output" && (
              <div className="animate-slide-up">
                {!result ? (
                  <div className="flex flex-col items-center justify-center py-12 text-center">
                    <Play className="w-12 h-12 text-slate-600 mb-3" />
                    <p className="text-slate-400 font-semibold">Run your code to see the output!</p>
                    <p className="text-slate-500 text-sm mt-1">Press the Run Code button or Ctrl+Enter</p>
                  </div>
                ) : (
                  <div className="space-y-3">
                    {/* Status banner */}
                    <div
                      className={`rounded-xl p-3 flex items-center gap-2 font-bold ${
                        result.passed
                          ? "bg-green-500/20 text-green-300 border border-green-500/30"
                          : result.success
                          ? "bg-yellow-500/20 text-yellow-300 border border-yellow-500/30"
                          : "bg-red-500/20 text-red-300 border border-red-500/30"
                      }`}
                    >
                      {result.passed ? (
                        <><CheckCircle className="w-5 h-5" /> Perfect! Output matches! 🎉</>
                      ) : result.success ? (
                        <><XCircle className="w-5 h-5" /> Output doesn&apos;t match yet</>
                      ) : (
                        <><XCircle className="w-5 h-5" /> Compilation error</>
                      )}
                    </div>

                    {/* Next exercise hint */}
                    {result.passed && hasExercises && exerciseIndex < totalExercises - 1 && (
                      <button
                        onClick={() => goToExercise(exerciseIndex + 1)}
                        className="w-full flex items-center justify-center gap-2 bg-indigo-500/20 hover:bg-indigo-500/30 border border-indigo-500/40 text-indigo-300 font-bold rounded-xl p-3 transition-all"
                      >
                        Continue to Exercise {exerciseIndex + 2} <ChevronRight className="w-4 h-4" />
                      </button>
                    )}

                    {/* Output */}
                    {result.output && (
                      <div>
                        <p className="text-xs text-slate-500 font-bold uppercase tracking-wider mb-1">Output</p>
                        <pre className="bg-slate-900 rounded-xl p-3 text-green-300 text-sm font-mono whitespace-pre-wrap border border-slate-700/50">
                          {result.output}
                        </pre>
                      </div>
                    )}

                    {/* Error */}
                    {result.error && (
                      <div>
                        <p className="text-xs text-red-400 font-bold uppercase tracking-wider mb-1">Error</p>
                        <pre className="bg-red-900/20 rounded-xl p-3 text-red-300 text-sm font-mono whitespace-pre-wrap border border-red-500/20">
                          {result.error}
                        </pre>
                      </div>
                    )}

                    {/* Expected vs got */}
                    {!result.passed && result.success && (
                      <div>
                        <p className="text-xs text-slate-500 font-bold uppercase tracking-wider mb-1">Expected</p>
                        <pre className="bg-slate-900 rounded-xl p-3 text-slate-300 text-sm font-mono whitespace-pre-wrap border border-slate-700/50">
                          {currentExercise ? currentExercise.expected_output : lesson.expected_output}
                        </pre>
                      </div>
                    )}

                    <p className="text-xs text-slate-500">⏱ {result.execution_time_ms}ms</p>
                  </div>
                )}
              </div>
            )}

            {panel === "ai" && (
              <AITutor
                lessonId={lessonId}
                code={code}
                errorMessage={result?.error || undefined}
                onClose={() => setPanel("theory")}
              />
            )}
          </div>
        </div>
      </div>

      {/* Success overlay */}
      {showSuccess && (
        <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center z-50 p-4">
          <div className="card p-8 max-w-sm w-full text-center animate-pop shadow-2xl border-green-500/30">
            <div className="text-6xl mb-4 animate-bounce-slow">
              {lesson.is_final_project ? "🏆" : "⭐"}
            </div>
            <h2 className="text-2xl font-black text-white mb-2">
              {lesson.is_final_project ? "World Complete!" : "Level Up!"}
            </h2>
            <p className="text-slate-400 mb-4">
              {lesson.is_final_project
                ? "Amazing work! You completed the whole world!"
                : "Great job! You completed all exercises!"}
            </p>
            <div className="flex items-center justify-center gap-2 bg-amber-500/20 rounded-xl p-3 mb-6">
              <Star className="w-5 h-5 text-amber-400 fill-amber-400" />
              <span className="text-amber-300 font-black text-lg">+{lesson.xp_reward} XP</span>
            </div>
            <div className="flex gap-3">
              <button
                onClick={() => setShowSuccess(false)}
                className="btn-secondary flex-1"
              >
                Keep Coding
              </button>
              <Link href="/worlds" className="flex-1">
                <button className="btn-primary w-full flex items-center justify-center gap-1.5">
                  {lesson.is_final_project ? (
                    <><Trophy className="w-4 h-4" /> Next World</>
                  ) : (
                    <>Next <ChevronRight className="w-4 h-4" /></>
                  )}
                </button>
              </Link>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
