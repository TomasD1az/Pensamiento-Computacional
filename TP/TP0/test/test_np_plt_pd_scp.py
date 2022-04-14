#!/usr/bin/env python3
"""
Script para verificar la instalación.
"""

# Importamos librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter as sg_filter


# Insertar acá su nombre completo
STUDENT_NAME = "Tomas Diaz"


def main():
    
    # Levantamos los datos del .csv
    direc = r'test_data.csv'
    file = pd.read_csv(direc, sep='\t')
    df_file = pd.DataFrame(file)
    df_file = df_file.iloc[:-6]
    
    # Realizamos un preprocesamiento de los datos
    time = df_file['time'].to_numpy()/1000
    posy = df_file['posy'].to_numpy()
    posy = posy - posy[0] + 0.3
    
    r_posy = posy.copy()
    
    for i in range(len(posy)):
        r_posy[i] += (np.random.rand()-0.5)*0.02
        
    # Suavizamos los datos
    filtered = sg_filter(r_posy, 15, 3)
    
    # Graficamos 
    plt.plot(time, r_posy, linewidth=2, alpha=0.5)
    plt.plot(time, filtered)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Altura [m]')
    plt.legend(['Medición', 'Filtrado'])
    plt.title(STUDENT_NAME)
    plt.savefig('val_np_plt_pd_scp.png')
    plt.show()


if __name__ == '__main__':
    # Ejecutamos el código 
    main()
