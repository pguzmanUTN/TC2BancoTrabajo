import numpy as np
import matplotlib.pyplot as plt

# Parámetro del filtro
beta = 0.9   # podés cambiar a 0.9 o cualquier valor entre 0 y 1

# Vector de frecuencias normalizadas (Ω en radianes)
Omega = np.linspace(0, np.pi, 1000)

# Respuesta en frecuencia H(e^jΩ) = (1 - e^{-jΩ}) / (1 - β e^{-jΩ})
H = (1 - np.exp(-1j * Omega)) / (1 - beta * np.exp(-1j * Omega))

# Módulo y fase
H_mag = np.abs(H)
H_phase = np.angle(H)

# Gráficos
plt.figure(figsize=(12,6))

# Magnitud
plt.subplot(2,1,1)
plt.plot(Omega/np.pi, 20*np.log10(H_mag), color='blue')
plt.title(f"Respuesta en frecuencia del DC-blocker (β = {beta:.4f})")
plt.ylabel("Módulo [dB]")
plt.grid(True)

# Fase
plt.subplot(2,1,2)
plt.plot(Omega/np.pi, H_phase, color='red')
plt.xlabel("Frecuencia Normalizada Ω/π")
plt.ylabel("Fase [rad]")
plt.grid(True)

plt.tight_layout()
plt.show()
