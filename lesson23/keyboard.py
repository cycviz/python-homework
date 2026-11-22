"""Неблокирующее чтение клавиш без сторонних библиотек (macOS/Linux/Windows).

Возвращает 'w', 'a', 's', 'd', 'f', 'g', 'q' (стрелки и русская раскладка
приводятся к ним же) или None, если ничего не нажато.
"""
import os
import sys

# Русская раскладка -> латиница, чтобы не переключать язык
RU_TO_EN = {"ц": "w", "ф": "a", "ы": "s", "в": "d", "а": "f", "п": "g", "й": "q"}
ARROWS = {"A": "w", "B": "s", "D": "a", "C": "d"}


def _normalize(ch):
    ch = ch.lower()
    return RU_TO_EN.get(ch, ch)


if os.name == "nt":
    import msvcrt

    WIN_ARROWS = {"H": "w", "P": "s", "K": "a", "M": "d"}

    class KeyReader:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def get_key(self):
            if not msvcrt.kbhit():
                return None
            ch = msvcrt.getwch()
            if ch in ("\x00", "\xe0"):
                return WIN_ARROWS.get(msvcrt.getwch())
            return _normalize(ch)

else:
    import select
    import termios
    import tty

    class KeyReader:
        def __enter__(self):
            self.fd = sys.stdin.fileno()
            self.old = termios.tcgetattr(self.fd)
            tty.setcbreak(self.fd)            # символы без Enter и без эха
            sys.stdout.write("\033[?25l")     # спрятать курсор
            return self

        def __exit__(self, *exc):
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old)
            sys.stdout.write("\033[?25h")     # вернуть курсор
            sys.stdout.flush()
            return False

        def get_key(self):
            if not select.select([sys.stdin], [], [], 0)[0]:
                return None
            data = os.read(self.fd, 8).decode("utf-8", errors="ignore")
            if data.startswith("\x1b["):      # стрелки: ESC [ A/B/C/D
                return ARROWS.get(data[2:3])
            return _normalize(data[0]) if data else None
