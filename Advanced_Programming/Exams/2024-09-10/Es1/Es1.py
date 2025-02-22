from polynomial import Polynomial

if __name__ == "__main__":
    p = Polynomial(7, 0, 4, 0, 1)
    q = Polynomial(5, 0, 0, 2)
    r = Polynomial(3.20, 0, 0, 5, 6, 7)

    print(f"p: {p}\nq: {q}\nr: {r}")

    z = p + q + r
    print(f"z: {z}")

    #print("monomials: {}".format(','.join(map(lambda x: str(x), z.monomials()))))

    z = z - p - r
    print(f"z: {z}")

    a = Polynomial(-1, -2, -3, -4)
    b = Polynomial(1, 2, 3, 4)
    print(a+b)