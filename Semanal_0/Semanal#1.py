#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 04:13:50 2025

@author: Pedrito
"""

###Lineas que tengo que agregar para que funcione
import sys
sys.path.append('/home/pedro/UTN/MATERIAS/2025/TC2/TC2Virtual/lib/python3.12/site-packages')

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np

# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap
w0=2*3.1415*10000
wz=R5=1000
Cn=10e-9*w0*wz
Cn2=10e-9*w0*wz
Rn4=Rn1=9000/wz
Rn=31830/wz
Rn3=2533/wz


R4=R1=Rn1*wz
R3=Rn3*wz
R=Rn*wz
C=Cn/(wz*w0)
C2=Cn2/(wz*w0)



# Definición de la función de transferencia (s-1)/(s+1)
numerador = [(1+Rn4)*(1/(Rn*Cn)) , 0]  # Coeficientes de s-1
denominador = [1, 1/(Rn*Cn), Rn4/(Rn1*Rn3*Cn*Cn2)]  # Coeficientes de s+1

# Crear la función de transferencia
my_tf = TransferFunction( numerador, denominador)

# Define el rango de frecuencias para la simulación
frecuencias = np.logspace(-3, 3, 500)  # Rango de frecuencias de 0.01 a 100 rad/s con 500 puntos

# Calcular la respuesta en frecuencia
w, mag, fase = signal.bode(my_tf, frecuencias)

# Graficar la magnitud
plt.figure(figsize=(10, 6))

# Magnitud (en amplitud, no en dB)
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)  #Convierte dB en veces
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

# Definición de la función de transferencia (s-1)/(s+1)
numerador = [(1+R4/R5)*(1/(R*C)) , 0]  # Coeficientes de s-1
denominador = [1, 1/(R*C), R4/(R1*R3*R5*C*C2)]  # Coeficientes de s+1

# Crear la función de transferencia
my_tf = TransferFunction( numerador, denominador)

# Define el rango de frecuencias para la simulación
frecuencias = np.logspace(0, 6, 500)  # Rango de frecuencias de 0.01 a 100 rad/s con 500 puntos

# Calcular la respuesta en frecuencia
w, mag, fase = signal.bode(my_tf, frecuencias)

# Graficar la magnitud
plt.figure(figsize=(10, 6))

# Magnitud (en amplitud, no en dB)
plt.subplot(2, 1, 1)
plt.semilogx(w/(2*3.1416), mag)  #Convierte dB en veces
plt.title('Respuesta en Magnitud y Fase de la Transferencia')
plt.ylabel('Modulo (Amplitud)')
plt.grid()

# Fase
plt.subplot(2, 1, 2)
plt.semilogx(w/(2*3.1416), fase)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Fase (grados)')
plt.grid()



plt.show()

plt.close('all')

pzmap(my_tf, fig_id=2) #S plane pole/zero plot


