"""
Songs to play
"""
from random import choice
from pathlib import Path

SONGS = [
    "local-forecast",
    "lofi",
    "overcast"
]


def __get_song(name: str) -> Path:
    base_directory = Path(__file__).parent
    return base_directory / f"{name}.mp3"


def get_random_song() -> Path:
    """
    Pick random song from the selection
    """
    return __get_song(choice(SONGS))
