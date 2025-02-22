def sm(guy_p, gal_p):
    def compute_sm(idx, guys_idx, couples):
        if len(couples) == len(guy_p):
            return couples
        guy = list(guy_p.keys())[idx]
        girl = guy_p[guy][guys_idx[guy]]
        if len(couples) == 0:
            if (gal_p[girl][0] == guy):
                print(f"💑 {girl} engages with {guy}")
                couples[girl] = guy
            return compute_sm((idx + 1) % len(guy_p.keys()), guys_idx, couples)
        if guy not in couples.values():
            if girl not in couples:
                print(f"💑 {girl} engages with {guy}")
                guys_idx[guy] += 1
                couples[girl] = guy
                return compute_sm((idx + 1) % len(guy_p.keys()), guys_idx, couples)
            if gal_p[girl].index(guy) < gal_p[girl].index(couples[girl]):
                print(f"💔 {girl} breaks with {couples[girl]} to 💑 engage with {guy}")
                guys_idx[guy] += 1
                couples[girl] = guy
                return compute_sm((idx + 1) % len(guy_p.keys()), guys_idx, couples)
            guys_idx[guy] += 1
            return compute_sm((idx + 1) % len(guy_p.keys()), guys_idx, couples)
        else:
            return compute_sm((idx + 1) % len(guy_p.keys()), guys_idx, couples)
    idx = {guy: 0 for guy in guy_p.keys()}
    return [(girl, guy) for girl, guy in compute_sm(0, idx, {}).items()]
