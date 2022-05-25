import logging
from threading import Thread

from elevator_music.songs import get_random_song
from elevator_music.vendor.playsound import get_play_sound


def __music(song_title):
    try:
        while True:
            get_play_sound()(song_title, block=True)
            break
    except:
        logging.debug("Could not start music, exiting.")


def play_music_in_background():
    song = get_random_song()
    thread = Thread(target=__music, args=(song,))
    thread.daemon = True
    thread.start()
