import logging
from threading import Thread
from typing import Union

from script_background_music.songs import get_random_song
from script_background_music.vendor.playsound import get_play_sound


def __music(song_title):
    try:
        while True:
            get_play_sound()(song_title, block=True)
            break
    except:
        logging.debug("Could not start music, exiting.")


def play_music_in_background(song_file: Union[str, None] = None):
    """
    Play music in background if no song is provided, a random will be picked

    :param song_file: Song to play, set to None or omit to use a random one
    """
    song_to_play = get_random_song() if song_file is None else song_file
    thread = Thread(target=__music, args=(song_to_play,))
    thread.daemon = True
    thread.start()


def play_random_music_in_background():
    """
    Play random music from the available songs in the background
    """
    play_music_in_background(None)


def play_song_in_background(file_name: str):
    """
    Play song from given file in background
    :param file_name: Filename of song to play in background
    :return:
    """
    play_music_in_background(file_name)
