import pytube
from pytube import YouTube
import os
import sys
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def input_link():
    address = str(input("Please input your YouTube video link: "))
    return address

if __name__ == "__main__":
    clear_console = lambda: os.system('cls')
    run_dialog = True
    while run_dialog:
        clear_console()
        print("YouTube Music Downloader by malbasic - 1.0.0.0")
        print(" ") # Spacer...  lel
        print("Current download location --> C:// ")
        print(" ")
        yt_obj = YouTube(input_link())
        print("Loading video information...")
        print(" ")
        print("Video Title: ", yt_obj.title)
        print(" ")
        confirm = input("Do you want to confirm the download? Y/N/E ")
        if confirm == 'Y':
            yt_stream = yt_obj.streams.filter(only_audio=True).first()
            yt_stream.download(resource_path("C:/"))
        if confirm == 'N':
            clear_console()
        if confirm == 'E':
            run_dialog = False
    exit()
