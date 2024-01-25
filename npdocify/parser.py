"""File parsing functions."""
from typing import List


def docstring_parse_file(lines: List[str]) -> List[List[int]]:
    """Parse source code lines.

    Parameters
    ----------
    lines : List[str]
        List of lines to parse.

    Returns
    -------
    range_docstr : List[List[int]]
        List of ranges of docstring line numbers [start, end]. Includes line at start,
        excludes line at end.
    """
    range_docstr = []
    in_docstr = False
    docstring_starters = ('"""', "'''", 'r"""', "r'''")
    for i, line in enumerate(lines):
        strip_line = line.strip()
        if strip_line.startswith(docstring_starters) and line.startswith(" "):
            # Case one-line docstring
            if (
                (strip_line.count('"""') > 1 or strip_line.count("'''") > 1)
                and not in_docstr
            ):
                range_docstr.append([i, i + 1])
            else:
                # Case multi-line docstring
                if not in_docstr:
                    current_range = [i]
                    in_docstr = True
                else:
                    current_range.append(i + 1)
                    range_docstr.append(current_range)
                    in_docstr = False
    return range_docstr
