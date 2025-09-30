import typer
from yadio.yadio import YadioApi as yadio
from typing import Optional
app = typer.Typer(help="Mi app de ejemplo con Typer")


@app.command()
def ping():
    """
    Checks the server status.
    """
    response = yadio.ping_server()
    typer.echo(response)


@app.command()
def convert(amount: float, currency_from: str, currency_to: str):
    """ """
    response = yadio.get_convert(amount, currency_from, currency_to)
    typer.echo(response)

@app.command()
def rate(quote : str , base: str):
    response= yadio.get_rate( quote , base)
    typer.echo(response)

@app.command()
def exrates(currency : str = Optional[str]):
    response= yadio.get_exrates(currency)
    typer.echo(response)

@app.command()
def currencies():
    response= yadio.get_currencies()
    typer.echo(response)

if __name__ == "__main__":
    app()
