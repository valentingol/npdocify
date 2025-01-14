"""Parameter section parsing functions."""

from functools import partial
from typing import List, Tuple

from docstripy.google.parse_doc import parse_params as parse_params_google
from docstripy.numpy.parse_doc import parse_params as parse_params_numpy
from docstripy.parse_doc.postprocessing import (
    postprocess_default_val,
    postprocess_description,
)
from docstripy.rest.parse_doc import parse_params as parse_params_rest


def parse_params_all(
    lines: List[str],
    style: str,
    section_name: str = "param",
) -> List[dict]:
    r"""Parse parameters, raises, returns, yields and attributes section.

    Parameters
    ----------
    lines : List[str]
        Lines of the docstring containing parameters descriptions.
    style : str
        Format style of the docstring (one of 'numpy', 'google' or 'rest').
    section_name : str, optional
        Name of the section to parse. One of "param", "return", "yield", "attribute",
        "raises". By default, "param".

    Returns
    -------
    params_dict : dict
        Parameters dictionary with the following keys:

        type : dict
            Dictionary of parameter names and their types.
        optional : dict
            Dictionary of parameter names and whether they are optional.
        description : dict
            Dictionary of parameter names and their descriptions.
        default : dict
            Dictionary of parameter names and their default values.

    Example
    -------
    One can parse a docstring as follows:

    .. code-block:: python

        [
            {
                'name': 'param1',
                'type': 'int',
                'optional': False,
                'description': ['Description of param1\n'],
            },
            {
                'name': 'param2',
                'type': 'str',
                'optional': True,
                'description': ['Description of param2\n'],
                'default': '""',
            },
        ],
    """
    pattern_type_rest = "rtype" if section_name in ("return", "yield") else "type"
    parse_params_rest_patterns = partial(
        parse_params_rest,
        pattern_type=pattern_type_rest,
    )
    parse_funcs = {
        "rest": parse_params_rest_patterns,
        "google": parse_params_google,
        "numpy": parse_params_numpy,
    }
    parse_func = parse_funcs[style]
    params_list = parse_func(lines=lines, section_name=section_name)  # type: ignore

    for param_dict in params_list:
        description = param_dict["description"]
        if section_name == "param":
            description, default_val = extract_default_value(param_dict["description"])
            param_dict["default"] = postprocess_default_val(default_val)
            if param_dict["default"] != "":
                param_dict["optional"] = True
        param_dict["description"] = postprocess_description(description)

    if section_name != "param":
        # Remove optional info
        for param_dict in params_list:
            del param_dict["optional"]

    return params_list


def extract_default_value(lines: List[str]) -> Tuple[List[str], str]:
    """Extract default value from description."""
    # Lines merging
    line = "".join(lines)
    patterns = [
        "default is ",
        "Default is ",
        "defaults to ",
        "default to ",
        "Defaults to ",
        "Default to ",
        "by default ",
        "By default ",
        "defaults : ",
        "Defaults : ",
        "default : ",
        "Default : ",
        "defaults: ",
        "Defaults: ",
        "default: ",
        "Default: ",
    ]
    patterns_comma1 = [", " + pattern for pattern in patterns]
    patterns_comma2 = [pattern[:-1] + ", " for pattern in patterns]
    patterns = patterns_comma2 + patterns_comma1 + patterns
    default = ""
    for pattern in patterns:
        if pattern in line:
            default_split1, default_split_2 = line.rsplit(pattern, maxsplit=1)
            default = default_split_2
            for break_pattern in [".\n", "\n", ". "]:
                default = default.split(break_pattern)[0].strip()
            if default + "." in default_split_2:
                line = default_split1 + default_split_2.replace(default + ".", "")
            else:
                line = default_split1 + default_split_2.replace(default, "")
            break
    # Reverse lines merging
    lines = line.split("\n")
    lines = [line + "\n" for line in lines]
    return lines, default
