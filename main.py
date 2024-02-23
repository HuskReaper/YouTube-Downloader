### NOTES ###
'''
This is a YouTube downloader using pytube3, tkinter, and customtkinter.
Usage of new library is required as pytube is deprecated.
The library pytube3 has many bugs, so expect to encounter server-side errors.
Please read README.md
'''
### IMPORTS ###
import tkinter, customtkinter
from pytube import YouTube

### TKINTER SETTINGS ###
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x400") # Sets window borders.
app.title("YouTube Downloader with Python") # Sets window title.

link_label = customtkinter.CTkLabel(app, text="Insert YouTube Link", font=("arial", 25)); link_label.pack(padx=10, pady=10) # Main label.
link_input = customtkinter.CTkEntry(app, width=350, height=40); link_input.pack()
status_label = customtkinter.CTkLabel(app, text=""); status_label.pack() # Status label.

# Functions #
def download_video():
  status_label.configure(text="Downloading...", text_color="white")
  
  try:
    link = link_input.get()
    ytObject = YouTube(link)
    link_label.configure(text=ytObject.title, text_color='white')
    ytObject = ytObject.streams.get_highest_resolution().download() # Downloads the video with highest res.
    YouTube.register_on_complete_callback(status_label.configure(text="Downloaded", text_color='green'))

  except Exception as error:
    status_label.configure(text="Error Downloading Object") # Sets label to indicate an error.
    print(f"There has been an error: {error}") # Prints error.
  
def download_audio():
  status_label.configure(text="Downloading...", text_color="white")

  try:
    link = link_input.get()
    ytObject = YouTube(link)
    link_label.configure(text=ytObject.title, text_color='white')
    ytObject = ytObject.streams.get_audio_only().download()
    YouTube.register_on_complete_callback(status_label.configure(text="Downloaded", text_color='green'))

  except Exception as error:
    status_label.configure(text="Error Downloading Object")
    print(f"There has been an error: {error}")

# Code #
video_button = customtkinter.CTkButton(app, text="Download Video", command=download_video); video_button.pack(padx=10, pady=10)
audio_button = customtkinter.CTkButton(app, text="Download Audio", command=download_audio); audio_button.pack()
app.mainloop()