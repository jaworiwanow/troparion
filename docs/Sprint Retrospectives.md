# Spirnt Retrospective

## Sprint 0
### 30.04.-14.05

The 0 sprint was used for research into the topic, the technical requirements, implementability and architectural requirements as well as existing software or solutions that could be build upon.

Functional requirements were defined. Technical requirements were partially defined, as no choice has yet been made for the web-app's (G)UI and I was unable to find a solution for dockerizaton. 

It was decided to use the music21 musicology library in combination with MuseScore for the initial release with a potential later use of LaTeX with the byzfonts package for rendered byzantine notation output.  

## Sprint 1
### 14.05.-21.05.
During the string the architecture had to be modified, but the core-functionality (except for fthora and ison) was implemented. 

It is expected, that the ison will be easy to implement, though fthores are expected to require further modifications to the architecture (most likely dealt with by case distinctions and modifications to the scale generation process).
The decision of notation convention for the ison has yet to be made, although I am leaning towards displaying it only within the bar it first appears instead of having tied long notes in every measure. 

## Sprint 2
### 21.05. - 04.06.
During this sprint the web-app for TROPARION has been partially implemented. What was assumed to be rather straightforward, turned out to have several challenges in store, as the research in sprint 0 seems to have been insufficient.

The initially planned use of the unicode symbols for the byzantine notation could not be adhered to, as it was impossible to get the symbols to display locally or within docker; Therefore a special font had to be found and used. 
Due to technical limitations (such as streamlit allowing only one font for all buttons) some workarounds had to be found (such as the use of unicode symbols).  

The image-output unfortunately will be a challenge, as music21 does not, to my surprise, yet support writing png files and the .show() output requires a display. 
Attempts to use an X Socket have not borne fruit yet.

## Sprint 2
### 04.06. - 12.07.

The greatest part of the second sprint was spent in experimentation, that, unfortunately has not yet lead to the desired solutions of getting MuseScore to display within docker, ison to be added or image output to work. 

The documentation, however, both for the package and webapp has been expanded and tutorials were added. Additionally a demo-video was created. 

A manual session reset has been added and download buttons were implemented with the files are being written as intended. 

The code was commented and cleaned a bit and the repository's folder structure was modified to allow for the easier finding of some files. 

Research into a better choice for a web framework has lead to the discovery of several candidates, further research as to whether or not they share streamlit's weaknesses or have others on their own, is necessary. 

Experimentation into a potential integration of LaTeX for byzantine notation output is ongoing. 

GitLab issues (of http framing layers) sadly could not be solved either, wherefore everything except for the issue boards was "migrated" to GitHub. 

