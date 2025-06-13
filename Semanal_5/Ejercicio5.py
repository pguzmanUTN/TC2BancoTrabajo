from pytc2.sistemas_lineales import analyze_sys, pretty_print_bicuad_omegayq, tf2sos_analog, pretty_print_SOS, pretty_print_lti
import numpy as np
from scipy import signal as sig

this_ripple = 0.5
this_order = 3
Q=5
eps = np.sqrt( 10**(this_ripple/10) - 1 )

z,p,k = sig.cheb1ap(this_order, this_ripple)

num, den = sig.zpk2tf(z,p,k)

# factorizamos en SOS's
this_sos = tf2sos_analog(num, den)


print( 'Transferencia pasa-bajos')
print( '------------------------')

pretty_print_SOS(this_sos, mode='omegayq')

num_bp, den_bp = sig.lp2bp(num, den,bw=(1/Q))

this_sos_bp = tf2sos_analog(num_bp, den_bp)
this_sos_bp2 = sig.tf2sos(num_bp, den_bp,analog=True)

print( 'Transferencia pasa-banda')
print( '------------------------')

pretty_print_SOS(this_sos_bp, mode='omegayq')
pretty_print_SOS(this_sos_bp2, mode='omegayq')
#_ = analyze_sys( this_sos )
pretty_print_lti(num_bp,den_bp)
_ = analyze_sys( this_sos_bp )
_ = analyze_sys( this_sos_bp2, same_figs=False )

print( 'Transferencia pasa-banda Obtenida a mano')
print( '------------------------')

num1 = [0.625/5, 0]

dem1 = [1, 0.625/5 ,1 ]

num2 = [(3*0.0562) , 0]

dem2 = [1, 0.0562 , (0.9034**2) ]

num3 = [(4*0.069), 0]

dem3 = [1, 0.069, 1.1075**2 ]


this_sos1 = tf2sos_analog(num1, dem1)
this_sos2 = tf2sos_analog(num2, dem2)
this_sos3 = tf2sos_analog(num3, dem3)
pretty_print_SOS(this_sos1, mode='omegayq')
pretty_print_SOS(this_sos2, mode='omegayq')
pretty_print_SOS(this_sos3, mode='omegayq')
#Por alguna razon les pone S**2 en el numerador cuando no deberia

num_total = np.polymul(np.polymul(num1, num2), num3)
dem_total = np.polymul(np.polymul(dem1, dem2), dem3)
this_sosf = tf2sos_analog(num_total, dem_total)
print( 'Transferencia pasa-banda Obtenida a mano final')
print( '------------------------')
pretty_print_SOS(this_sosf, mode='omegayq')

_ = analyze_sys(this_sosf)
