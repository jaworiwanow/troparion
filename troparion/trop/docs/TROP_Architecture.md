# TROP Architecture

## Process
First, the mode and root are specified to define the scale, from which iteratively the music phrases are generated based on the user input. 

The music-input follows, with it being divided in phrases, instead of being done in bulk. This is done in order of barlines to be able to mark phrase endings.

The syntax is automatically checked with the creation of each instance. 

Phrases are then combined into the composition using the combine_phrases() method, which takes a list of phrases and combines them.

## Input Syntax
The note-input is a string of specific characters. 

Entry is done note by note, where text, fthora, rhythmic signs and ison are entered with the note itself. Notes are separated by commas (,).

The first and only not required is the **melodic direction**, where 0 indicates repetition of pitch and integers are used to indicate the number of steps (1 being one step higher, -3 being three steps lower).

Additional note-features are entered in brackets following the digit.

### Parameters
|Parameter|bracket|
|--------|-----|
| text   | ( ) |
| rhythm | [ ] |
| fthora | { } |

#### Text
Text is entered syllabically. Hyphenation has to be entered as well, if it is to appear. 

#### Rhythm
Rhythmic symbols are entered with certain strings above the note they apear to be written above or below. The acceptable input here is 
'k' for klasma, 'a' for aple, 'dp' for diple, 'tp' for triple as well as 'g' for gorgon, 'dg' for digorgon and 'tg' for trigorgon. 

The names here refer to the names of the rhytmic symbols.

#### Fthora
The original concept of the syntax has proven to be unsuitable and alternatives are being considered. For the time being, though, it is funcionality that will be added later. 

### Ison
The ison is entered as a syllable with an underscore as prefix following the melodic direction of the note over which it appears. 
