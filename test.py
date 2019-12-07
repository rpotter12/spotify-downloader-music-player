from tkinter import *
import os
from tkinter import filedialog
import tkinter
from tkinter import ttk

root = None
active_window = None

root = tkinter.Tk()
root.title('spotify-downloader-music-player')

# Set the configuration of GUI window  
root.geometry("700x175") 

# Function for song name
def songnamee():
    frame1 = Frame(root, borderwidth=2, relief='ridge')  
    frame2 = Frame(root, borderwidth=2, relief='ridge')  
    frame3 = Frame(root, borderwidth=2, relief='ridge')
    frame4 = Frame(root, borderwidth=0, relief='ridge')
    frame5 = Frame(root, borderwidth=0, relief='ridge')
    frame6 = Frame(root, borderwidth=0, relief='ridge')
     
    frame1.grid(column=0, row=0, sticky="nsew")  
    frame2.grid(column=0, row=1, sticky="nsew")  
    frame3.grid(column=0, row=2, sticky="nsew")
    frame4.grid(column=1, row=0, sticky="nsew")
    frame5.grid(column=2, row=0, sticky="nsew")
    frame6.grid(column=2, row=1, sticky="nsew")

    menu = Menu(root) 
    root.config(menu=menu) 
    filemenu = Menu(menu) 
    menu.add_cascade(label='Download Type', menu=filemenu) 
    filemenu.add_command(label='Song Name', command=songnamee) 
    filemenu.add_command(label='Youtube Link', command=youtubelink) 
    filemenu.add_command(label='File', command=file) 
         
    home = Button(frame1, text="HOME",width=15, command=songnamee)  
    playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
    about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
    songName = Entry(frame4, width=40)
    download = Button(frame5, text="Download", command=lambda: downloadname(songName))
    progress = ttk.Progressbar(frame6,orient ="horizontal",length = 200, mode ="determinate")
     
    home.pack(fill='x')  
    playlist.pack(fill='x')  
    about.pack(fill='x')
    songName.pack()
    download.pack()
    progress.pack()
     
    root.mainloop() 

# Function for youtube link button
def youtubelink():
    frame1 = Frame(root, borderwidth=2, relief='ridge')  
    frame2 = Frame(root, borderwidth=2, relief='ridge')  
    frame3 = Frame(root, borderwidth=2, relief='ridge')
    frame4 = Frame(root, borderwidth=0, relief='ridge')
    frame5 = Frame(root, borderwidth=0, relief='ridge')
    frame6 = Frame(root, borderwidth=0, relief='ridge')
     
    frame1.grid(column=0, row=0, sticky="nsew")  
    frame2.grid(column=0, row=1, sticky="nsew")  
    frame3.grid(column=0, row=2, sticky="nsew")
    frame4.grid(column=1, row=0, sticky="nsew")
    frame5.grid(column=2, row=0, sticky="nsew")
    frame6.grid(column=3, row=1, sticky="nsew")

    menu = Menu(root) 
    root.config(menu=menu) 
    filemenu = Menu(menu) 
    menu.add_cascade(label='Download Type', menu=filemenu) 
    filemenu.add_command(label='Song Name', command=songnamee) 
    filemenu.add_command(label='Youtube Link', command=youtubelink) 
    filemenu.add_command(label='File', command=file) 
         
    home = Button(frame1, text="HOME",width=15, command=youtubelink)  
    playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
    about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
    songLink = Entry(frame4, width=40)
    download = Button(frame5, text="Download", command=lambda: downloadlink(songLink))
     
    home.pack(fill='x')  
    playlist.pack(fill='x')  
    about.pack(fill='x')
    songLink.pack()
    download.pack()

