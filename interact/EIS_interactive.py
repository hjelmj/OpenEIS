# Python dependencies
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, FloatText
from IPython.display import display

# generate a default angular frequency vector
w=np.logspace(7,0,7*10)

# impedance functions
def Z_R_C(R, C, w=w):
    """
    Returns the impedance of a -R-C- circuit.
    
    Parameters:
    -----------
    R : resistance (Ohmic resistance) of circuit [Ohm]
    C : capacitance of circuit [Farad]
    w : angular frequency [rad s^-1]
    
    Returns:
    --------
    The frequency dependent impedance as a complex number. [Ohm]
    """
    Z_R = R
    Z_C = -1j/(w*C) # capacitive reactance
    Z_R_C = Z_R + Z_C # series connection
    return Z_R_C

def Z_R_RC(R0, R1, C1, w=w):
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
"""
def Z_Randles_si(w,R0=5, Rct=50, C=1e-5, n=1, Dox=1e-5, Dred=1e-5, Cox=1e-6, Cred=1e-6, A=1, T=298):
    #docstring
    #function that returns the impedance of a Randles circuit with a semi-infinite diffusion element
    Z_R0 = R0 # series resistance (uncompensated electrolyte resistance)
    sigma = ((R*T)/(n**2 * F**2 * A * np.sqrt(2)))*(1/(np.sqrt(Dox)*Cox) + 1/(np.sqrt(Dred)*Cred)) # Warburg coefficient
    Z_W = sigma/w**0.5 - 1j*sigma/w**0.5 # Warburg impedance, semi-infinite planar diffusion
    Z_f = Rct + Z_W # impedance of faradaic branch
    Z_C = -1j/(w*C1) # capacitive reactance - impedance of capacitor (models double-layer capacitance)            
    Z_parallel = 1/(1/Z_C + 1/Z_f)
    Z_total = Z_R0 + Z_parallel
    return Z_total"""

# plot functions

def plot_nyquist():
    pass

def plot_bode():
    pass

def plot_residuals():
    pass

def R_C_plot(R,C):
    Z = Z_R_C(R,C)
    # set up a figure canvas with two plot areas (sets of axes)
    fig,ax = plt.subplots(nrows=1, ncols=2, figsize=(10,3))
    # add a Nyquist plot (first plot)
    ax[0].plot(Z.real, -1*Z.imag, marker='o',ms=5, mec='b', mew=0.7, mfc='none')
    ax[0].set_xlim(0,60)
    ax[0].set_ylim(0,60)
    ax[0].set_aspect('equal')
    ax[0].set_xlabel('Z$_{re}$ [$\Omega$]')
    ax[0].set_ylabel('-Z$_{im}$ [$\Omega$]')
    # add a Bode plot with 
    ax[1].plot(w/2*np.pi,-1*Z.imag, marker='o',ms=5, mec='r', mew=0.7, mfc='none', label='$Z_{im}$')
    ax[1].plot(w/2*np.pi,Z.real, marker='o',ms=5, mec='b', mew=0.7, mfc='none', label='$Z_{re}$')
    ax[1].set_xscale("log")
    ax[1].set_xlim(min(w),max(w))
    ax[1].set_ylim(0,100)
    ax[1].set_ylabel('|Z$_{i}$| [$\Omega$]')
    ax[1].set_xlabel('f [Hz]')
    ax[1].legend(loc='best')
    #plt.tight_layout()
    plt.show()

def R_RC_plot(R0,R1,C1):
    Z = Z_R_RC(R0,R1,C1)
    # set up a figure canvas with two plot areas (sets of axes)
    fig,ax = plt.subplots(nrows=2, ncols=1, figsize=(8,8))
    # add a Nyquist plot (first plot)
    ax[0].plot(Z.real, -1*Z.imag, marker='o',ms=5, mec='b', mew=0.7, mfc='none')
    ax[0].set_xlim(0,60)
    ax[0].set_ylim(0,20)
    ax[0].set_aspect('equal')
    ax[0].set_xlabel('Z$_{re}$ [$\Omega$]')
    ax[0].set_ylabel('-Z$_{im}$ [$\Omega$]')
    # add a Bode plot
    ax[1].plot(w/2*np.pi,-1*Z.imag, marker='o',ms=5, mec='r', mew=0.7, mfc='none', label='$Z_{im}$')
    ax[1].plot(w/2*np.pi,Z.real, marker='o',ms=5, mec='b', mew=0.7, mfc='none', label='$Z_{re}$')
    ax[1].set_xscale("log")
    ax[1].set_xlim(min(w),max(w))
    ax[1].set_ylim()
    ax[1].set_ylabel('|Z$_{i}$| [$\Omega$]')
    ax[1].set_xlabel('f [Hz]')
    ax[1].legend(loc='best')
    
    plt.tight_layout()
    plt.show()
    
"""def Randles_si_plot(np.logspace(7,0,7*10),R0=5, Rct=50, C=1e-5, n=1, Dox=1e-5, Dred=1e-5, Cox=1e-6, Cred=1e-6, A=1, T=298):
    Z = Z_Randles_si(w, R0=R0, Rct=Rct, C=C, n=n, Dox=Dox, Dred=Dred, Cox=Cox, Cred=Cred, A=A, T=T)
    #set up a figure canvas with two plot areas (sets of axes)
    fig,ax = plt.subplots(nrows=1, ncols=1, figsize=(8,4))
    #add a Nyquist plot (first plot)
    ax.plot(Z.real, -1*Z.imag, marker='o',ms=5, mec='b', mew=0.7, mfc='none')
    ax.set_xlim(0,60)
    ax.set_ylim(0,60)
    ax.set_aspect('equal')
    ax.set_xlabel('Z$_{re}$ [$\Omega$]')
    ax.set_ylabel('-Z$_{im}$ [$\Omega$]')
    plt.show()"""

# functions for interactive output using ipywidgets
def R_C_interactive():
    w1 = interact(R_C_plot, 
                  R=FloatSlider(description='$R$', min=0, max=60, step=1, value=10, orientation='horizontal', 
                                readout=True, readout_format='.1f', continuous_update=True),
                  C=FloatSlider(description='$C$', min=1e-6, max=1e-3, step=1e-6, value=1e-5,orientation='horizontal',
                                readout=True, readout_format='.2e', continuous_update=False))
    display(w1)


def R_RC_interactive():
    interact(R_RC_plot, 
             R0=FloatSlider(description='$R_0$', min=0, max=30, step=1, value=10, orientation='horizontal', 
                            readout=True, readout_format='.1f', continuous_update=True),
             R1=FloatSlider(description='$R_1$', min=5, max=30, step=1, value=20, orientation='horizontal', 
                            readout=True, readout_format='.1f', continuous_update=True),
             C1=FloatSlider(description='$C_1$', min=1e-6, max=1e-3, step=1e-6, value=1e-5,orientation='horizontal', 
                            readout=True, readout_format='.2e', continuous_update=False))

   
"""def Randles_si_interactive():
    interact(Randles_si_plot, 
             R0=FloatSlider(description='$R_0$', min=0, max=30, step=1, value=10, orientation='horizontal', 
                            readout=True, readout_format='.1f', continuous_update=True),
             Rct=FloatSlider(description='$R_1$', min=5, max=30, step=1, value=20, orientation='horizontal', 
                            readout=True, readout_format='.1f', continuous_update=True),
             C=FloatSlider(description='$C_1$', min=1e-6, max=1e-3, step=1e-6, value=1e-5,orientation='horizontal', 
                            readout=True, readout_format='.2e', continuous_update=False))"""