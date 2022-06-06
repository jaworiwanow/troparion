import unittest

from trop.modus import Modus
from trop.phrase import Phrase
from trop.dictionaries import mode_types

class TestMode(unittest.TestCase):
    def test_right_mode_type(self):
        ''' Testing if the right mode type is selected.'''

        mode_numbers = list(range(1,9))
        modes = [Modus(x).mode_type for x in mode_numbers]

        self.assertEqual(modes, list(mode_types.values()))


class TestPhrase(unittest.TestCase):
    def testPhraseExtraction(self):
        '''Testing the extraction of inputs.'''

        input = "0(Ма-), 0(ри-)[a], 1(е), 1(Де-)[a], 0(во), 1(чи-),-1, -1(ста-), -1(я), 0(Пре-), 2(свя-), -1(та-)[a], -1(я), -1(Бо-)[a], 0(го-), 1(ро-), 2, -1(ди), -1(це.)[a]"
        changes = [0, 0, 1, 1, 0, 1, -1, -1, -1, 0, 2, -1, -1, -1, 0, 1, 2, -1, -1]
        text = ['Ма-', 'ри-', 'е', 'Де-', 'во', 'чи-', '', 'ста-', 'я', 'Пре-', 'свя-', 'та-', 'я', 'Бо-', 'го-', 'ро-', '', 'ди', 'це.']
        rhythm = [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2]

        phrase = Phrase(1, input, 'pa')

        phrase.syntax_check()

        self.assertEqual(phrase.mode_num, 1)
        self.assertEqual(phrase.changes, changes)
        self.assertEqual(phrase.text, text)
        self.assertEqual(phrase.durations, rhythm)