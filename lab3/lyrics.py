"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi
"""


def lyrics(x):
    # this function print the lyrics for five different animals
    header = "Old MacDonald had a farm, ee-igh, ee-igh, oh!"
    if x == 'cow':
        print(header)
        print("And on that farm he had a cow, ee-igh, ee-igh, oh!")
        print("With a moo, moo here and a moo, moo there.")
        print("Here a moo, there a moo, everywhere a moo, moo.")
        print(header)
    elif x == 'chicken':
        print(header)
        print("And on that farm he had a chicken, ee-igh, ee-igh, oh!")
        print("With a cluck, cluck here and a cluck, cluck there.")
        print("Here a cluck, there a cluck, everywhere a cluck, cluck.")
        print(header)
    elif x == 'pig':
        print(header)
        print("And on that farm he had a pig, ee-igh, ee-igh, oh!")
        print("With a oink, oink here and a oink, oink there.")
        print("Here a oink, there a oink, everywhere a oink, oink.")
        print(header)
    elif x == 'sheep':
        print(header)
        print("And on that farm he had a sheep, ee-igh, ee-igh, oh!")
        print("With a baa, baa here and a baa, baa there.")
        print("Here a baa, there a baa, everywhere a baa, baa.")
        print(header)
    elif x == 'duck':
        print(header)
        print("And on that farm he had a duck, ee-igh, ee-igh, oh!")
        print("With a quack, quack here and a quack, quack there.")
        print("Here a quack, there a quack, everywhere a quack, quack.")
        print(header)


def main():
    x = 'cow'
    lyrics(x)
    x = 'chicken'
    lyrics(x)
    x = 'pig'
    lyrics(x)
    x = 'sheep'
    lyrics(x)
    x = 'duck'
    lyrics(x)


if __name__ == '__main__':
    main()
