"""
Settings file for zagros.py. Import this in zagros.py to access the variables.
"""

import time
import os
import sys
import scipy.constants as sc
#import pypolychord as ppc
#from pypolychord.settings import PolyChordSettings
import dyPolyChord.pypolychord_utils
import dyPolyChord
import numpy as np
import logging

#-------------------------------------------------------------------------------
# define some constants

deg2rad = sc.pi / 180.0;
arcsec2rad = deg2rad / 3600.0;
uas2rad = 1e-6 * deg2rad / 3600.0;

sqrtTwo=np.sqrt(2.0)

#------------------------------------------------------------------------------
# Variables for assigning weights to visibilities

sigmaSim=None #Error on each visibility that goes into the predictions - should be the same as SIMULATION NOISE; None -> fit it
sefds=np.array([6000,1300,560,220,2000,1600,5000,1600,4500]) # station SEFDs in Jy - from EHT2017_station_info
corr_eff=0.88

# Codex-africanus settings

# dyPolyChord settings
nlive=300 # Number of live points for dpc
nlive_init=50
#num_repeats = 30 # Recommended (not less than 2*nDims)
#evtol=0.5 # Evidence tolerance for ppc
dynamic_goal=1.0
seed=42

#-------------------------------------------------------------------------------

# Priors - MUST BE CHANGED FOR EVERY MODEL THAT IS TESTED

# for uniform priors
Smin=0; Smax=2 # Jy
dxmin=-50*uas2rad; dxmax= 50*uas2rad; # uas
dymin=-50*uas2rad; dymax= 50*uas2rad; # uas
e1min = 0*uas2rad; e1max = 40*uas2rad;
e2min = 0*uas2rad; e2max = 40*uas2rad;
pamin = np.deg2rad(0); pamax = np.deg2rad(180);

#for Gaussian priors
#Smu=0.149124;Ssigma=1e-4;
