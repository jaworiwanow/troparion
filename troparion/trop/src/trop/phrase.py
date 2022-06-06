from logging import raiseExceptions
from trop.auxilary import get_lyric
from trop.modus import *
from trop.dictionaries import rhythm_to_duration
from music21 import stream
import re

class Phrase:
    ''' Byzantine notation phrase/line 

    Parameters:
    ----------
    mode_num: int
        number of the Mode
    input: str
        character string of the music input
    incipit: str or music21 note object
        syllable of the first note or the note itself
    first_ison: str
        syllable for the ison of the first note (default: None)
    
    Attributes:
    -----------
    scale: music21 scale+
        scale object containing the notes
    lyrics: bool
        inclusion of lyrics in the phrase
    

    Methods:
    ----------
    input_prep
        input-cleaning (removal of blank spaces) and splitting
    syntax_check
        checking of the input syntax, requires input to be split with input_prep
    rules_check
        checking of byzantine notation rules, full implementation not realized, necessary for rendered byzantine notation output mostly
    '''

    def __init__(self, mode_num, input, incipit, first_ison = None):

        self.input = input

        assert isinstance(self.input, str), "Input must be a character string."
        assert len(self.input) > 0, "There needs to be an input to work with."

        
        # loading the mode and checking the validity in the Modus class
        self.modus = Modus(mode_num)
                
        #initialisation of the Phrase
        self.mode_num = mode_num    
        self.scale = self.modus.get_scale()
               
        
        self.ison = first_ison
        
        #setting of the "lyric mode"
        if self.input.count("(") > 0:
            self.lyrics = True
        else:
            self.lyrics = False

        self.incipit = incipit

        self.input_prep()
        self.syntax_check()
        self.get_changes()
            
            
    
    def input_prep(self):
        ''' Input perparation: removal of spaces to make indexing throughout the process easier and splitting.
        Parameter:
        ----------
        self.input: str
            chracter string of the input

        Return:
        --------
        self.input: list
            list containing the input splits
        
        '''
        # splitting the string    
        self.input = self.input.split(",")
        # removal of blank spaces
        for i in range(len(self.input)):
            self.input[i] = self.input[i].replace(" ", "")
            assert len(self.input[i])>0, "There needs to be at least a valid melodic direction for note {}".format(i+1)

    def syntax_check(self):
        ''' Syntax checker for the input; detection of bracket mismatches and valid melodic input
        
        '''
        for i in range(len(self.input)):
            # Checking for a valid melodic direction 
            if self.input[i][0].isdigit():
                pass    
            elif self.input[i][0] == "-":
                if self.input[i][1].isdigit():
                    pass
                else:
                    raise ValueError("Please enter a valid melodic direction first at note {} ".format(i+1)) 
            
            else:
                raise ValueError("Please enter a valid melodic direction first at note {} ".format(i+1))
            
            ### checking for bracket mismatches
            for brackets in [["(", ")"], ["[", "]"],  ["{", "}"]]:
                if self.input[i].count(brackets[0]) != self.input[i].count(brackets[1]):

                    raise ValueError("input error: {}{} bracket mismatch at note {}".format(brackets[0], brackets[1], i+1))

                else: 
                    pass

            for brackets in [["(", ")"], ["[", "]"],  ["{", "}"]]:
                if self.input[i].count(brackets[0]) > 1 or self.input[i].count(brackets[1])> 1:
                    raise ValueError("input error: Too many {}{} brackets at note {}".format(brackets[0], brackets[1], i+1))

        ### checking for missing lyrics or a surplus of lyric brackets 
        if self.lyrics == True and self.input[0].count("(") !=1:
            raise ValueError('The initial note must have text if lyrics have been entered.')    

    def rules_check(self):
        ''' Rules checker to ensure proper transcription. Most rules not implemented, as they are relevant for byzantine rendered output only.
        
        
        '''
        if self.input[0][0] != 0:
            raise ValueError("The first note cannot be anything other than a ison (0)")
        
    def get_changes(self):
        ''' Extracting melodic direction changes and rhythmical values from the input.
        Parameters:
        ----------
        self.input: list of str
            list of items in the input

        Return:
        ---------
        changes: list of integers
            extracted list of melodic directions

        durations: list of floats
            extracted list of rhythmic durations
        
        '''
        changes = []
        durations = [1]*len(self.input)
        text = [' ']*len(self.input)

        for i in range(len(self.input)):
            if self.input[i][0].isdigit(): # appending non-negative directions
                changes.append(int(self.input[i][0]))
            else:                          # appending negative directions
                changes.append(-int(self.input[i][1]))

            if self.input[i].count("[") ==1: # checking for rhythmic symbol
                rhythmic_symbol = re.search(r"\[(.*?)\]", self.input[i]).group(1).replace("'", "")
                duration = rhythm_to_duration[rhythmic_symbol]
                if duration > 1:
                    durations[i] = durations[i] *duration
                elif duration == 0.5:
                    durations[i] = durations[i] *duration
                    durations[i-1] = durations[i-1] *duration
                elif duration == 0.333333333:
                    durations[i] = durations[i] *duration
                    durations[i-1] = durations[i-1] *duration
                    durations[i+1] = durations[i+1] *duration
                elif duration == 0.25:
                    durations[i] = durations[i] *duration
                    durations[i-1] = durations[i-1] *duration
                    durations[i+1] = durations[i+1] *duration
                    durations[i+2] = durations[i+2] *duration

            if self.lyrics == True:
                text[i]= (get_lyric(self.input[i]))

        self.changes = changes
        self.durations = durations
        self.text = text
        

    def to_stream(self):
        ''' Generation of a music21 stream for rendered western notation output.
            
        '''
        
        substream = stream.Stream()  
        # generation of the Gamut
        lower_limit = self.scale.pitches[0].transpose('-P8')
        upper_limit = self.scale.pitches[-1].transpose('P8')

        notes = [p for p in self.scale.getPitches(lower_limit, upper_limit)]
        # setting of the first note
        if len(substream) == 0:
            if isinstance(self.incipit, str):
                n = note.Note(syllables_to_notes[self.incipit])
                n.octave = 4
            elif isinstance(self.incipit, note.Note):
                n = self.incipit
                substream.clef = clef.GClef()
                substream.clef.hideObjectOnPrint = True

            i = notes.index(n.pitch)
        # iterative note generation
        for j in range(len(self.changes)):    
            i = i + self.changes[j]
            n = note.Note(notes[i])
            n.duration = duration.Duration(self.durations[j])
            n.addLyric(self.text[j])
            substream.append(n)
        # defining the time signature so that the whole phrase fits in one bar
        substream.timeSignature = meter.TimeSignature('{}/4'.format(round(sum(self.durations))))
        substream.timeSignature.style.hideObjectOnPrint = True

        self.substream = substream
        self.last_note = n # needed to calculate the first note of the next phrase. 

        

    def show_western(self):
        ''' Generation of a music21 stream and rendered western notation output.
        
        '''
        stream = self.to_stream()
        stream.show()

    def show_midi(self):
        ''' Generation of a music21 stream and conversion to midi.
                
        '''
        stream = self.to_stream()
        stream.show('midi')
            


def combine_phrases(phrases):
    '''Function for the combination of phrases.
    Parameter:
    ---------
    phrases: list
        List of Phrase instances
    

    Return:
    --------
    combined_stream: music21 stream
        music21 stream object consisting of the combined phrases
    
    '''
    assert isinstance(phrases, list)
    combined_stream = stream.Stream()
    for phrase in phrases:
        assert isinstance(phrase, Phrase)

        
    for phrase in phrases:
        
        m = stream.Measure()
        for note in phrase.substream.notes:
            m.append(note)

        combined_stream.append(m)       
  
    return combined_stream