# Function for file button
def file():
    frame1 = Frame(root, borderwidth=2, relief='ridge')  
    frame2 = Frame(root, borderwidth=2, relief='ridge')  
    frame3 = Frame(root, borderwidth=2, relief='ridge')
    frame4 = Frame(root, borderwidth=0, relief='ridge')
    frame5 = Frame(root, borderwidth=0, relief='ridge')
    frame6 = Frame(root, borderwidth=0, relief='ridge')
     
    frame1.grid(column=0, row=0, sticky="nsew")  
    frame2.grid(column=0, row=1, sticky="nsew")  
    frame3.grid(column=0, row=2, sticky="nsew")
    frame4.grid(column=1, row=0, sticky="nsew")
    frame5.grid(column=2, row=0, sticky="nsew")
    frame6.grid(column=3, row=1, sticky="nsew")

    menu = Menu(root) 
    root.config(menu=menu) 
    filemenu = Menu(menu) 
    menu.add_cascade(label='Download Type', menu=filemenu) 
    filemenu.add_command(label='Song Name', command=songnamee) 
    filemenu.add_command(label='Youtube Link', command=youtubelink) 
    filemenu.add_command(label='File', command=file)  
         
    home = Button(frame1, text="HOME",width=15, command=file)  
    playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
    about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
    filetxt = Entry(frame4, width=40)
    download = Button(frame5, text="Download", command=lambda: downloadfile(filetxt))
     
    home.pack(fill='x')  
    playlist.pack(fill='x')  
    about.pack(fill='x')
    filetxt.pack()
    download.pack()

# Function for about button
def aboutbackground():
    frame1 = Frame(root, borderwidth=2, relief='ridge')  
    frame2 = Frame(root, borderwidth=2, relief='ridge')  
    frame3 = Frame(root, borderwidth=2, relief='ridge')
    frame4 = Frame(root, borderwidth=0, relief='ridge')
    frame5 = Frame(root, borderwidth=0, relief='ridge')
    frame6 = Frame(root, borderwidth=0, relief='ridge')
     
    frame1.grid(column=0, row=0, sticky="nsew")  
    frame2.grid(column=0, row=1, sticky="nsew")  
    frame3.grid(column=0, row=2, sticky="nsew")
    frame4.grid(column=1, row=0, sticky="nsew")
    frame5.grid(column=1, row=1, sticky="nsew")
    frame6.grid(column=1, row=2, sticky="nsew")
     
    home = Button(frame1, text="HOME",width=15, command=youtubelink)  
    playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
    about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
    Label(frame4, text="A GUI version of spotify-downloder of Ritiek Malhotra.").pack()
    Label(frame5, text="It can download music from YouTube in MP3 format and can play them.").pack()
    Label(frame6, text="It can download songs directly by typing name or typing the link.").pack()
     
    home.pack(fill='x')  
    playlist.pack(fill='x')  
    about.pack(fill='x')

# Function for playlist button
def playlistbackground():
    frame1 = Frame(root, borderwidth=2, relief='ridge')  
    frame2 = Frame(root, borderwidth=2, relief='ridge')  
    frame3 = Frame(root, borderwidth=2, relief='ridge')
    frame4 = Frame(root, borderwidth=0, relief='ridge')
    frame5 = Frame(root, borderwidth=0, relief='ridge')
    frame6 = Frame(root, borderwidth=0, relief='ridge')
     
    frame1.grid(column=0, row=0, sticky="nsew")  
    frame2.grid(column=0, row=1, sticky="nsew")  
    frame3.grid(column=0, row=2, sticky="nsew")
    frame4.grid(column=1, row=0, sticky="nsew")
    frame5.grid(column=2, row=0, sticky="nsew")
    frame6.grid(column=2, row=1, sticky="nsew")

    folder_path = StringVar()
    home = Button(frame1, text="HOME",width=15, command=youtubelink)  
    playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
    about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
    Label(frame4, text=" select song         ").pack()
    choose = Button(frame5, text="choose", command=browse_button)
     
    home.pack(fill='x')  
    playlist.pack(fill='x')  
    about.pack(fill='x')
    choose.pack()

# function for song download by name
def downloadname(songName):
    musicname="spotdl --song \"allen walker - faded\""
    os.system(musicname)

# function for song downloading
def downloadlink(songLink):
    musiclink="spotdl -s https://www.youtube.com/watch?v=dfnCAmr569k"
    os.system(musiclink)

# function for song downlaod by file
def downloadfile(filetxt):
    txtfile="spotdl --list "+filetxt.get()
    os.system(txtfile)

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

if __name__ == '__main__':
    songnamee()
    downloadlink()

