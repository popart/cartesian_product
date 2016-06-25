import sys

def _cartesian(consts, sets):
    results = []
    if len(sets) == 0:
        return consts
    else:
        rest = _cartesian(consts[1:], sets[1:])
        for x in sets[0]:
            for y in cartesian(x):
                for z in rest:
                    results.append(consts[0] + y + z)
    return results

""" Return the cartesian product of a string
    Where sets are contained within '{}' brackets
    Proceeding from inner '{}' brackets outwards
"""
def cartesian(s: str):
    if ' ' in s:
        raise InputException

    consts, sets = tokenize(s)
    return _cartesian(consts, sets)

""" Tokenize a string by '{}' brackets, returning 2 lists (consts, sets)
    consts: includes substrings outside outermost '{}' brackets
    sets: includes substrings within outermost '{}' brackets
"""
def tokenize(s: str):
    if ' ' in s:
        raise InputException

    consts = []
    sets = []

    left_idx = 0
    count = 0
    for i, c in enumerate(s):
        if c == '{':
            if count == 0:
                consts.append(s[left_idx:i])
                left_idx = i + 1
            count = count + 1
        elif c == '}' and count > 0: # (to handle '}{{')
            count = count - 1
            if count == 0:
                sets.append(split(s[left_idx:i]))
                left_idx = i + 1

    if count != 0:
        raise InputException

    consts.append(s[left_idx:len(s)])

    return (consts, sets)

def split(s: str):
    """ Split a string by ',', ignoring '{}' brackets """
    if ' ' in s:
        raise InputException

    substrings = []

    left_idx = 0
    count = 0
    for i, c in enumerate(s):
        if c == '{':
            count = count + 1
        elif c == '}' and count > 0:
            count = count - 1
        elif c == ',' and count == 0:
            substrings.append(s[left_idx:i])
            left_idx = i + 1

    substrings.append(s[left_idx:len(s)])

    return substrings

class InputException(Exception):
    pass

""" example: python cartesian.py "input{x,y}{1,2,3}"
    quotes are req'd, else bash's cartesian product will split input up
    does not accept spaces (which would result in ambiguous output)
"""
if __name__ == "__main__":
    try:
        print (' '.join(cartesian(sys.argv[1])))
    except InputException:
        print (sys.argv[1])
    except IndexError:
        print ("No argument given")
