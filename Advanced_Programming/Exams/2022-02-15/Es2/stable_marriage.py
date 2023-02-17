
def check_propose(w_key, w_pref, current_suitors, proposal):
    m_index = w_pref.index(proposal)
    if w_key in current_suitors:
        return m_index < current_suitors[w_key]
    else:
        return True

def find_stable(men, women):
    def update_structures(props, r, um):
        if len(props) > 0:
            if props[0][1] in r.keys():
                old_proposal_index = r[props[0][1]]
                r[props[0][1]] = women[props[0][1]].index(props[0][0])
                um.append(women[props[0][1]][old_proposal_index])
            else:
                r.update({props[0][1]: women[props[0][1]].index(props[0][0])})

            um.remove(props[0][0])

            update_structures(props[1:], r, um)

    def update_prop_pool(props, props_pool):
        if len(props) > 0:
            props_pool[props[0][0]] += 1
            update_prop_pool(props[1:], props_pool)

    def search_couples(res, prop_pool, uncoupled_men):
        if len(uncoupled_men) == 0:
            return res
        requests = [(m_key, men[m_key][prop_pool[m_key]]) for m_key in uncoupled_men]
        accepted_proposal = [r for r in requests if check_propose(r[1], women[r[1]], res, r[0])]
        update_structures(accepted_proposal, res, uncoupled_men)
        update_prop_pool(requests, prop_pool)
        return search_couples(res, prop_pool, uncoupled_men)

    couples = search_couples({}, {k: 0 for k in men.keys()}, list(men.keys()))
    return '\n'.join(["({},{})".format(k, women[k][v]) for k, v in couples.items()])