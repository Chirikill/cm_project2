import sys
import typer

app = typer.Typer()

@app.command()
def start():
    """Запуск анализатора"""
    print(" Анализатор зависимостей запущен!")

app()
