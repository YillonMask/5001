"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi 
"""


def main():
    header = '+---+---+---+---+---+'
    print(header)
    print('| p | q | r | A | B |')
    values = [False, True]
    for p in values:
        for q in values:
            for r in values:
                A = (p and q) or not r  
                B = not (p and (q or not r))
                if p is True:
                    p = 'T'
                else:
                    p = 'F'
                if q is True:
                    q = 'T'
                else:
                    q = 'F'
                if r is True:
                    r = 'T'
                else:
                    r = 'F'
                if B is True:
                    B = 'T'
                else:
                    B = 'F'
                if A is True:
                    A = 'T'
                else:
                    A = 'F'
                print('+---+---+---+---+---+')
                print('| ' + p + ' | ' + q + ' | ' + r +
                      ' | ' + A + ' | ' + B + ' |')
    print('+---+---+---+---+---+')


if __name__ == '__main__':
    main()
