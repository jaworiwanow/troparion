
from music21 import *
from trop.dictionaries import*
from trop.scales import *

class Modus:
    ''' Byzantine Mode class, defined by 
    Parameters
    ----------
    mode_num: int
        Number of the mode (between 1 and 8)
    
    Attributes
    ----------
    mode_num: int
        Number of the mode (between 1 and 8)    mod
    mode_type: str
        Genus of the mode (diatonic, soft chromatic, hard chromatic or enharmonic)

    Methods
    -------
    get_scale
        Generation of the note names as a music21 scale object    
    '''
    def __init__(self, mode_num):
        assert mode_num in list(range(1,9)),"Please enter the mode-number as a digit."
        self.mode_num = mode_num
        self.mode_type = mode_types[self.mode_num]

        

    def get_scale(self):
        ''' class method for the retrieval of note names
        Parameters:
        ----------
        mode_type: str
            type of the mode (diatonic, soft chromatic, hard chromatic, enharmonic)
        
        Return:
        ----------
        mode_notes: music21 scale
            music21 scale object containing the note-names
        '''
        
        mode_notes = scale_gen[self.mode_type]

        return mode_notes
    
            

 