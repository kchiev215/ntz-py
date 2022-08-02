"""RP To-Do entry point script."""
# rptodo/__main__.py

from rptodo import cli, __app_name__

def main():
    # In __main__.py, you first import cli and __app_name__ from rptodo. Then you define main().
    # In this function, you call the Typer app with cli.app(), passing the application’s name to the prog_name argument.
    # Providing a value to prog_name ensures that your users get the correct app name when running the
    # --help option on their command line.
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()