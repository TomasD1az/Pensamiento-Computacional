#!/usr/bin/env python3
"""
Script para verificar la instalación.
"""

# Importamos librerías
import PyWave
from PIL import Image, ImageDraw


# Insertar acá su nombre completo
STUDENT_NAME = "Tomas Diaz"
PATH = "test.wav"


def main():
    
    # Abrimos el archivo .wav
    wf = PyWave.open(PATH)
    
    # Imprimimos en consola información relevante
    print("This WAVE file has the following properties:")
    print(wf.channels, "channel/s")
    print(wf.frequency, "Hz sample rate")
    print(wf.bitrate, "bits per second")
    print(wf.samples, "total samples")
    
    # Creamos imagen
    img = Image.new('RGB', (400, 130), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Imprimimos en la imagen la información relevante
    draw.text((5, 10), STUDENT_NAME, (0,0,0))
    draw.text((5, 30), "This WAVE file has the following properties:", (0,0,0))
    draw.text((5, 50), "{} channel/s".format(wf.channels), (0,0,0))
    draw.text((5, 70), "{} Hz sample rate".format(wf.frequency), (0,0,0))
    draw.text((5, 90), "{} bits per second".format(wf.bitrate), (0,0,0))
    draw.text((5, 110), "{} total samples".format(wf.samples), (0,0,0))
    img.save('val_pywave.png')

    # Cerramos el archivo .wav
    wf.close()


if __name__ == '__main__':
    # Ejecutamos el código 
    main()
    