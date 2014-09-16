# test_solar_nadiation.py
# 
# Created:  Emilio Botero, Sep 2014

#----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Attributes import Units

from SUAVE.Structure import (
Data, Container, Data_Exception, Data_Warning,
)

import numpy as np
import copy, time

#from SUAVE.Components.Energy.Processes import Solar_Radiation as Solar_Radiation
def main():
    
    # Setup and pack inputs, test several cases
    
    conditions = Data()
    conditions.frames = Data()
    conditions.frames.body = Data()    
    conditions.frames.planet = Data()
    conditions.frames.inertial = Data()
    conditions.freestream = Data()
    conditions.frames.body.inertial_rotations = np.zeros((3,3))
    conditions.frames.planet.time_date = time.strptime("Thu, Mar 20 12:00:00  2014", "%a, %b %d %H:%M:%S %Y",)
    conditions.frames.planet.latitude = np.array([[0.0],[35],[70]])
    conditions.frames.planet.longitude = np.array([[0.0],[0.0],[0.0]])
    conditions.frames.body.inertial_rotations[:,0] = np.array([0.0,np.pi/10,np.pi/5]) # Phi
    conditions.frames.body.inertial_rotations[:,1] = np.array([0.0,np.pi/10,np.pi/5]) # Theta
    conditions.frames.body.inertial_rotations[:,2] = np.array([0.0,np.pi/2,np.pi])    # Psi
    conditions.freestream.altitude = np.array([[600000.0],[0.0],[60000]])
    conditions.frames.inertial.time = np.array([[0.0],[0.0],[0.0]])
    
    # Call solar radiation
    rad = SUAVE.Components.Energy.Processes.Solar_Radiation()
    fluxes = rad.solar_radiation(conditions)
    
    print('Solar Fluxes')
    print fluxes
    truth_fluxes = [[ 1304.01069749],[ 815.02502004],[  783.55678702]]

    
    max_error =  np.max(np.abs(fluxes-truth_fluxes))
    
    assert( max_error < 1e-5 )
    
    return

# ----------------------------------------------------------------------        
#   Call Main
# ----------------------------------------------------------------------    

if __name__ == '__main__':
    main()
    