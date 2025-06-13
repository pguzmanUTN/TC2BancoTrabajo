#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 04:13:50 2025

@author: Pedrito
"""

###Lineas que tengo que agregar para que funcione
#import sys
#sys.path.append('/home/pedro/UTN/MATERIAS/2025/TC2/TC2Virtual/lib/python3.12/site-packages')

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
#import math
# Librería de TC2, esta la vas a usar mucho
from pytc2.general import print_latex
from pytc2.sistemas_lineales import analyze_sys, bodePlot, pzmap, pretty_print_bicuad_omegayq
a=1.2526
b=1.2526
c=1.569





def butterworth_max_planicidad(alfa_max, alfa_min, wp, ws):
    # Convertir atenuaciones en dB a escala lineal
    ep2 = 10**(alfa_max / 10) - 1
    A2 = 10**(alfa_min / 10) - 1
    ep=np.sqrt(ep2)
    # Calcular el orden mínimo del filtro
    n = np.ceil(np.log10(A2 / ep2) / (2 * np.log10(ws / wp))).astype(int)

    # Diseñar el filtro
    b, a = signal.butter(N=n, Wn=wp*(ep**(-1/n)), btype='low', analog=True)

    # Mostrar la función de transferencia
    H = signal.TransferFunction(b, a)
    print(f"Orden del filtro: {n}")
    print("Numerador:", H.num)
    print("Denominador:", H.den)

    return H

# Ejemplo: alfa_max = 1 dB, alfa_min = 40 dB, wp = 1 rad/s, ws = 2 rad/s
H = butterworth_max_planicidad(1, 12, 1, 2)






# Definición de la función de transferencia
numerador1 = [a] 
denominador1 = [1,a]  
numerador2 = [c] 
denominador2 = [1,b,c]  
my_tf = TransferFunction( np.polymul(numerador1,numerador2), np.polymul(denominador1,denominador2))




# Define el rango de frecuencias para la simulación
frecuencias = np.logspace(-3, 3, 500)   

# Calcular la respuesta en frecuencia
w, mag, fase = signal.bode(my_tf, frecuencias)
w2, mag2, fase2 = signal.bode(H, frecuencias)

# Graficar la magnitud
plt.figure(figsize=(10, 6))

# Magnitud (en dB)
plt.subplot(2, 1, 1)
plt.semilogx(w, 10**(mag/20),label='my_tf')  
plt.semilogx(w2, 10**(mag2/20), color='red',linestyle='--',label='H(s)')
plt.title('Respuesta en Magnitud y Fase de la Transferencia')
plt.legend(loc='best')
plt.ylabel('Modulo (Amplitud)')
plt.grid()

# Fase
plt.subplot(2, 1, 2)
plt.semilogx(w, fase,label='my_tf')
plt.semilogx(w2, fase2, color='red',linestyle='--',label='H(s)') 
plt.legend(loc='best')
plt.xlabel('Frecuencia (rad/s)')
plt.ylabel('Fase (grados)')
plt.grid()



plt.show()

plt.close('all')

pzmap(my_tf,annotations=False ,fig_id=2) #S plane pole/zero plot
pzmap(H,annotations=False ,fig_id=1) #S plane pole/zero plot


