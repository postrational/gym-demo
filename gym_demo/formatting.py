"""Functions associated with formatting output."""

import math
import shutil
from itertools import zip_longest
from typing import Any, List, Text, Tuple

import colorful
from colorful import Colorful

colorful.use_style("solarized")
COLUMN_MARGIN = 3


def get_columns_count_and_width(strings: List[Text]) -> Tuple[int, int]:
    """Calculate how to break a list of strings into multiple columns.

    Calculate the optimal column width and number of columns
    to display a list of strings on screen.

    :param strings: list of strings
    :return: a tuple with the number of columns and column width
    """
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    max_string_width = max(len(string) for string in strings)
    col_width = max_string_width + COLUMN_MARGIN
    num_cols = int(terminal_width / col_width)

    if num_cols > len(strings):
        num_cols = len(strings)

    if num_cols == 0:
        num_cols = 1

    return num_cols, col_width


def list_to_columns(strings: List[Text]) -> Text:
    """Prepare multi-column output string from a list of strings."""
    if len(strings) == 0:
        return ""

    num_cols, col_width = get_columns_count_and_width(strings)
    col_height = math.ceil(len(strings) / num_cols)
    cols = [strings[i : i + col_height] for i in range(0, len(strings), col_height)]
    num_cols = len(cols)

    format_string = "{:<}\n"  # noqa
    for _ in range(num_cols - 1):
        format_string = "{{:<{0}}}{1}".format(col_width, format_string)

    strings_in_columns = ""
    for col_strings in zip_longest(*cols, fillvalue=""):
        strings_in_columns += format_string.format(*col_strings)
    return strings_in_columns


def _print_colorful(color: Colorful.ColorfulStyle, *args: Any) -> None:
    if len(args) > 1:
        string = " ".join(str(arg) for arg in args)
    else:
        string = args[0]
    print(color | string)


def print_header(*args: Any) -> None:
    """Print heading text to console.

    A color will be used to distinguish the heading from other text.
    """
    _print_colorful(colorful.bold & colorful.blue, *args)


def print_error(*args: Any) -> None:
    """Print an error message to console.

    A color will be used to distinguish the heading from other text.
    """
    _print_colorful(colorful.bold & colorful.red, *args)
