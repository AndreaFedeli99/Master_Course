from ireduction import calculator

if __name__ == "__main__":
    expression = [
        "+34", "+3-15", "*+34-23", "+7++34+23", "^72", "-^2*32^5+23",
        "*+*34-34/6-35", "/+-81*45*/93/52", "*+/12/14-2/32", "+2*-53/63"]
    for expr in expression:
        c = calculator(expr)
        print('-----------------------------')
        print(c)
        while True:
            try:
                next(c)
            except StopIteration: break
            print(c)
        print('-----------------------------')