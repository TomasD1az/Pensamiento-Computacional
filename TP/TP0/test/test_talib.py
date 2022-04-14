#!/usr/bin/env python3
"""
Script para verificar la instalación.
"""

# Importamos librerías
import matplotlib.pyplot as plt
import talib as ta
import yfinance as yf


# Insertar acá su nombre completo
STUDENT_NAME = "Tomas Diaz"


def main():
        
    # Descargamos datos
    aapl = yf.download('AAPL', '2019-1-1','2019-12-27')
    aapl['Simple MA'] = ta.SMA(aapl['Close'],14)
    aapl['EMA'] = ta.EMA(aapl['Close'], timeperiod = 14)
    
    # Graficamos los datos
    aapl[['Close','Simple MA','EMA']].plot(figsize=(15,15))
    # Insertamos el título del gráfico
    plt.title(STUDENT_NAME)
    plt.tight_layout()
    # Guardamos el gráfico
    plt.savefig('val_talib.png')
    plt.show()


if __name__ == '__main__':
    # Ejecutamos el código 
    main()
