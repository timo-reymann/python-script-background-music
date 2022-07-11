from setuptools import setup, find_packages
from os import environ

with open("README.md", "r") as readme_file:
    readme = "".join(readme_file.readlines()) \
        .replace(
        ".github/images/elevator.png",
        "https://raw.githubusercontent.com/timo-reymann/python-script-background-music/main/.github/images/elevator.png"
    )

setup(
    name='script-background-music',
    version=environ.get("VERSION", "snapshot"),
    author="Timo Reymann <mail@timo-reymann.de>",
    url="https://github.com/timo-reymann/python-script-background-music",
    include_package_data=True,
    packages=find_packages(),
    requires=[],
    python_requires='>3.8.0',
    description="Play elevator music in the background while your script runs.",
    long_description=readme,
    long_description_content_type='text/markdown'
)
