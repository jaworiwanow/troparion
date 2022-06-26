import streamlit as st
from PIL import Image
from trop.phrase import *
import os
import base64

### Setting the enviornment variable to run MuseScore
environment.set('musescoreDirectPNGPath', '../usr/bin/mscore')

### Overwriting markdown settings to allow for the display of 
### byzantine notational symbols
m = st.markdown("""
<style>
div.stButton > button:first-child {
    font-family: "EZ Psaltica";
    font-size:20px;
    font-weight: bold;
    width: 3em;
    position:relative;left:25%;

}

</style>""", unsafe_allow_html=True)

### Download button generation
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

st.title("TROPARION ")

### Loading of graphics, as having two different button fonts is impossible
img_new = Image.open('./graphics/button_new-phrase.png')
img_undo = Image.open('./graphics/button_undo.png')
img_mxl = Image.open('./graphics/button_export-mxl.png')
img_midi = Image.open('./graphics/button_export-midi.png')

### Creating the columns 
mcol1, mcol2, mcol3, mcol4 = st.columns([1,1,1,1])

### initialising the composition and first phrase
if "composition" not in st.session_state:
	st.session_state.composition = []
if "phrase" not in st.session_state:
    st.session_state.phrase = ""

### Metadata
if "title" not in st.session_state:
    with st.form("metadata"):
        t = st.text_input('title')
        c = st.text_input('composer (optional)') 
        submitted = st.form_submit_button("✅")

    if submitted:
        st.session_state.composer = c
        st.session_state.title = t
        st.write(st.session_state.title)

### Button generation
with mcol1:
    st.image(img_new)
    new_phrase = st.button('✚')
with mcol2:
    st.image(img_undo)
    undo = st.button('⇦')

with mcol3:
    st.image(img_mxl)
    mxl = st.button(u'\U0001F3BC')
    if "stream" in st.session_state:
        st.markdown(get_binary_file_downloader_html('outputfile.musicxml', 'MusicXML'), unsafe_allow_html=True)

        
with mcol4:
    st.image(img_midi)
    midi = st.button(u'\U0001F3B6')
    if "stream" in st.session_state:
            st.markdown(get_binary_file_downloader_html('outputfile.midi', 'Midi'), unsafe_allow_html=True)



mode = st.selectbox(
    'What mode is the composition?',
    (1,2,3,4,5,6,7,8))

st.session_state.modus = mode
 


first_note = st.selectbox(
    'What is the first note?',
    ('ni', 'pa', 'vu', 'ga', 'di', 'ke', 'zo'))

st.session_state.first_note = first_note



### lyric selection choice (disappears once notes have been entered)
if len(st.session_state.composition) == 0 and len(st.session_state.phrase) ==0:
    lyric_choice = st.selectbox(
        'Would you like to enter lyrics?',
        ('yes', 'no'))
    #st.write("You selected", lyric_choice)
    st.session_state.lyrics = lyric_choice

if st.session_state.lyrics == 'yes':
    st.write("Please write the text after selecting the note it appears below and confirm by pressing the button")
    with st.form("syllable"):
        syllable = st.text_input("Lyric input", max_chars= 7)
        text = st.form_submit_button('✚')

### second row of columns for the music entry itself
col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])

with col1:
    ison1 = st.button("0")
    ison2 = st.button("p")
with col2:
    b1 = st.button("1")
    b2 = st.button("2")
    b3 = st.button("3")
    b4 = st.button("4")
    b5 = st.button("5")
    b6 = st.button("6")
    b7 = st.button("7")
    b8 = st.button("8")
    b9 = st.button("9")
with col3:
    b1a = st.button("q")
    b1b = st.button("`")
    b2a = st.button("w")
    b3a = st.button("e")
    b4a = st.button("r")
    b5a = st.button("t")
    b6a = st.button("y")
    b7a = st.button("i")

with col4:
    b_1 = st.button("!")
    b_2 = st.button("@")
    b_3 = st.button("#")
    b_4 = st.button("$")
    b_5 = st.button("%")
    b_6 = st.button("^")
    b_7 = st.button("&")

with col5:
    b_1a = st.button("Q")
    b_2a = st.button("W")
    b_3a = st.button("E")

