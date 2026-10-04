import subprocess
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: novarestorecheck ARCHIVE", file=sys.stderr)
        raise SystemExit(2)
    path = Path(sys.argv[1])
    if not path.is_file():
        print("Archive does not exist or is not a file", file=sys.stderr)
        raise SystemExit(2)
    try:
        result = subprocess.run(
            ["pg_restore", "--list", str(path)],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"Unable to inspect archive: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    if result.returncode:
        print(result.stderr.strip() or "Invalid PostgreSQL archive", file=sys.stderr)
        raise SystemExit(1)
    print(f"Archive catalog readable: {path}")
