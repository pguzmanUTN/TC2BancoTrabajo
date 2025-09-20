import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Parámetros
fs = 1000       # Frecuencia de muestreo [Hz]
f = 5           # Frecuencia de la señal [Hz]
N = 500         # Cantidad de muestras
n = np.arange(N)
t = n / fs

# Señal de entrada
x = np.sin(2 * np.pi * f * t)

# Derivada discreta teórica: (2πf/fs)*cos(...)
x_deriv = (2 * np.pi * f) /fs * np.cos(2 * np.pi * f * t)

# Filtro diferenciador: H(z) = 1/2 * (1 - z^-2)
b = [0.5, 0, -0.5]  # Coeficientes del numerador
a = [1]             # Denominador (FIR)
y = lfilter(b, a, x)

x_diff = np.diff(x)
t_diff = t[:-1]           

# Gráficos
plt.figure(figsize=(10,6))

plt.plot(t, x, label="Señal de entrada x[n] (seno)", color="blue")
plt.plot(t, x_deriv, label="Derivada discreta teórica", color="red", linestyle="--")
plt.plot(t, y, label="Salida del filtro diferenciador", color="green")
plt.plot(t_diff, x_diff, label="Derivada con np.diff", color="magenta", alpha=0.7)

plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.title("Filtro diferenciador vs derivadas")
plt.legend()
plt.grid(True)
plt.show()
