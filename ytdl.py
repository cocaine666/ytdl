from pytube import YouTube
import os
import sys
import tkinter
from tkinter import *
import tk

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def download(audio):
    if video_input.get() != "":
        yt_obj = YouTube(video_input.get())
        if audio:
            yt_stream = yt_obj.streams.filter(only_audio=True).first()
            yt_stream.download(resource_path("C:/"))
        else:
            yt_stream = yt_obj.streams.filter(only_audio=False).first()
            yt_stream.download(resource_path("C:/"))
    else:
        return

obj = tkinter.Tk()
obj.title('YTDL')
obj.geometry("250x125")
obj.iconbitmap(r'yt.ico')

padding_label = tkinter.Label(obj, text="        ").grid(row=0, column=2)
link_label = tkinter.Label(obj, text='Link:').grid(row=2,column=3)
video_input = tkinter.Entry(width=25)
cb = BooleanVar()
run_bool = False
conversion_chkbox = tkinter.Checkbutton(obj, variable=cb, text="Convert to MP3").grid(row=3,column=3)
dl_button = tkinter.Button(obj, text='Download', width=25, command=lambda : download(cb.get())).grid(row=4,column=3)


video_input.grid(row=2,column=3)

obj.mainloop()
