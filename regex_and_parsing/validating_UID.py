import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        #It must contain at least  uppercase English alphabet characters.
        assert re.search(r'[A-Z]{2}', u)
        #It must contain at least  digits ( - ).
        assert re.search(r'\d\d\d', u)
        #It should only contain alphanumeric characters ( - ,  -  &  - ).
        assert not re.search(r'[^a-zA-Z0-9]', u)
        #No character should repeat.
        assert not re.search(r'(.)\1', u)
        #There must be exactly  characters in a valid UID.
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')