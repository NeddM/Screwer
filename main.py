import os
from pydub import AudioSegment
import youtube_dl


def directorios():
    ruta = os.getcwd()
    rutaMusica = os.listdir(ruta)

    return ruta, rutaMusica


def separarNombreyExtension(filename):
    sname = ""
    sext = ""
    i = filename.rfind(".")
    if (i != 0):
        n = len(filename)
        j = n-i-1
        sname = filename[0:i]
        sext = filename[-j:]

    return sname, sext


def descargar_audio_youtube(archivo_enlaces):
    with open(archivo_enlaces, 'r') as f:
        for enlace in f:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }]
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([enlace])


def ralentizaAudio(ruta, rutaMusica):
    for archivo in rutaMusica:
        if archivo.endswith(".mp3"):

            audio = AudioSegment.from_file(archivo)
            octavas = -0.3

            nuevoSampleRate = int(audio.frame_rate * (2.0 ** octavas))
            audio = audio._spawn(audio.raw_data, overrides={
                'frame_rate': nuevoSampleRate})

            nombreNuevo, extension = separarNombreyExtension(archivo)

            audio.export(
                f"{ruta}/Procesado/{nombreNuevo} - SLOWED by pyScrewer.{extension}", format="mp3")

    print("¡Archivos exportados exitosamente!")


def borrarBasura(ruta):
    musicaResiduo = os.listdir(ruta)

    for archivo in musicaResiduo:
        rutaCompleta = os.path.join(ruta, archivo)

        if rutaCompleta.endswith('.mp3'):
            os.remove(rutaCompleta)


def main():
    enlacesDeYoutube = "Enlaces.txt"
    descargar_audio_youtube(enlacesDeYoutube)
    ruta, rutaMusica = directorios()
    ralentizaAudio(ruta, rutaMusica)
    borrarBasura(ruta)


if "__main__" == __name__:
    main()
