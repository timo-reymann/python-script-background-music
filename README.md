script-background-music
===
[![CircleCI](https://circleci.com/gh/timo-reymann/python-script-background-music.svg?style=shield)](https://app.circleci.com/pipelines/github/timo-reymann/python-script-background-music)
[![GitHub Release](https://img.shields.io/github/v/tag/timo-reymann/python-script-background-music.svg?label=version)](https://github.com/timo-reymann/python-script-background-music/releases)
[![PyPI version](https://badge.fury.io/py/script-background-music.svg)](https://pypi.org/project/script-background-music)
[![pre-commit](https://img.shields.io/badge/%E2%9A%93%20%20pre--commit-enabled-success)](https://pre-commit.com/)

<p align="center">
  <img width="300" src=".github/images/elevator.png">
</p>

<p align="center">
  <b>script-background-music</b> - Play elevator music in the background while your script runs.
</p>

## Why?

> **Everything** is better with music!

## Usage

It is very simple to use the package inside your scripts ...

### ... the entire time, until your script exits

```python
from script_background_music import play_music_in_background

play_music_in_background()
```

### ... for a specific set of instructions

```python
from script_background_music import BackgroundMusicContext

with BackgroundMusicContext():
    # your instructions go here
    pass
```

## Notes on implementation

### Can it break my script?

No, it should not at least. If something goes wrong playing music etc. it simply wont play music.
If you encounter the opposite feel free to create a bug report.

## Credits

- Special thanks to [@TaylorSMarks](https://github.com/TaylorSMarks/) for
  creating [playsound](https://github.com/TaylorSMarks/playsound) that I modified and ship with this package.
- [Clker-Free-Vector-Images](https://pixabay.com/users/clker-free-vector-images-3736/) for the
  wonderful [elevator image](https://pixabay.com/vectors/elevator-people-silhouette-down-44013/) used as project image
