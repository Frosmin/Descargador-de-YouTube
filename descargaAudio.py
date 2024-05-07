# from pytube import YouTube


# def descargar_audio_youtube(url):
#     youtube = YouTube(url)
#     audio = youtube.streams.get_audio_only()
#     print("iniciando descarga...")
#     audio.download()
   
    

# url = "https://www.youtube.com/watch?v=blgwRBtWqbA&list=RDblgwRBtWqbA&start_radio=1"
# descargar_audio_youtube(url)
# print("Descarga completada")


# from pytube import YouTube
# from moviepy.editor import AudioFileClip

# def descargar_audio_youtube(url):
#     youtube = YouTube(url)
#     video = youtube.streams.get_highest_resolution()
#     video.download(filename="temp")
#     print("Video descargado, extrayendo audio...")
    
#     videoclip = AudioFileClip("temp.mp4")
#     audioclip = videoclip.audio
#     audioclip.write_audiofile("audio.mp3")
#     print("Audio extraído.")

# # Usar la función
# url = "https://www.youtube.com/watch?v=blgwRBtWqbA&list=RDblgwRBtWqbA&start_radio=1"
# descargar_audio_youtube(url)



from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def descargar_audio_youtube(url):
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download(output_path=".", filename="temp")
    print("Video descargado, extrayendo audio...")
    
    if os.path.exists("./temp.mp4"):
        videoclip = AudioFileClip("./temp.mp4")
        audioclip = videoclip.audio
        audioclip.write_audiofile("audio.mp3")
        print("Audio extraído.")
    else:
        print("El archivo temp.mp4 no se encontró.")

# Usar la función
url = "https://www.youtube.com/watch?v=blgwRBtWqbA&list=RDblgwRBtWqbA&start_radio=1"
descargar_audio_youtube(url)