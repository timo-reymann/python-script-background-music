"""
Use the elevator music as a context
"""
from typing import Callable, Union

from script_background_music.play import play_random_music_in_background, PlayThread


class BackgroundMusicContext(object):
    """
    Run background music in a given context

    <b>WARNING: Not verified to work on macOS! Should work there as well, since also creates a subprocess under the hood.</b>
    """
    __thread: Union[PlayThread, None] = None

    def __init__(self, player_callback: Callable[[], PlayThread] = play_random_music_in_background):
        """
        Create new background music context

        :param player_callback: Callback to run the music, defaults to<i>script_background_music.play.play_random_music_in_background</i>
        """
        self.__thread = player_callback()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__thread.kill_children()
        self.__thread.terminate()
