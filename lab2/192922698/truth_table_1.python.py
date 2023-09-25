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
                p_str = 'T' if p else 'F'
                q_str = 'T' if q else 'F'
                r_str = 'T' if r else 'F'

                A = (p and q) or not r  
                B = not (p and (q or not r))

                A_str = 'T' if A else 'F'
                B_str = 'T' if B else 'F'

                print('+---+---+---+---+---+')
                print('| ' + p_str + ' | ' + q_str + ' | ' + r_str +
                      ' | ' + A_str + ' | ' + B_str + ' |')
    print('+---+---+---+---+---+')


if __name__ == '__main__':
    main()
