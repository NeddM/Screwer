import os
import subprocess
from time import sleep
from pydub import AudioSegment
import youtube_dl


def directorios():
    ruta = os.getcwd()
    rutaMusica = os.listdir(ruta)

    rutaProcesado = f"{ruta}/Procesado/"
    if not os.path.isdir(rutaProcesado):
        os.makedirs(rutaProcesado)

    return ruta, rutaMusica


def separarNombreyExtension(archivo):
    trozoNombre = ""
    trozoExtension = ""
    i = archivo.rfind(".")
    if (i != 0):
        n = len(archivo)
        j = n-i-1
        trozoNombre = archivo[0:i]
        trozoExtension = archivo[-j:]

    return trozoNombre, trozoExtension


def descargarAudioYoutube(archivo_enlaces):
    i = 1
    with open(archivo_enlaces, 'r') as f:
        for enlace in f:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{i} - %(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }]
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([enlace])
            i += 1
            subprocess.call('youtube-dl --rm-cache-dir', shell=True)
            limpiarPantalla()


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
                f"{ruta}/Procesado/{nombreNuevo} - SLOWED by pyPurped.{extension}", format="mp3")

    limpiarPantalla()
    print("¡Archivos exportados exitosamente!")


def borrarBasura(ruta):
    musicaResiduo = os.listdir(ruta)

    for archivo in musicaResiduo:
        rutaCompleta = os.path.join(ruta, archivo)

        if rutaCompleta.endswith('.mp3'):
            os.remove(rutaCompleta)

    with open("Enlaces.txt", "w") as file:
        file.truncate()


def firma():
    print("""
                __________                               .___
    ______ ___.__.\\______   \\__ _______________   ____   __| _/
    \\____ <   |  | |     ___/  |  \\_  __ \\____ \\_/ __ \\ / __ | 
    |  |_> >___  | |    |   |  |  /|  | \\/  |_> >  ___// /_/ | 
    |   __// ____| |____|   |____/ |__|  |   __/ \\___  >____ | 
    |__|   \\/                            |__|        \\/     \\/ 
                                                            

                    https://github.com/NeddM
    """)

    sleep(4)
    limpiarPantalla()


def limpiarPantalla():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)


def main():
    firma()
    enlacesDeYoutube = "Enlaces.txt"
    descargarAudioYoutube(enlacesDeYoutube)
    ruta, rutaMusica = directorios()
    ralentizaAudio(ruta, rutaMusica)
    borrarBasura(ruta)


if "__main__" == __name__:
    main()
