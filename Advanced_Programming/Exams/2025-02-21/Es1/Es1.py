from sm import sm

if __name__ == "__main__":
    guyprefers = {
        'abe': ['abi', 'eve', 'isa', 'ivy', 'jan', 'dee', 'fay', 'bea', 'lin', 'may'],
        'bob': ['isa', 'lin', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'may'],
        'col': ['lin', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'may', 'isa', 'jan'],
        'dan': ['ivy', 'fay', 'dee', 'may', 'lin', 'eve', 'jan', 'bea', 'isa', 'abi'],
        'gav': ['may', 'eve', 'ivy', 'bea', 'isa', 'abi', 'dee', 'lin', 'jan', 'fay'],
        'hal': ['abi', 'eve', 'lin', 'fay', 'ivy', 'isa', 'jan', 'bea', 'may', 'dee'],
        'ian': ['lin', 'isa', 'dee', 'may', 'bea', 'abi', 'fay', 'ivy', 'lin', 'may'],
        'ike': ['jan', 'dee', 'bea', 'isa', 'fay', 'eve', 'abi', 'ivy', 'lin', 'may'],
        'jon': ['abi', 'fay', 'jan', 'may', 'eve', 'bea', 'dee', 'isa', 'ivy', 'lin'],
        'joy': ['bea', 'abi', 'dee', 'may', 'eve', 'ivy', 'isa', 'jan', 'lin', 'fay'],
    }

    galprefers = {
        'abi': ['bob', 'joy', 'jon', 'gav', 'ian', 'abe', 'dan', 'ike', 'col', 'hal'],
        'bea': ['bob', 'abe', 'col', 'joy', 'gav', 'dan', 'ian', 'ike', 'jon', 'hal'],
        'isa': ['joy', 'bob', 'ike', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
        'dee': ['joy', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ike'],
        'eve': ['jon', 'hal', 'joy', 'dan', 'abe', 'gav', 'col', 'ike', 'ian', 'bob'],
        'fay': ['bob', 'abe', 'ike', 'ian', 'jon', 'dan', 'joy', 'gav', 'col', 'hal'],
        'may': ['jon', 'gav', 'hal', 'joy', 'bob', 'abe', 'col', 'ike', 'dan', 'ian'],
        'lin': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ike', 'col', 'joy'],
        'ivy': ['ian', 'col', 'hal', 'gav', 'joy', 'bob', 'abe', 'ike', 'jon', 'dan'],
        'jan': ['ike', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'joy', 'dan'],
    }

    print("Engagements!")
    couples = sm(guyprefers, galprefers)
    print(f"{chr(10)}Final Couples")
    print(chr(10).join([f"  · {guy} 💑 {gal}" for gal, guy in sorted(couples, key = lambda e: e[1])]))
