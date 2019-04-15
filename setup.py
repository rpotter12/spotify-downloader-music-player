from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
	name="spotpl",
	version="1.1.0",
	install_requires=["spotdl >= 1.2.0"],
	packages=find_packages(),
	description="Download youtube songs in mp3 format and plays them",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rohit Potter",
    author_email="rohitpotter12@gmail.com",
    license="MIT",
    python_requires=">=3.4",
    url="https://github.com/rpotter12/spotify-downloader-music-player",
    download_url="https://pypi.org/project/spotpl/",
    keywords=[
        "spotify",
        "downloader",
        "download",
        "music",
        "youtube",
        "mp3",
        "album",
        "metadata",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["spotpl = spotpl.spotpl:songnamee"]},
	)
