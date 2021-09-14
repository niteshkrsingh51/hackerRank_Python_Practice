import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        #There must be exactly  characters in a valid UID.
        assert len(u) == 10
        #It should only contain only digits.
        assert re.search(r'[^[0-9]+$]', u)
    except:
        print('Invalid')
    else:
        print('Valid')