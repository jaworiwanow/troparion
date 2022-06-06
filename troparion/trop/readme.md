# TROP / TROPARION
#### **Tr**anscribing **O**rthodox **P**salmody / **A**nd **R**endering **I**t **On**line


## Goal
The Goal of this project is to create a python package (TROP) and a web application (TROPARION) to assist in the transcription of byzantine musical notation into modern western notation and midi. 

## Motivation
My hopes are to write a piece of software that is helpful to musicologists, novice performers, teachers and composers.

## Roadmap
1. planing/architectural design
2. build of a python package to handle the core functionality 
3. build of additional features for the web app
4. build of the web-app
5. deployment of the web-app

## Planned Features
#### Core Features
- textbased symbolic user input of byzantine notation
- rendered modern western notation output
- midi output

#### Additional Features
- rendered byzantine notation output
- textbased syllabic user input of byzantine notation
- editable modern western notation output
- microtonally tuned midi-output 
- lyrics input and output (Latin)
- lyrics input and output (Cyrillic)
- lyrics input and output (Greek)
 
#### Potential  Additional Features
- button based input
- modern western notation to byzantine notation transcription
- wysiwyg input
- lyrics input and output (Arabic)
- lyrics input and output (Hebrew)
- meter and barlines 
- companion optical character recognition software

## Known Issues
Even when MuseScore is installed, the .show() method may not work imediatelly. There are several solutions to this. 

### Command Line Fix
Running python -m music21.configure in the command line will open the configuration wizard.   

### script fix
Importin music21 and running music21.configure.run() within a script should do the same. 

### Jupyter Notebook Output
Running environment.set('musescoreDirectPNGPath', 'C:\\Program Files\\MuseScore 3\\bin\MuseScore3.exe') with the respective installation path allows for png outputs in jupyter notebooks.


## Documentation
## Screenshots
## Tutorials
Please refer to the TROP Architecture file for now.
