import re

DEFAULT_TYPES = [
    "feat",
    "fix",
    "build",
    "chore",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "refactor",
    "revert",
    "style",
    "test",
]


def r_types(types):
    """Join types with pipe "|" to form regex ORs."""
    return "|".join(types)


def r_scope(optional=True):
    """Regex str for an optional (scope)."""
    if optional:
        return r"(\([\w \/:-]+\))?"
    else:
        return r"(\([\w \/:-]+\))"


def r_delim():
    """Regex str for optional breaking change indicator and colon delimiter."""
    return r"!?:"


def r_subject():
    """Regex str for subject line, body, footer."""
    return r" .+"


def is_conventional(input, types=DEFAULT_TYPES, optional_scope=True):
    """
    Returns True if input matches Conventional Commits formatting
    https://www.conventionalcommits.org

    Optionally provide a list of additional custom types.
    """
    types = set(types)
    pattern = f"^({r_types(types)}){r_scope(optional_scope)}{r_delim()}{r_subject()}$"
    regex = re.compile(pattern, re.DOTALL)

    return bool(regex.match(input))
