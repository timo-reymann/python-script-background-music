from random import choice
from pathlib import Path

SONGS = [
    "local-forecast",
    "lofi"
]


def __get_song(name: str) -> Path:
    base_directory = Path(__file__).parent
    return base_directory / f"{name}.mp3"


def get_random_song() -> Path:
    return __get_song(choice(SONGS))
