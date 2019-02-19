"""Functions associated with formatting output."""

import math
import shutil
from itertools import zip_longest
from typing import List, Text, Tuple

COLUMN_MARGIN = 3


def get_columns_count_and_width(strings: List[Text]) -> Tuple[int, int]:
    """Calculate the optimal width and number of columns to display a list of strings.

    :param strings: list of strings
    :return: a tuple with the number of columns and column width
    """
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    max_string_width = max(len(string) for string in strings)
    col_width = max_string_width + COLUMN_MARGIN
    num_cols = int(terminal_width / col_width)

    if num_cols > len(strings):
        num_cols = len(strings)

    return num_cols, col_width


def list_to_columns(strings: List[Text]) -> Text:
    """Prepare multi-column output string from a list of strings."""
    num_cols, col_width = get_columns_count_and_width(strings)
    col_height = math.ceil(len(strings) / num_cols)
    cols = [strings[i : i + col_height] for i in range(0, len(strings), col_height)]

    format_string = "{:<}\n"  # noqa
    for _ in range(num_cols - 1):
        format_string = "{{:<{0}}}{1}".format(col_width, format_string)

    strings_in_columns = ""
    for col_strings in zip_longest(*cols, fillvalue=""):
        strings_in_columns += format_string.format(*col_strings)
    return strings_in_columns
