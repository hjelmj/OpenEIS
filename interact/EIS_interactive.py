# Python dependencies
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider


def Z_R_RC(R0, R1, C1, w):
    """
    Returns the impedance of a -R-(RC)- circuit.
    
    Parameters:
    -----------
    R0 : series resistance (Ohmic resistance) of circuit [Ohm]
    R1 : resistance of parallel connected circuit element [Ohm]
    C1 : capacitance of parallel connected circuit element [Farad]
    w : angular frequency, accepts an array as well as a single number [rad s^-1]
    
    Returns:
    --------
    The frequency dependent impedance as a complex number. [Ohm]
    """
    Z_R0 = R0
    Z_R1 = R1
    Z_C1 = -1j/(w*C1) # capacitive reactance
    Z_RC = 1/(1/Z_R1 + 1/Z_C1) # parallel connection
    return Z_R0 + Z_RC # Z_R0 and Z_RC connected in series

# 2D plot functions
def plot_nyquist():
    pass

def plot_bode():
    pass

def plot_residuals():
    pass

def R_RC_plot(R0,R1,C1):
    Z = Z_R_RC(R0,R1,C1,w)
    # set up a figure canvas with two plot areas (sets of axes)
    fig,ax = plt.subplots(nrows=2, ncols=1, figsize=(8,8))
    # add a Nyquist plot (first plot)
    ax[0].plot(Z.real, -1*Z.imag, marker='o',ms=5, mec='b', mew=0.7, mfc='none')
    ax[0].set_xlim(0,60)
    ax[0].set_ylim(0,20)
    ax[0].set_aspect('equal')
    ax[0].set_xlabel('Z$_{re}$ [$\Omega$]')
    ax[0].set_ylabel('-Z$_{im}$ [$\Omega$]')
    # add a Bode plot with 
    ax[1].plot(w/2*np.pi,-1*Z.imag, marker='o',ms=5, mec='r', mew=0.7, mfc='none', label='$Z_{im}$')
    ax[1].plot(w/2*np.pi,Z.real, marker='o',ms=5, mec='b', mew=0.7, mfc='none', label='$Z_{re}$')
    ax[1].set_xscale("log")
    ax[1].set_xlim(min(w),max(w))
    ax[1].set_ylim()
    ax[1].set_ylabel('|Z$_{i}$| [$\Omega$]')
    ax[1].set_xlabel('f [Hz]')
    ax[1].legend(loc='best')
    # plt.tight_layout()
    plt.show()

# functions for interactive output using ipywidgets
def R_RC_interactive():
    interact(R_RC_plot, 
             R0=FloatSlider(description='$R_0$', min=0, max=30, step=1, value=10, orientation='horizontal', 
                            readout=True, readout_format='.1f', continuous_update=True),
             R1=FloatSlider(description='$R_1$', min=5, max=30, step=1, value=20, orientation='horizontal', 
                            readout=True, readout_format='.1f', continuous_update=True),
             C1=FloatSlider(description='$C_1$', min=1e-6, max=1e-3, step=1e-6, value=1e-5,orientation='horizontal', 
                            readout=True, readout_format='.2e', continuous_update=False))
    