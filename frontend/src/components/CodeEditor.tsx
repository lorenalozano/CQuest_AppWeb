"use client";
import dynamic from "next/dynamic";
import { useRef } from "react";

const MonacoEditor = dynamic(
  () => import("@monaco-editor/react").then((m) => m.default),
  { ssr: false, loading: () => <div className="w-full h-full bg-[#1e1e2e] animate-pulse rounded-lg" /> }
);

interface CodeEditorProps {
  value: string;
  onChange: (value: string) => void;
  height?: string;
  readOnly?: boolean;
}

export function CodeEditor({ value, onChange, height = "400px", readOnly = false }: CodeEditorProps) {
  const editorRef = useRef<unknown>(null);

  function handleEditorDidMount(editor: unknown) {
    editorRef.current = editor;
  }

  return (
    <div className="rounded-xl overflow-hidden border border-slate-700 shadow-xl">
      <div className="flex items-center gap-2 bg-[#1e1e2e] px-4 py-2 border-b border-slate-700">
        <div className="w-3 h-3 rounded-full bg-red-500" />
        <div className="w-3 h-3 rounded-full bg-yellow-500" />
        <div className="w-3 h-3 rounded-full bg-green-500" />
        <span className="ml-2 text-slate-400 text-sm font-mono">main.c</span>
      </div>
      <MonacoEditor
        height={height}
        language="c"
        theme="vs-dark"
        value={value}
        onChange={(v) => onChange(v ?? "")}
        onMount={handleEditorDidMount}
        options={{
          fontSize: 22,
          lineHeight: 32,
          fontFamily: "'JetBrains Mono', 'Fira Code', Consolas, monospace",
          minimap: { enabled: false },
          scrollBeyondLastLine: false,
          lineNumbers: "on",
          renderLineHighlight: "all",
          cursorBlinking: "smooth",
          readOnly,
          padding: { top: 12, bottom: 12 },
          wordWrap: "on",
          automaticLayout: true,
          suggestOnTriggerCharacters: true,
          quickSuggestions: true,
          tabSize: 4,
        }}
      />
    </div>
  );
}
