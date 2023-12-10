# Imports #
import tkinter, customtkinter
from pytube import YouTube

# Functions #
def download_video():
  finishLabel.configure(text="Downloading...", text_color="white") # Sets indicator label to a "default" state if the button is clicked.

  try:
    link = link_input.get()
    ytObject = YouTube(link)
    link_label.configure(text=ytObject.title, text_color='white')
    finishLabel.configure(text="Downloaded", text_color='green')

    ytObject = ytObject.streams.get_highest_resolution().download() # Downloads the video with highest res.

  except Exception as error:
    print(f"There has been an error: {error}") # Prints error.
    finishLabel.configure(text="Error Downloading Object") # Sets label to indicate an error.
  
def download_audio():
  finishLabel.configure(text="Downloading...", text_color="white")

  try:
    link = link_input.get()
    ytObject = YouTube(link)
    link_label.configure(text=ytObject.title, text_color='white')
    finishLabel.configure(text="Downloaded", text_color='green')

    ytObject = ytObject.streams.get_audio_only().download()

  except Exception as error:
    print(f"There has been an error: {error}")
    finishLabel.configure(text="Error Downloading Object")

# Tkinter Settings #
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480") # Sets window borders.
app.title("YouTube Downloader with Python") # Sets window title.

link_label = customtkinter.CTkLabel(app, text="Insert YouTube Link", font=("arial", 25))
link_input = customtkinter.CTkEntry(app, width=350, height=40)
link_label.pack(padx=10, pady=10)
link_input.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

video_button = customtkinter.CTkButton(app, text="Download Video", command=download_video)
audio_button = customtkinter.CTkButton(app, text="Download Audio", command=download_audio)
video_button.pack(pady=10)
audio_button.pack(pady=10)

# Code #
app.mainloop()