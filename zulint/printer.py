from itertools import cycle

# Terminal Color codes for use in differentiating linters
BOLDRED = "\x1B[1;31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN = "\x1b[36m"
WHITE = "\x1b[37m"
BRIGHT_BLACK = "\x1b[90m"
ORANGE = "\x1b[38;5;208m"
PINK = "\x1b[38;5;205m"
PURPLE = "\x1b[38;5;93m"
LIME = "\x1b[38;5;118m"
TEAL = "\x1b[38;5;30m"
BROWN = "\x1b[38;5;94m"
SKY_BLUE = "\x1b[38;5;117m"
ENDC = "\033[0m"

colors = cycle([
    GREEN,
    YELLOW,
    BLUE,
    MAGENTA,
    CYAN,
    WHITE,
    BRIGHT_BLACK,
    ORANGE,
    PINK,
    PURPLE,
    LIME,
    TEAL,
    BROWN,
    SKY_BLUE,
])

def print_err(name: str, color: str, line: str) -> None:
    print('{color}{name}{pad}|{end} {red_color}{line!s}{end}'.format(
        color=color,
        name=name,
        pad=' ' * max(0, 10 - len(name)),
        red_color=BOLDRED,
        line=line.rstrip(),
        end=ENDC,
    ), flush=True)
