from peano import zero, succ, add, sub, mult, div, convert, evaluate, NegativeNumber, DivisionByZero

if __name__ == "__main__":
    z = zero()
    one = succ(zero())
    two = succ(succ(zero()))
    three = succ(succ(succ(zero())))
    print(f"Zero :- {z}\nOne :- {one}\nTwo :- {two}\nThree :- {three}\n")
    print(f"0 :- {evaluate(z)}\nsucc(0) :- {evaluate(one)}\nsucc(succ(0)) :- {evaluate(two)}\nsucc(succ(succ(0))) :- {evaluate(three)}\n")

    print(f"15 + 8 = 23 :- {evaluate(add(convert(15), convert(8)))}")
    print(f"25 - 7 = 18 :- {evaluate(sub(convert(25), convert(7)))}")
    print("5 - 23 = -18 :-")
    try:
        print(evaluate(sub(convert(5), convert(23))), "\n")
    except NegativeNumber:
        print("Subtraction must return a positive number!\n")

    print(f"7 * 6 = 42 :- {evaluate(mult(convert(7), convert(6)))}")
    print(f"28 / 7 = 4 :- {evaluate(div(convert(28), convert(7)))}")
    print(f"25 / 2 = 12 :- {evaluate(div(convert(25), convert(2)))}")
    print("50 / 0 = err :-")
    try:
        print(evaluate(div(convert(50), convert(0))), "\n")
    except DivisionByZero:
        print("Division by 0 is undefined!")