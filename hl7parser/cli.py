import sys
from enum import Enum
from pathlib import Path
from typing import Callable, Optional

import typer

from hl7parser import __app_name__, __version__
from hl7parser.parsers import HL7MessageParser

app = typer.Typer()


class Formats(str, Enum):
    json = "json"


class SegmentTerminators(str, Enum):
    """Segment terminators for HL7 messages."""

    cr = "cr"
    lf = "lf"
    crlf = "crlf"


SEGMENT_TERMINATORS_CHARACTER_MAP = {
    SegmentTerminators.cr.value: "\r",
    SegmentTerminators.lf.value: "\n",
    SegmentTerminators.crlf.value: "\r\n",
}


@app.command()
def convert(
    file: Path = typer.Argument(..., help="The HL7 Message file to be converted.", exists=True),
    output_format: Optional[Formats] = typer.Option(
        Formats.json.value,
        "--format",
        "-f",
        help="The output format.",
        show_default=True,
    ),
    output: Optional[Path] = typer.Option(
        None,
        help="Optional path to an output file for storing results. [default: stdout]",
    ),
    force_validation: Optional[bool] = typer.Option(
        False, help="Whether to force validation of the HL7 message."
    ),
    segment_terminator: Optional[SegmentTerminators] = typer.Option(
        SegmentTerminators.lf.value,
        "--segment-terminator",
        "-t",
        help="The segment terminator character. [default: 'lf' (\\n)]",
        show_default=False,
    ),
    use_long_name: Optional[bool] = typer.Option(
        True, help="Whether to use long names for fields, e.g. 'patient_name' instead of 'pid_5')"
    ),
    find_groups: Optional[bool] = typer.Option(True, help="Whether to find groups"),
):
    """
    Converts an HL7 file into an appropriate format.
    """
    format_converter: dict[Formats, Callable] = {Formats.json: HL7MessageParser.hl7_to_json}
    kwargs = {
        "segment_terminator": SEGMENT_TERMINATORS_CHARACTER_MAP[segment_terminator],
        "use_long_name": use_long_name,
        "find_groups": find_groups,
        "force_validation": force_validation,
    }

    with file.open("r") as hl7_file:
        content = hl7_file.read()

    result = format_converter[output_format](content, **kwargs)

    with output.open("w") if output else sys.stdout as file_to_write:
        file_to_write.write(result)


def _version_callback(value: bool) -> None:
    if value:
        print(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
