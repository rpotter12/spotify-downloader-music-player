from tkinter import *
import os
from tkinter import filedialog

root = None
active_window = None

# Function to close previous window
def new_window(root):
    global active_window
    if active_window is not None:
        active_window.destroy()
    active_window = Tk()
    return active_window

# Function for song name
def songnamee():
    root2 = new_window(root)
    root2.title('spotify-downloader-music-player')

    # Set the configuration of GUI window  
    root2.geometry("600x175") 

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
    frame5.grid(column=2, row=0, sticky="nsew")
    frame6.grid(column=3, row=1, sticky="nsew")

    menu = Menu(root2) 
    root2.config(menu=menu) 
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
     
    home.pack(fill='x')  
    playlist.pack(fill='x')  
    about.pack(fill='x')
    songName.pack()
    download.pack()
     
    root2.mainloop() 

# Function for youtube link button
def youtubelink():
    root2 = new_window(root)
    root2.title('spotify-downloader-music-player')

    # Set the configuration of GUI window  
    root2.geometry("600x175") 

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
    frame5.grid(column=2, row=0, sticky="nsew")
    frame6.grid(column=3, row=1, sticky="nsew")

    menu = Menu(root2) 
    root2.config(menu=menu) 
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
     
    root2.mainloop() 

# Function for file button
def file():
    root2 = new_window(root)
    root2.title('spotify-downloader-music-player')

    # Set the configuration of GUI window  
    root2.geometry("600x175") 

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
    frame5.grid(column=2, row=0, sticky="nsew")
    frame6.grid(column=3, row=1, sticky="nsew")

    menu = Menu(root2) 
    root2.config(menu=menu) 
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
     
    root2.mainloop() 

# Function for about button
def aboutbackground():
    root2 = new_window(root)
    root2.title('spotify-downloader-music-player')

    # Set the configuration of GUI window  
    root2.geometry("600x175") 

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
     
    home = Button(frame1, text="HOME",width=15, command=youtubelink)  
    playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
    about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
    Label(frame4, text="A GUI version of spotify-downloder of Ritiek Malhotra.").pack()
    Label(frame5, text="It can download music from YouTube in MP3 format and can play them.").pack()
    Label(frame6, text="It can download songs directly by typing name or typing the link.").pack()
     
    home.pack(fill='x')  
    playlist.pack(fill='x')  
    about.pack(fill='x')
     
    root2.mainloop() 

# Function for playlist button
def playlistbackground():
    root2 = new_window(root)
    root2.title('spotify-downloader-music-player')

    # Set the configuration of GUI window  
    root2.geometry("600x175") 

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
     
    root2.mainloop() 

# function for song download by name
def downloadname(songName):
    musicname="spotdl --song \""+songName.get()+"\""
    os.system(musicname)

# function for song downloading
def downloadlink(songLink):
    musiclink="spotdl -s "+songLink.get()
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
