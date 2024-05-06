from pytube import YouTube

def descargar_video_youtube(url):
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()

# Usar la función
descargar_video_youtube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')