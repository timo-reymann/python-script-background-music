#!/usr/bin/env python3
import sys
from time import sleep

from script_background_music import play_music_in_background, BackgroundMusicContext


def main_background():
    play_music_in_background()
    input()


def main_context():
    while True:
        with BackgroundMusicContext():
            print("Press any key to play random song")
            input()


if __name__ == "__main__":
    main_context()
