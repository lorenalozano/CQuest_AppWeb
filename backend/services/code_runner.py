import subprocess
import tempfile
import os
import time


def run_c_code(code: str, expected_output: str) -> dict:
    start = time.time()

    with tempfile.TemporaryDirectory() as tmpdir:
        src = os.path.join(tmpdir, "main.c")
        exe = os.path.join(tmpdir, "main")

        with open(src, "w") as f:
            f.write(code)

        compile_result = subprocess.run(
            ["gcc", "-o", exe, src, "-lm", "-Wall"],
            capture_output=True,
            text=True,
            timeout=10,
        )

        if compile_result.returncode != 0:
            elapsed = int((time.time() - start) * 1000)
            return {
                "output": "",
                "error": compile_result.stderr,
                "success": False,
                "passed": False,
                "execution_time_ms": elapsed,
            }

        try:
            run_result = subprocess.run(
                [exe],
                capture_output=True,
                text=True,
                timeout=3,
                cwd=tmpdir,
            )
        except subprocess.TimeoutExpired:
            elapsed = int((time.time() - start) * 1000)
            return {
                "output": "",
                "error": "Time limit exceeded (3 seconds). Check for infinite loops!",
                "success": False,
                "passed": False,
                "execution_time_ms": elapsed,
            }

        elapsed = int((time.time() - start) * 1000)
        output = run_result.stdout
        error = run_result.stderr

        passed = output.strip() == expected_output.strip()

        return {
            "output": output,
            "error": error,
            "success": run_result.returncode == 0,
            "passed": passed,
            "execution_time_ms": elapsed,
        }
