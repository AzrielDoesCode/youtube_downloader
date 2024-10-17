import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pytube import YouTube

def download():
    # Get the URL from the entry field and strip any leading/trailing spaces
    url = url_entry.get().strip()
    
    # Print the URL to the console for debugging purposes
    print(f"Attempting to download from URL: {url}")  # Debugging line
    
    try:
        yt = YouTube(url)  # Attempt to create a YouTube object
        video = yt.streams.filter(file_extension='mp4').all()   # Get all available streams
        video.download()  # Download the video
        messagebox.showinfo("Download Complete", " downloaded successfully.")
    except Exception as e:
        # Show an error message if something goes wrong
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.geometry("600x600")
window.title("YTC")
window.resizable(False, False)

# Title label with formatted text
title_frame = tk.Frame(window)
title_frame.pack(pady=20)

yt_label = tk.Label(title_frame, text="You", font=("Helvetica", 36))
yt_label.pack(side=tk.LEFT)

tube_label = tk.Label(title_frame, text="Tube", font=("Helvetica", 36), fg="red")
tube_label.pack(side=tk.LEFT)

downloader_label = tk.Label(window, text="downloader", font=("Helvetica", 24))
downloader_label.pack()

url_label = tk.Label(window, text="Enter a Youtube Link to download:")
url_label.pack(pady=20)

url_entry = tk.Entry(window, width=40)
url_entry.pack(pady=20)

download_button = tk.Button(window, text="Proceed Download", command=download)
download_button.pack(pady=20)

window.mainloop()