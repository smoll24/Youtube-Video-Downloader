# Importation des modules utiles
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
#PyTube error, make sure to fix before using: https://github.com/pytube/pytube/issues/1498
#Modify {home}/.local/lib/python3.7/site-packages/pytube/cipher.py, line 411, to 'transform_plan_raw = js'

# Définition des fonctions
def download_video():
    """Download la video youtube

    Arguments:
    None
    
    Return :
    None
    """
    
    #Gets link inputted
    link = champSaisie_link.get()
    
    #Gets path to download at
    path = champSaisie_path.get()
    
    try:
        yt = YouTube(link)
        
        # Get all video streams for the YouTube video
        streams = yt.streams
        
        # Create a list of available video formats for the YouTube video
        video_formats = [f"{s.resolution} {s.fps}fps {s.mime_type}" for s in streams if s.mime_type.startswith("video/")]
        
        # Show a dropdown menu of available video formats
        selected_format = tk.StringVar()
        selected_format.set("Choose Video Format")
        menu = tk.OptionMenu(fenetre, selected_format, *video_formats)
        menu.grid(row=5, column=0, columnspan=3, padx=6, pady=6, ipadx=5)

        # Wait for the user to select a video format from the dropdown menu
        fenetre.wait_variable(selected_format)
        
        # Find the stream that matches the selected video format
        selected_format = selected_format.get()
        print(selected_format)
        stream = next((s for s in streams if f"{s.resolution} {s.fps}fps {s.mime_type}" == selected_format), None)
        print(stream)
        
        menu.destroy()
        
        def on_download_click():
            # Download the video stream
            stream.download(output_path=path)
            if path != "":
                video_path = f"{path}/{stream.default_filename}"
            else:
                video_path = stream.default_filename
        
            video_download_button.destroy()
            
            # Open the downloaded file using the default application for the file type
            os.startfile(video_path)
        
        if stream is not None:
            video_download_button = tk.Button(fenetre, text='Download Video', fg="white", bg="green", command=on_download_click)
            video_download_button.grid(row=5, column=0, columnspan=3, padx=6, pady=6, ipadx=5)
        
        else:
            messagebox.showerror(title='Error', message="Could not find a matching video stream.")
        
    except Exception as e:
        messagebox.showerror(title='Error', message=str(e))
        print (e)


        
def download_audio():
    """Download l'audio de la video youtube

    Arguments:
    None
    
    Return:
    None
    """
    
    #Gets link inputted
    link = champSaisie_link.get()
    
    #Gets path to download at
    path = champSaisie_path.get()
    
    try:
        yt = YouTube(link)
        
        # Get all audio streams for the YouTube video
        audio_streams = yt.streams.filter(only_audio=True)
        
        # Create a list of available audio formats for the YouTube video
        audio_formats = [f"{s.abr}kbps {s.mime_type}" for s in audio_streams]
        
        # Show a dropdown menu of available audio formats
        selected_format = tk.StringVar()
        selected_format.set("Choose Audio Format")
        menu = tk.OptionMenu(fenetre, selected_format, *audio_formats)
        menu.grid(row=9, column=0, columnspan=3, padx=6, pady=6, ipadx=5)
        
        # Wait for the user to select an audio format from the dropdown menu
        fenetre.wait_variable(selected_format)
        
        # Find the stream that matches the selected audio format
        selected_format = selected_format.get()
        print(selected_format)
        stream = next((s for s in audio_streams if f"{s.abr}kbps {s.mime_type}" == selected_format), None)
        print(stream)
        
        menu.destroy()
        
        def on_download_click():
            # Download the audio stream
            stream.download(output_path=path)
            if path != "":
                audio_path = f"{path}/{stream.default_filename}"
            else:
                audio_path = stream.default_filename
            
            audio_download_button.destroy()
            
            # Open the downloaded file using the default application for the file type
            os.startfile(audio_path)
            
        
        if stream is not None:
            audio_download_button = tk.Button(fenetre, text='Download Audio', fg="white", bg="green", command=on_download_click)
            audio_download_button.grid(row=9, column=0, columnspan=3, padx=6, pady=6, ipadx=5)
        
        else:
            messagebox.showerror(title='Error', message="Could not find a matching audio stream.")
        
    except Exception as e:
        messagebox.showerror(title='Error', message=str(e))
        print(e)
        

# Création de la fenêtre tkinter

root = tk.Tk()
root.geometry('400x320')
root.title('Youtube Video Downloader')
root.configure(background='#e4e4e4')

fenetre = tk.Frame(root)
fenetre.pack()
fenetre.configure(background='#e4e4e4')

# Création des boutons

bouton_quitter = tk.Button(fenetre, text='Quit', command=root.destroy)
bouton_quitter.grid(row=13, column=0, columnspan=3, padx=6, pady=6, ipadx=5)

bouton_video = tk.Button(fenetre, text='Get Video', command=download_video)
bouton_video.grid(row=4, column=0, columnspan=3, padx=6, pady=6, ipadx=5)

bouton_audio = tk.Button(fenetre, text='Get Audio', command=download_audio)
bouton_audio.grid(row=8, column=0, columnspan=3, padx=6, pady=6, ipadx=5)

# Création des zones de texte

entete = tk.Label(fenetre, text="Youtube Video Downloader",
                  font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4')
entete.grid(row=0, column=0, columnspan=3, padx=6, pady=6, ipadx=5)

link_label = tk.Label(fenetre, text='Link :')
link_label.grid(row=1, column=0)

path_label = tk.Label(fenetre, text='Path :')
path_label.grid(row=2, column=0)

# Création du champ de saisie

champSaisie_link = tk.Entry(fenetre, font=('Arial', 10), width=35)
champSaisie_link.grid(row=1, column=1, columnspan=2, padx=6, pady=6, ipadx=5)

champSaisie_path = tk.Entry(fenetre, font=('Arial', 10), width=35)
champSaisie_path.grid(row=2, column=1, columnspan=2, padx=6, pady=6, ipadx=5)

# Programme principal

fenetre.mainloop()    # Boucle d'attente des événements
