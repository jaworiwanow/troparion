from music21 import scale


dt = ["d", "e", "f`", "g", "a", "b", "c`"]
en = ["f", "g", "a", "b-","c", "d", "e"]
hc = ["d", "e-", "f#~","g", "a", "b-", "c#~"]
sc = ["g", "a`", "b`", "c", "d", "e`", "f"]

diatonic = scale.ConcreteScale(pitches= dt)
enharmonic = scale.ConcreteScale(pitches= en)
hard_chromatic = scale.ConcreteScale(pitches= hc)
soft_chromatic = scale.ConcreteScale(pitches= sc)

scale_gen = {'diatonic': diatonic, 'soft_chromatic': soft_chromatic, 'hard_chromatic': hard_chromatic, 'enharmonic': enharmonic}