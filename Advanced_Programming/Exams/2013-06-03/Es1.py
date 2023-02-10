def palin(s):
    def _palin(st):
        if len(st) <= 1: return []
        if st[0] == st[-1]: return _palin(st[1:-1])
        return min([st[-1]]+_palin(st[:-1]),[st[0]]+_palin(st[1:]),key=lambda x:len(x))
    chars = _palin(s)
    basic_msg = f"The word <<{s}>> needs {len(chars)} insertions to become palindrome"
    return basic_msg if len(chars) == 0 else basic_msg + f": {chars}"


if __name__ == "__main__":
    print(palin("casa"))
    print(palin("otto"))
    print(palin("palindromo"))
    print(palin("posero"))
    print(palin("coccinella"))
