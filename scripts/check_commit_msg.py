"""Хук commit-msg: проверяет, что сообщение коммита начинается с эмодзи из кодстайла."""

import sys
from pathlib import Path

EMOJIS = ("☠️", "💫", "🐞", "⚙️", "📝")


def main() -> int:
    """Проверяет первую строку сообщения коммита.

    Returns:
        int - 0, если сообщение начинается с допустимого эмодзи, иначе 1.

    """
    message = Path(sys.argv[1]).read_text(encoding="utf-8").lstrip()
    if message.startswith(EMOJIS):
        return 0
    allowed = " ".join(EMOJIS)
    sys.stderr.write(f"Сообщение коммита должно начинаться с одного из: {allowed}\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
