from typing import Callable

from script_background_music.play import play_random_music_in_background, PlayThread


class BackgroundMusicContext(object):
    """
    Run background music in a given context

    <b>WARNING: Only verified to work on macOS! Should work on Linux and Windows as well since they also create a subprocess under the hood.</b>
    """
    __thread: PlayThread = None

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
