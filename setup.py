import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twitch_plays_hackRU", 
    version="1.0.0",
    author="Jeffrey Fung",
    author_email="jeff.fung07@gmail.com",
    description="A TwitchPlays API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HackRU/twitch-plays",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)