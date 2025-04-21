#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 03:52:46 2025

@author: pedro
"""

###Lineas que tengo que agregar para que funcione
import sys
sys.path.append('/home/pedro/UTN/MATERIAS/2025/TC2/TC2Virtual/lib/python3.12/site-packages')



import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import s, w
from sympy.physics.control.lti import TransferFunction



num = s - 1
den = s + 1
H = TransferFunction(num, den, s) #Define la funcion transferencia

ceros = sp.solveset(num, s, domain=sp.S.Complexes) #Encuentra los 0 del numerador
polos = sp.solveset(den, s, domain=sp.S.Complexes) #Encuentra los 0 del denominador

ceros_val = [c.evalf() for c in ceros]
polos_val = [p.evalf() for p in polos] #Convierte los valores simbolicos a numericos


plt.figure(figsize=(6, 6))


plt.scatter([sp.re(c) for c in ceros_val], [sp.im(c) for c in ceros_val], 
            marker='o', color='b', label='Ceros') #Ubica los 0 desde su parte real
#Y parte imaginaria

plt.scatter([sp.re(p) for p in polos_val], [sp.im(p) for p in polos_val], 
            marker='x', color='r', label='Polos') #Ubica los polos desde su parte real
#E  Imaginaria

plt.axhline(0, color='k', linewidth=1) 
plt.axvline(0, color='k', linewidth=1) #Marca los ejes
#Le tuve que poner color porque por alguna razon el valor DEFAULT de color
# de los ejes es azul.
plt.grid() #Activa la grilla
plt.xlabel("Re(s)")
plt.ylabel("Im(s)")
plt.legend()
plt.title("Diagrama de Polos y Ceros")


Hjw = H.to_expr().subs(s, sp.I * w)  # Reemplaza s por jω
w_vals = np.logspace(-2, 2, 1000)  # Frecuencia de 0.01 a 100 rad/s

# Convierte a expresion numerica
Hjw_func = sp.lambdify(w, Hjw, "numpy")
#Evalua la funcion con los valores de w_vals
Hjw_vals = Hjw_func(w_vals)

# Obtiene modulo y fase
modulo_vals = np.abs(Hjw_vals)  # Módulo |H(jw)|
fase_vals = np.angle(Hjw_vals, deg=True)  # Fase en grados

plt.figure(figsize=(10, 5))

# Módulo en amplitud
plt.subplot(2, 1, 1)
plt.semilogx(w_vals, modulo_vals)  # Escala logarítmica en frecuencia
plt.grid()
plt.ylabel("|H(jω)| (Amplitud)")
plt.title("Módulo (Amplitud) y Fase")

# Fase (grados)
plt.subplot(2, 1, 2)
plt.semilogx(w_vals, fase_vals)
plt.grid()
plt.ylabel("Fase [°]")
plt.xlabel("Frecuencia [rad/s]")

plt.show()
