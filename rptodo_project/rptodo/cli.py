"""This module provides the RP To-Do CLI."""
# rptodo/cli.py

from typing import Optional

import typer

from rptodo import __app_name__, __version__

app = typer.Typer()  # creates an explicit Typer application, app


def _version_callback(value: bool) -> None:
    """This function takes a Boolean argument called value.
    If value is True, then the function prints the application’s name and version using echo().
    After that, it raises a typer.Exit exception to exit the application cleanly."""
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()  # define main() as a Typer callback using the @app.callback() decorator.
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
