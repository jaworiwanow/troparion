notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
syllables = ['ni', 'pa', 'vu', 'ga', 'di', 'ke', 'zo']

notes_to_syllables = dict(zip(notes, syllables))
syllables_to_notes = dict(zip(syllables, notes))
rhythm_to_duration = {'k': 2, 'a': 2, 'dp': 3, 'tp': 4, 'g': 0.5, 'dg':0.333333333, 'tg': 0.25}


mode_types ={1: 'diatonic', 2: 'soft_chromatic', 3: 'enharmonic', 4: 'diatonic', 5: 'diatonic', 6: 'hard_chromatic', 7: 'enharmonic', 
    8: 'diatonic'}
roots = {'diatonic': 'D', 'soft_chromatic': 'G', 'hard_chromatic': 'D', 'enharmonic':'F'}
