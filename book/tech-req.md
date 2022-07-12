# Requirements for TrOPARIOn

## Technical Requirements 
The web-app shall provide a graphical interface for the use of a python-package (trop) handling the core functionality. 

### **Requirements for the python package ("back-end")**
- Python 3
    -  music21 
    

### **Requirements for the Web-App**
- Python
    - Music21
    - trop 
* font containing the Byzantine musical notation symbol set
* graphics
* python web-framework (e.g.: streamlit, flask, Django,...)

### **Requirements for Deployment**
* configured docker container
* cloud application platform capable of deploying docker containers (e.g.: Heroku) 

### **Storage Requirements**
* 1.5 GB for the docker image
* 300 KB for the output files

## Expected Requirement Changes

A change of hosting may be necessary but is hard to predict. 

The web-framework will definitely need to change, though.
For while streamlit initially seemed a reasonable choice, in creating a web-app through it several shortcomings were made apparent, wherefore another web-framework is currently being considered and researched

