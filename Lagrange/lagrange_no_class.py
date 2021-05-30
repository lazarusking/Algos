import pprint


def lagrange(x, fx, input) -> list:
    """ f(xi)li(x)*f(x)
        li(x)=∑(x-xj/xi-xj)*(x-xj/xi-xj)
              j=0
              j≠i
    """

    lagrange = 0
    # fx = 84
    xpt = 2
    for i in range(0, len(x)):
        li = 1
        for j in range(len(x)):
            if j != i:
                li *= ((xpt-x[j])/(x[i]-x[j]))
        li *= fx[i]
        lagrange += li
        # print(lagrange)
        dictx = dict(zip(x, fx))
        # dicty = dict([(i, v) i for i in x, v for v in fx])
    print("x", "|" "f(X)")
    print("------")
    # pprint.pprint(dictx, compact=True, indent=8,
    #               depth=5, width=5, sort_dicts=False)
    res = [[i, v] for (i, v) in dictx.items()]
    for i in range(len(x)):
        # res = f"{x[i]:>10}, {fx[i]}"
        # res[i]
        print(" : ".join(map(str, res[i])))
    # res = [f"{i}:{v}" for i in dict]

    print(f"At f({input}): {lagrange}")


def main():

    x = [1, 2, 3]
    fx = [86, 84, 89]
    input = 2
    # chelseaEqn = Lagrange([1, 1.25, 0.9], [0.3010, 0.4393, 0.2304])
    chelseaEqn = lagrange([1, 2, 3], [86, 84, 89], input)


if __name__ == "__main__":
    main()
