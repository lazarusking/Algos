from sympy import symbols

class Lagrange:
    """
    Can output the equation as well when you ignore parameters in 
    lagrange() , you need to 'pip install sympy' first 
    """

    def __init__(self, x, fx) -> None:
        self.x = x
        self.fx = fx

    def lagrange(self, input=symbols("x")) -> list:
        """ f(xi)li(x)
            li(x)=∑(x-xj/xi-xj)*(x-xj/xi-xj)
                j=0
                j≠i
        """

        lagrange = 0
        # xpt = symbols("x")
        for i in range(0, len(self.x)):
            li = 1
            for j in range(len(self.x)):
                if j != i:
                    li *= (input-self.x[j]) / (self.x[i]-self.x[j])
            li *= self.fx[i]
            lagrange += li
            dictx = dict(zip(self.x, self.fx))
        print("x", "|" "f(X)")
        print("------")        
        res = [[i, v] for (i, v) in dictx.items()]
        for i in range(len(self.x)):           
            print(" : ".join(map(str, res[i])))
        print(f"At f({input}): {lagrange}")


def main():
    # Instance of Langrange class
    x = [1, 2, 3]
    fx = [86, 84, 89]
    input = 2
    # chelseaEqn = Lagrange([1, 1.25, 0.9], [0.3010, 0.4393, 0.2304])
    chelseaEqn = Lagrange(x, fx)
    chelseaEqn.lagrange()  # without input displays formula
    chelseaEqn.lagrange(input)  # at a particular point


if __name__ == "__main__":
    main()
