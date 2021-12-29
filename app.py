from typing import Optional
import typer

app = typer.Typer()


@app.command()
def hello(name: Optional[str] = typer.Argument(None, help="A person name")):
    """Say hi to name.

    Args:
        name (str, optional): a person name

    Returns:
        [type]: an echo color goodbye
    """
    if name is not None:
        return typer.secho(f"Hello {name}", fg=typer.colors.GREEN, bold=True)

    return typer.secho(f"Hello", fg=typer.colors.GREEN, bold=True)


@app.command()
def goodbye(
    name: Optional[str] = typer.Argument(None, help="A person name"),
    formal: bool = typer.Option(False),
):
    """Say goodbye to name (if --formal is used, say goodbye very formally).

    Args:
        name (str, optional): person name
        formal (bool, optional): formal parameter. Defaults to False.

    Returns:
        [type]: an echo color goodbye
    """
    if not formal:
        message = "Bye"
        if name is not None:
            return typer.secho(message + f" {name}", fg=typer.colors.GREEN, bold=True)

        return typer.secho(message, fg=typer.colors.GREEN, bold=True)

    message = "Goodbye"
    if name is not None:
        return typer.secho(
            message + f" Ms. {name}. Have a nice day.", fg=typer.colors.BLUE, bold=True
        )

    return typer.secho(message + ". Have a nice day.", fg=typer.colors.BLUE, bold=True)


if __name__ == "__main__":
    app()
