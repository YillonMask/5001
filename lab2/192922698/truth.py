"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi 
"""


def main():
    header = '+---+---+---+---+---+'
    print(header)
    print('| p | q | r | A | B |')
    #values = [False, True]
    for p in range(0, 2, 1):
        for q in range(0, 2, 1):
            for r in range(0, 2, 1):
                A = (p and q) or not r  
                B = not (p and (q or not r))
                if p == 1:
                    p = 'T'
                else:
                    p = 'F'
                if q == 1:
                    q = 'T'
                else:
                    q = 'F'
                if r == 1:
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
