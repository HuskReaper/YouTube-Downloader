# Imports #
from pytube import YouTube
from colorama import Fore, Back, Style
import os, time

# Variables #
link = ""
type = ""
video = YouTube(link).streams.first().download()
app_closed = False

# Functions #
def downloader():
    if type == "Video":
        video.streams.filter(progressive=True, file_extension = 'mp4')

# Code #
while not app_closed:
    os.sytem("clear")
    print(f"{Fore.LIGHTWHITE_EX}YouTube Downloader")
    print(Style.RESET_ALL)
    link = input("Element Link > ").strip()
    type = input("Type > ").strip().capitalize()

