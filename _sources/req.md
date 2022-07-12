# Requirements for TrOPARIOn

## Functional Requirements 

**GENERAL FUNCTIONALITY**
1. The app shall provide users with the ability to transcribe Orthodox psalmody without modulation or ornamentation from Byzantine musical notation into modern western music notation.
2. The app should provide users with the ability to transcribe Orthodox psalmody including modulation or ornamentation into modern western music notation. 
3. The app should provide users with the ability to transcribe Orthodox psalmody with movable drones (ison) from Byzantine musical notation into modern western music notation. 

**SYSTEM REQUIREMENTS**

4. The app shall run within web-browsers.
5. The app shall be usable without an internet connection locally, provided technical requirements are met. 
6. The online app shall not require any local installation on the user's machine for its operation.
7. The offline app shall not require commercial software products for its operation. 
8. The offline app should be executable on as many operating systems as possible.

```{dropdown} requirement justifications
4. Having the application run within web-browsers tremendously simplifies reaching the goal of cross platform availability.
5. Having the ability to use the application independently of a hosting service may be desirable to some users and add to the longevity of the project.
6. While this requierment adds an additional challange, it ensures a better user experience and makes testing and troubleshooting for the web-version more reliable.
7. To guarantee cross-platform accessibility to the largest extent practicable. 
8. To guarantee cross-platform accessibility to the largest extent practicable. 

```

**DATA AND STORAGE**

9. The app shall not collect any user data.
10. The app shall only process the button-based and text-based user input.
11. The app shall not save HTTP cookies on the user's machine. 
12. The app shall not automatically save any files on the user's machine. 
13. The app  shall not store any data after a session has ended.

```{dropdown} requirement justifications
The first four of these requirements are for one a limitation of scope and a legal precaution on the other hand. 

The last one is limiting the storage to a session state is, given the generation of downloadable output files, a way to limit the ressource requierments for the app to operate. 

```


**INPUT**

14. The app shall use a symbolic button-based input for pitch directions and rhythm.
15. The app's buttons shall display Byzantine music notation characters. 
16. The app's input shall be strictly sequential.
17. The app should allow for undoing the last action before the user input is committed. 
18. The app shall support Cyrillic, Greek and Latin text input. 
19. The app should support Armenian, Coptic and  Georgian text input. 
20. The app may support Amaharic, Arabic and Hebrew text input.

```{dropdown} requirement justifications
14. This way entry is simplified for the user and the possibility of improper input is limited.
15. This further specification is to make sure that the symbols themselves and not a translation thereof is displayed, so that users require little to no understanding of the symbols themselves. 
16. A limitation of scope simplifying the architecture. A non-linear input makes little sense, given how the notation is read and a transcription is done. 
17. Usability feature
18. Focus on Cyrillic, Greek and Latin as the majority of psalmody is written in those scripts.
19. Eventual addition, as those scripts are of significant enough relevance.
20. Expected to pose challenges in implementation. 

```

**OUTPUT**

21. The app shall have a graphical (modern western sheet music) output upon the user's manual request if user input has been committed. 
22. The app should have a playable auditory (sound) output upon the user's manual request if user input has been committed.
23. The app shall not display the graphical output itself, but generate a MusicxML file.
24. The app shall not play back the auditory output itself, but generate a midi file. 
25. The app's output files shall be in editable, non-proprietary formats with cross-platform support. 
26. The app's graphical output shall be in a file-format usable by the most common music notation software solutions. 
27. The app's graphic output shall use bar lines to divide phrases and not regular metric bars. 
28. The app may create non-editable graphical outputs.
29. The app's graphic output should visually represent microtonal deviations form twelve-tone equal temperament.
30. The app's auditory output should reproduce microtonal deviations from twelve-tone equal temperament. 
 
```{dropdown} requirement justifications
21. Specification of the conditions.
22. Specification of the conditions.
23. Limitation of scope to keep the application lightweight. 
24. Limitation of scope to keep the application lightweight. 
25. Neccessary, to allow for cross-platform availability and usability in computer-assisted musicology. 
26. Specification to make sure the output can be used for computer assited musicological analysis, as e.g.: svg is also an editable format. 
27. Barlines would be of no other uses other than marking structural points, as the music itself is measureless and the rhythmic characteristics are determined by the words, not a given time signature. Barlines, however can still be useful for analysis, e.g.: when it comes to structure, phrase length and so on. 
28. Usability feature. Low priority, as editable music notation formats can be easily converted into various other file formats, including pdf and svg. 
29. Relevant for musicological analysis.
30. Desirable for a better representation. 


```
```{dropdown} specifications
The most suitable fileformats are (uncompressed) MusicXML and midi, due to them being 
- editable
- non-proprietary
- widely used
- natively supported by most music notation software

The most common music notation software solutions refered to are Dorico, Finale, LilyPond, MuseScore, Notion and Sibelius. 

```

__________________________________
## Expected Requirement Changes

While new develpments in an long codified and conservative tradition seem unlikely, the requirements are likely to be expanded. 

Given, that the musical notation system nowadays used in Orthodox psalmody has evolved over a long period of time and has sprouted several off-shoots, it is likely that the symbol set at the very least may need to be expanded in the future to allow for better transcription of earlier sources.

Also, ornamentation, especially in Sticheraric genera, can be of great importance, wherefore the requirement of an addition of ornamentation is quite likely. 
_________________________________

## Internalisation issues

Text input is expected to add challenges, as encoding may be an issue and correct display may not be possible without additional software or fonts.

Arabic and Hebrew, furthermore, are read right to left, which would require a mirroring of the notation itself as well. 