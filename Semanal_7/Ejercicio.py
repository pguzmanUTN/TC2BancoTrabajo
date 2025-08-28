#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 11:40:23 2025

@author: mariano

Ejemplo de análisis de red doble Tee RC en configuración notch y verificación 
via MAI y cuadripolos.
"""

import sympy as sp

from pytc2.cuadripolos import calc_MAI_vtransf_ij_mn
from pytc2.general import print_latex, s, print_subtitle, a_equal_b_latex_s


L, C = sp.symbols('L, C', complex=False)
# G = sp.symbols('G', real=True, positive=True)

# Armo la MAI

print_subtitle('Análisis via matriz admitancia indefinida')

#               Nodos: 0         1         2           3         
Ymai = sp.Matrix([  
   [ 1/(s*L)-((1/(s*L))**2)*1/(2/(s*L)+s*C),     -((1/(s*L))**2)*1/(2/(s*L)+s*C),            -(C/L)*1/(2/(s*L)+s*C)],
   [ -((1/(s*L))**2)*1/(2/(s*L)+s*C),            1/(s*L)-((1/(s*L))**2)*1/(2/(s*L)+s*C),     -(C/L)*1/(2/(s*L)+s*C)],
   [ -(C/L)*1/(2/(s*L)+s*C),                    -(C/L)*1/(2/(s*L)+s*C),                       s*C-((s**2)*(C**2))/(2/(s*L)+s*C)],
                 ])

print_latex( a_equal_b_latex_s('Y_{MAI}', Ymai ))

subs_dict = {L:1, C:1}

con_detalles = False
# con_detalles = True


# Calculo la Z en el puerto de entrada a partir de la MAI


V2313 = calc_MAI_vtransf_ij_mn(Ymai, ii=2-1, jj=3-1,mm=1-1,nn=3-1, verbose=con_detalles)


print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(2-1, 3-1, 1-1, 3-1) +  sp.latex(V2313) + ' = ' + sp.latex(V2313.subs(subs_dict)) )



V2313 = calc_MAI_vtransf_ij_mn(Ymai, ii=2-1, jj=3-1,mm=1-1,nn=3-1, verbose=con_detalles)


print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(2, 3, 1, 3) +  sp.latex(V2313) + ' = ' + sp.latex(V2313.subs(subs_dict)) )



V2131 = calc_MAI_vtransf_ij_mn(Ymai, ii=2-1, jj=1-1,mm=3-1,nn=1-1, verbose=con_detalles)


print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(2, 1, 3, 1) +  sp.latex(V2131) + ' = ' + sp.latex(V2131.subs(subs_dict)) )

V1232 = calc_MAI_vtransf_ij_mn(Ymai, ii=1-1, jj=2-1,mm=3-1,nn=2-1, verbose=con_detalles)


print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(1, 2, 3, 2) +  sp.latex(V1232) + ' = ' + sp.latex(V1232.subs(subs_dict)) )




