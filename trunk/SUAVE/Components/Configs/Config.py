## @ingroup Components-Configs
# Config.py
#
# Created:  Oct 2014, T. Lukacyzk
# Modified: Jan 2016, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Diffed_Data

# ----------------------------------------------------------------------
#  Config
# ----------------------------------------------------------------------

## @ingroup Components-Configs
class Config(Diffed_Data):
    """ SUAVE.Components.Config()
    
        The Top Level Configuration Class
        
            Assumptions:
            None
            
            Source:
            N/A
    """
    
    def __defaults__(self):
        """ This sets the default values for the configuration.
        
                Assumptions:
                None
                
                Source:
                N/A
                
                Inputs:
                None
                
                Outputs:
                None
                
                Properties Used:
                N/A
        """
        self.tag    = 'config'