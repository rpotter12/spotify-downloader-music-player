from tkinter import *
import os

root = None
active_window = None

def new_window(root):
    global active_window
    if active_window is not None:
        active_window.destroy()
    active_window = Tk()
    return active_window

def homebackground():
    root2 = new_window(root)
    root2.title('spotify-downloader-music-player')

    frame1 = Frame(root, borderwidth=2, relief='ridge')  
    frame2 = Frame(root, borderwidth=2, relief='ridge')  
    frame3 = Frame(root, borderwidth=2, relief='ridge')
    frame4 = Frame(root, borderwidth=0, relief='ridge')
    frame5 = Frame(root, borderwidth=0, relief='ridge')

    frame1 = Frame(root2, borderwidth=2, relief='ridge')  
    frame2 = Frame(root2, borderwidth=2, relief='ridge')  
    frame3 = Frame(root2, borderwidth=2, relief='ridge')
    frame4 = Frame(root2, borderwidth=0, relief='ridge')
    frame5 = Frame(root2, borderwidth=0, relief='ridge')
     
    frame1.grid(column=0, row=0, sticky="nsew")  
    frame2.grid(column=0, row=1, sticky="nsew")  
    frame3.grid(column=0, row=2, sticky="nsew")
    frame4.grid(column=1, row=0, sticky="nsew")
    frame5.grid(column=2, row=0, sticky="nsew")
     
    home = Button(frame1, text="HOME",width=15, command=homebackground)  
    playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
    about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
    songName = Entry(frame4, width=40)
    download = Button(frame5, text="Download", command=lambda: downloadsong(songName))
     
    home.pack(fill='x')  
    playlist.pack(fill='x')  
    about.pack(fill='x')
    songName.pack()
    download.pack()
     
    root2.mainloop() 

def aboutbackground():
    root2 = new_window(root)
    root2.title('spotify-downloader-music-player')

    frame1 = Frame(root, borderwidth=2, relief='ridge')  
    frame2 = Frame(root, borderwidth=2, relief='ridge')  
    frame3 = Frame(root, borderwidth=2, relief='ridge')
    frame4 = Frame(root, borderwidth=0, relief='ridge')
    frame5 = Frame(root, borderwidth=0, relief='ridge')
    frame6 = Frame(root, borderwidth=0, relief='ridge')

    frame1 = Frame(root2, borderwidth=2, relief='ridge')  
    frame2 = Frame(root2, borderwidth=2, relief='ridge')  
    frame3 = Frame(root2, borderwidth=2, relief='ridge')
    frame4 = Frame(root2, borderwidth=0, relief='ridge')
    frame5 = Frame(root2, borderwidth=0, relief='ridge')
    frame6 = Frame(root2, borderwidth=0, relief='ridge')
     
    frame1.grid(column=0, row=0, sticky="nsew")  
    frame2.grid(column=0, row=1, sticky="nsew")  
    frame3.grid(column=0, row=2, sticky="nsew")
    frame4.grid(column=1, row=0, sticky="nsew")
    frame5.grid(column=1, row=1, sticky="nsew")
    frame6.grid(column=1, row=2, sticky="nsew")
     
    home = Button(frame1, text="HOME",width=15, command=homebackground)  
    playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
    about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
    Label(frame4, text="A GUI version of spotify-downloder of Ritiek Malhotra.").pack()
    Label(frame5, text="It can download music from YouTube in MP3 format and can play them.").pack()
    Label(frame6, text="It can download songs directly by typing name or typing the link.").pack()
     
    home.pack(fill='x')  
    playlist.pack(fill='x')  
    about.pack(fill='x')
     
    root2.mainloop() 

def playlistbackground():
    root2 = new_window(root)
    root2.title('spotify-downloader-music-player')

    frame1 = Frame(root, borderwidth=2, relief='ridge')  
    frame2 = Frame(root, borderwidth=2, relief='ridge')  
    frame3 = Frame(root, borderwidth=2, relief='ridge')
    frame4 = Frame(root, borderwidth=0, relief='ridge')
    frame5 = Frame(root, borderwidth=0, relief='ridge')
    frame6 = Frame(root, borderwidth=0, relief='ridge')

    frame1 = Frame(root2, borderwidth=2, relief='ridge')  
    frame2 = Frame(root2, borderwidth=2, relief='ridge')  
    frame3 = Frame(root2, borderwidth=2, relief='ridge')
    frame4 = Frame(root2, borderwidth=0, relief='ridge')
    frame5 = Frame(root2, borderwidth=0, relief='ridge')
    frame6 = Frame(root2, borderwidth=0, relief='ridge')
     
    frame1.grid(column=0, row=0, sticky="nsew")  
    frame2.grid(column=0, row=1, sticky="nsew")  
    frame3.grid(column=0, row=2, sticky="nsew")
    frame4.grid(column=1, row=0, sticky="nsew")
    frame5.grid(column=1, row=1, sticky="nsew")
    frame6.grid(column=2, row=1, sticky="nsew")

    folder_path = StringVar()
    home = Button(frame1, text="HOME",width=15, command=homebackground)  
    playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
    about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
    Label(frame4, text=folder_path).pack()
    choose = Button(frame5, text="choose", command=browse_button)
     
    home.pack(fill='x')  
    playlist.pack(fill='x')  
    about.pack(fill='x')
    choose.pack()
     
    root2.mainloop() 

def downloadsong(songName):
    musiclink="spotdl -s "+songName.get()
    os.system(musiclink)

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

if __name__ == '__main__':
    homebackground()
