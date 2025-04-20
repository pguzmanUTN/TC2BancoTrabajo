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
from pytc2.sistemas_lineales import pzmap

w0=1
Q=1
K=-1


# Definición de la función de transferencia
numerador = [K*w0/Q] 
denominador = [1, w0/Q, w0**2]  

# Crear la función de transferencia
my_tf = TransferFunction( numerador, denominador)

# Define el rango de frecuencias para la simulación
frecuencias = np.logspace(-3, 3, 500)   

# Calcular la respuesta en frecuencia
w, mag, fase = signal.bode(my_tf, frecuencias)

# Graficar la magnitud
plt.figure(figsize=(10, 6))

# Magnitud (en dB)
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)  
plt.title('Respuesta en Magnitud y Fase de la Transferencia')
plt.ylabel('Modulo (Amplitud)')
plt.grid()

# Fase
plt.subplot(2, 1, 2)
plt.semilogx(w, fase)
plt.xlabel('Frecuencia (rad/s)')
plt.ylabel('Fase (grados)')
plt.grid()



plt.show()

plt.close('all')

pzmap(my_tf, fig_id=2) #S plane pole/zero plot


