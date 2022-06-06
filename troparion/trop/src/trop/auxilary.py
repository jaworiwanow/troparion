import re

def change_extractor(list):
    ''' Function extracting the melodic changes from the input
    
    Parameter: 
    ----------
    list: list
        list of the split input string
    
    Return:
    ----------
    changes: list
        list of the melodic changes as integers
    
    '''
    changes = []
    for i in range(len(list)):
        if list[i][0].isdigit():
            changes.append(int(list[i][0]))
        else:
            changes.append(-int(list[i][1]))    
    return changes



def get_lyric(input):
    ''' Function retrieving the lyrics from the input
    
    Parameter:
    ---------
    input: str
        split off input string

    Return:
    --------
    lyric: str
        Lyric from the string
    '''
    
    assert isinstance(input, str), "invalid input"
    if input.count('(') == 1:
        lyric = re.search(r'\((.*?)\)',input).group(1)
    else:
        lyric = ''
    return lyric






