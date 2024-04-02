import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = entry.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text= ytObject.title)
        finishedlabel.configure(text="")
        video.download()
        finishedlabel.configure(text="Download finished")
    except:
        finishedlabel.configure(text="Download failed", text_color= "red")
        print(Exception)
        
def on_progress(stream, chunk, bytes_remaining):
    total_size =  stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    percentage = str(int(percentage_of_completion))
    pPercentage.configure(text=percentage + "%")
    pPercentage.update()
    
    progressBar.set(float(percentage / 100))


customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a youtube link", font=("Arial", 20))
title.pack(padx=10, pady=10)

# make stringvar to store the url
url_var = tkinter.StringVar()
entry = customtkinter.CTkEntry(app, width=400, font=("Arial", 15), textvariable=url_var)
entry.pack()

finishedlabel = customtkinter.CTkLabel(app, text="")
finishedlabel.pack()

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10 , pady=10)

Button = customtkinter.CTkButton(app, text="Download", font=("Arial", 15), command=startDownload)
Button.pack(padx=10, pady=10)

app.mainloop()