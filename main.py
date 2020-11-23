# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting

# Press the green button in the gutter to run the script.

from scipy import fftpack as f

import numpy as np
import os
if __name__ == '__main__':



        prueba=int(input("Introduce un numero de la opción que quieres ejecutar:\n"
                         "1-Cortar 10 segundos de vídeo\n"
                         "2 Extraer histograma YUV vídeo y crear nuevo vídeo con el histograma\n"
                         "3-Cambiar calidad de vídeo\n"
                         "4-Cambiar a mono audio:\n"))


        if(prueba==1):
                archivo_input=input("Introduce el directorio del vídeo");
                archivo_output=input("Introduce el directorio donde quieras que guarde el archivo y su nombre");
                os.system("ffmpeg -ss 00:01:00.0 -i " +archivo_input+ " -c copy -t 00:00:05.0 1"+archivo_output+"");
        if(prueba==2):
                archivo_input = input("Introduce el directorio del vídeo");
                archivo_output = input("Introduce el directorio donde quieras que guarde el archivo y su nombre");
                os.system("ffmpeg -i " +archivo_input+ " -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay " +archivo_output+"");
        if(prueba==3):
                archivo_input = input("Introduce el directorio del vídeo");
                archivo_output = input("Introduce el directorio donde quieras que guarde el archivo y su nombre");
                resolucion = input("Introduce la nueva resolución en formato Numero-Numero");
                os.system("ffmpeg -i " + archivo_input + " -filter:v scale="+resolucion+" -acodec copy " + archivo_output + "");
        if(prueba==4):
                archivo_input = input("Introduce el directorio del vídeo");
                archivo_output = input("Introduce el directorio donde quieras que guarde el archivo y su nombre");
                os.system("ffmpeg -i " +archivo_input+ " -ac 1 " +archivo_output+ "");
        if(prueba>4):
                print("Opción no válida");


        


        # See PyCharm help at https://www.jetbrains.com/help/pycharm/
