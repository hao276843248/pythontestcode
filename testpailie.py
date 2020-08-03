def group_elements(eles):
    if len(eles) == 1:
        yield (eles,)
        return

    for g_tuple in group_elements(eles[1:]):
        yield (eles[:1],) + g_tuple

        for i in range(len(g_tuple)):
            yield (
                    g_tuple[:i]
                    + ((eles[:1] + g_tuple[i]),)
                    + g_tuple[i + 1:]
            )


if __name__ == '__main__':
    a = []
    k = 0
    for j in group_elements((1, 2, 3)):
        a.append(j)
        if len(j) == 2:
            k += 1
            print(j)
    print(k)
    print(len(a))


    # x = c41 +
