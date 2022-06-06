from trop.phrase import *

### if there are issues with the .show() command, the following must be run; 
    # import music21
    # music21.configure.run()


p1 = "0(Ма-), 0(ри-)[a], 1(е), 1(Де-)[a], 0(во), 1(чи-),-1, -1(ста-), -1(я), 0(Пре-), 2(свя-), -1(та-)[a], -1(я), -1(Бо-)[a], 0(го-), 1(ро-), 2, -1(ди), -1(це.)[a]"
p2 = "0(Ра-),0(дуй-),0(ся), 1(Не-), 1(ве-)[a], -2(сто), 0(Не-), 0(не-), 1(вест-)[a], -2(на-),1(я)[a]."
p3 = "0(Ца-), 0(ри-)[a],1(це),1(Ма-)[a],0(ти),1(Де-),-1,-1,-1(во)[a],2(Ру-),-1(но)[a], -1(все-),-1(по-)[a], 0(крь-), 1(ва-), 2(ю-), -1(ще-), -1(е.)[a]"
p5 = "0(Пре-),1[g], 1(вьс-)[a], 1(ша-), 1[g], 0(я)[a],0(не-), 1(бес-),-1[g], -1, 0(ньх), 1(сил)[a], 2(не), -1(тлен)[a],-1(но-), -1(е)[a], 0(си-), 1(я-)[a], 0(ни-), 0(е.)"

phrase1 = Phrase(1, p1, 'pa') 
phrase1.to_stream()

phrase2 = Phrase(1, p2, phrase1.last_note)
phrase2.to_stream()

phrase3 = Phrase(1, p3, phrase2.last_note)
phrase3.to_stream()

phrase5 = Phrase(1, p5, phrase2.last_note)
phrase5.to_stream()

combination = combine_phrases([phrase1, phrase2, phrase3, phrase2, phrase5]) 

combination.insert(0, metadata.Metadata())
combination.metadata.title = 'Марие Дево чистая (Ἁγνὴ Παρθένε)'
combination.metadata.composer = 'Нектарий Эгинский (Νεκτάριος Αιγίνης)'
combination.show()