with col6:
    klasma = st.button("  a")
    aple = st.button("  ;")
    diple = st.button("  k")
    triple = st.button("  k:")
    gorgon = st.button("s")
    digorgon = st.button("d")
    trigorgon = st.button("f")
    pass

### appending the pitch changes
if ison1 or ison2:
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "0"
    else:
        st.session_state.phrase = st.session_state.phrase + ",0"
if b1 or b1a or b1b:
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "1"
    else:
        st.session_state.phrase = st.session_state.phrase + ",1"

if b2 or b2a:
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "2"
    else:
        st.session_state.phrase = st.session_state.phrase + ",2"
if b3 or b3a:
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "3"
    else:
        st.session_state.phrase = st.session_state.phrase + ",3"

if b4 or b4a: 
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "4"
    else:
        st.session_state.phrase = st.session_state.phrase + ",4"
if b5 or b5a: 
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "5"
    else:
        st.session_state.phrase = st.session_state.phrase + ",5"
if b6 or b6a: 
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "6"
    else:
        st.session_state.phrase = st.session_state.phrase + ",6"
if b7 or b7a: 
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "7"
    else:
        st.session_state.phrase = st.session_state.phrase + ",7"
if b8:
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "8"
    else:
        st.session_state.phrase = st.session_state.phrase + ",8"    
if b9:
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "9"
    else:
        st.session_state.phrase = st.session_state.phrase + ",9"

if b_1 or b_1a:
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "-1"
    else:
        st.session_state.phrase = st.session_state.phrase + ",-1"
if b_2 or b_2a:
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "-2"
    else:
        st.session_state.phrase = st.session_state.phrase + ",-2"
if b_3 or b_3a:
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "-3"
    else:
        st.session_state.phrase = st.session_state.phrase + ",-3"
if b_4:
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "-4"
    else:
        st.session_state.phrase = st.session_state.phrase + ",-4"
if b_5: 
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "-5"
    else:
        st.session_state.phrase = st.session_state.phrase + ",-5"
if b_6: 
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "-6"
    else:
        st.session_state.phrase = st.session_state.phrase + ",-6"
if b_7: 
    if len(st.session_state.phrase) == 0:
        st.session_state.phrase = st.session_state.phrase + "-7"
    else:
        st.session_state.phrase = st.session_state.phrase + ",-7"

# appending the rhythm
if klasma:
    st.session_state.phrase = st.session_state.phrase + "[k]"
if aple:
    st.session_state.phrase = st.session_state.phrase + "[a]"
if diple:
    st.session_state.phrase = st.session_state.phrase + "[dp]"
if triple:
    st.session_state.phrase = st.session_state.phrase + "[tp]"

if gorgon:
    st.session_state.phrase = st.session_state.phrase + "[g]"
if digorgon:
    st.session_state.phrase = st.session_state.phrase + "[dg]"
if trigorgon:
    st.session_state.phrase = st.session_state.phrase + "[tg]"

if st.session_state.lyrics == 'yes':
    if text:
        st.session_state.phrase = st.session_state.phrase + "({})".format(syllable)

#st.write(st.session_state.composition)


if new_phrase:
    st.session_state.composition.append(st.session_state.phrase)
    st.session_state.phrase = ""

if undo:
    if len(st.session_state.phrase) == 0:
        st.session_state.composition.pop()
    else:
        st.session_state.phrase.pop()
   
if mxl or midi: 
    phrases = []
    first_note = st.session_state.first_note
    for phrase in st.session_state.composition:
        if len(phrase) == 0:
            pass
        elif "temp_first_note" not in st.session_state:
            temp_phrase = Phrase(st.session_state.modus, phrase, first_note)
            temp_phrase.to_stream()
            phrases.append(temp_phrase)
            st.session_state.temp_first_note = temp_phrase.last_note
        else:
            temp_phrase = Phrase(st.session_state.modus, phrase, first_note)
            temp_phrase.to_stream()
            phrases.append(temp_phrase)
            st.session_state.temp_first_note = temp_phrase.last_note

    combination = combine_phrases(phrases)
    combination.insert(0, metadata.Metadata())
    combination.metadata.title = st.session_state.title
    combination.metadata.composer = st.session_state.composer
    
    st.session_state.stream = combination



    if mxl:
        combination.write(fp = 'outputfile.musicxml', fmt = 'musicxml')
    if midi:
        combination.write(fp = 'outputfile.midi', fmt = 'midi')
    
