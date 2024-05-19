"""
Infrastructure to facilitate playing songs
"""
import logging
from multiprocessing import Process
from typing import Union
import psutil
from script_background_music.songs import get_random_song
from script_background_music.vendor.playsound import get_play_sound


class PlayThread(Process):
    """
    Thread to be used for playing songs
    """
    def kill_children(self):
        """
        Ensures all player child threads are terminated properly
        """
        process = psutil.Process(self.pid)
        for child in process.children(recursive=True):
            child.kill()


def __music(song_title):
    try:
        while True:
            get_play_sound()(song_title, block=True)
    except:
        logging.debug("Could not start music, exiting.")


def play_music_in_background(song_file: Union[str, None] = None) -> PlayThread:
    """
    Play music in background if no song is provided, a random will be picked

    :param song_file: Song to play, set to None or omit to use a random one
    :return: Underlying thread for playing music
    """
    song_to_play = get_random_song() if song_file is None else song_file
    thread = PlayThread(target=__music, args=(song_to_play,))
    thread.start()
    return thread


def play_random_music_in_background() -> PlayThread:
    """
    Play random music from the available songs in the background

    :return: Underlying thread for playing music
    """
    return play_music_in_background(None)


def play_song_in_background(file_name: str) -> PlayThread:
    """
    Play song from given file in background

    :param file_name: Filename of song to play in background
    :return: Underlying thread for playing music
    """
    return play_music_in_background(file_name)
