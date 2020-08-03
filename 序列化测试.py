import pickle as p


def a():
    print(1 + 1)


if __name__ == '__main__':
    s = a
    p.dump(s, open("a.def", "wb"))

    ss = p.load(open("a.def"))
    ss()
