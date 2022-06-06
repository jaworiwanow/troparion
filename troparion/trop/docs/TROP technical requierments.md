# TROP technical requirements

## Core Features: modern western notation output and midi-output

For this feature, while several options were considered, the most promising seems to be the music21 Python library, altough  python-ly (a python lilypond-wrapper) or a combination of abc-notation scripts could also be considered. 

It is yet to be determined if using music21's tiny notation or abc-notation will be preferable, it would mostly depend on the lyrics input. 

### Techical requirements
**bold** denotes a choice made, *italic* a preference.  

- Docker Image containing
    - **Python** 
        - relevant packages
    - Notation tool, either
        - *MuseScore*,
        - LilyPond or
        - abc-Notation tools
    

music21 and Musescore are the prefered combination, due to their combined versitility and functionality. 

A setup of music21 and LilyPond is possible, but significantly more difficult to set up.

Initial development will rely on MuseScore, while a setup with LilyPond may be used for the web-app deployment. 

### Potential Issues and alternative solutions
- Docker and software setup
    - alternative: abc-notation 
- Docker size (hosting)


## Core Feature: textbased symbolic user input of byzantine notation
Input for the python package is of no real concern, as long as encoding doesn't prove troublesome. 

For different "symbol maps" further research into the currently available notation options is necessary. 

The processing will be based on string, list and maybe tuple processing that python can handle natively. 

