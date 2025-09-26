import typer
from rich import print

def main(name: str):
    print(f"Hello, [bold green]{name}[/bold green]!")

if __name__ == "__main__":
    typer.run(main)


