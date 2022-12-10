```art
                                __________                               .___
                    ______ ___.__.\______   \__ _______________   ____   __| _/
                    \____ <   |  | |     ___/  |  \_  __ \____ \_/ __ \ / __ |
                    |  |_> >___  | |    |   |  |  /|  | \/  |_> >  ___// /_/ |
                    |   __// ____| |____|   |____/ |__|  |   __/ \___  >____ |
                    |__|   \/                            |__|        \/     \/
```

# Historia

Para empezar, viene bien conocer lo que es la música [**Chopped and Screwed**](https://es.wikipedia.org/wiki/Chopped_and_screwed), género creado por [Dj Screw](https://en.wikipedia.org/wiki/DJ_Screw) en Houston, Tejas, en la década de los 90, y que se basa en ralentizar canciones.
La gente se dió cuenta de que se puede disfrutar mucho mejor la música cuando está ralentizada. De esta manera se aprecian mucho más los tonos, la letra, y la música en general.

![Dj Screw](/img/DJ-Screw-1.jpg)

Es un género muy extendido por todo el mundo, sobre todo por Estados Unidos, y también es un recurso que los artistas usan actualmente como un recurso musical, para por ejemplo terminar canciones.

Este género también es llamado de otras maneras, como _Slowed and reverb_ o _Slowed and purped_.

Por ello he decidido bautizar este script con el nombre de **pyPurped**, por Python y por el género.

# Sobre el script

El script básicamente descarga canciones de YouTube, las ralentiza y te las exporta. ¡Listas para escuchar!

# Uso del script

Para empezar, necesitas tener instalado `Python3`.

También necesitarás algunas dependencias:

```python
pip install AudioSegment
pip install youtube_dl
```

Clona este repositorio, y abrelo.
Dentro de la carpeta del script hay un archivo llamado **Enlaces.txt**, ahí es donde debes poner los enlaces de YouTube, de manera sucesiva, sin saltar lineas. Un ejemplo:

```
https://youtu.be/ockzzfKbFOE
https://youtu.be/IWBDbXnn_Gs
https://youtu.be/effbcOytzXk
https://youtu.be/v6Vovj1xZSw
https://youtu.be/rpaonSDPw7Y
https://youtu.be/L8aIUhkeoxI
```

`¡También puedes poner el enlace de una playlist!`

Una vez tienes los enlaces guardados en el achivo **Enlaces.txt**, ya podemos ejecutar el script, de la siguiente forma:

```bash
python3 main.py
```

Cuando el script se haya ejecutado, luego tendrás una carpeta llamada `Procesado`, dentro de la carpeta del script.

Dentro de la carpeta `Procesado`estarán las canciones ralentizadas.
