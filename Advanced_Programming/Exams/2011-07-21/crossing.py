country_borders = {
                    'portugal': ['spain'],
                    'andorra': ['france', 'spain'],
                    'spain': ['portugal', 'andorra', 'france'],
                    'france': ['andorra', 'spain', 'monaco', 'switzerland', 'italy', 'luxembourg', 'belgium', 'germany'],
                    'monaco': ['france'],
                    'italy': ['switzerland', 'san marino', 'vatican city', 'austria', 'slovenia', 'france'],
                    'switzerland': ['italy', 'liechtenstein', 'austria', 'france', 'germany'],
                    'liechtenstein': ['switzerland', 'austria'],
                    'luxembourg': ['france', 'belgium', 'germany'],
                    'belgium': ['france', 'luxembourg', 'netherlands', 'germany'],
                    'netherlands': ['belgium', 'germany'],
                    'united kingdom': ['ireland'],
                    'ireland': ['united kingdom'],
                    'iceland': [],
                    'denmark': ['germany'],
                    'germany': ['netherlands', 'belgium', 'luxembourg', 'france', 'switzerland', 'austria', 'czech republic', 'poland', 'denmark'],
                    'austria': ['liechtenstein', 'switzerland', 'slovenia', 'italy', 'hungary', 'slovakia', 'czech republic', 'germany'],
                    'slovenia': ['italy', 'austria', 'croatia', 'hungary'],
                    'czech republic': ['austria', 'germany', 'poland', 'slovakia'],
                    'poland': ['germany', 'czech republic', 'slovakia', 'ukraine', 'belarus', 'lithuania', 'russia'],
                    'san marino': ['italy'],
                    'vatican city': ['italy'],
                    'slovakia': ['austria', 'hungary', 'ukraine', 'poland', 'czech republic'],
                    'hungary': ['austria', 'croatia', 'serbia', 'romania', 'ukraine', 'slovakia', 'slovenia'],
                    'croatia': ['slovenia', 'bosnia and herzegovina', 'hungary', 'serbia', 'montenegro'],
                    'bosnia and herzegovina': ['croatia', 'serbia', 'montenegro'],
                    'montenegro': ['bosnia and herzegovina', 'serbia', 'albania', 'croatia'],
                    'albania': ['montenegro', 'serbia', 'macedonia', 'greece'],
                    'greece': ['albania', 'macedonia', 'bulgaria'],
                    'macedonia': ['albania', 'greece', 'bulgaria', 'serbia'],
                    'bulgaria': ['greece', 'macedonia', 'serbia', 'romania'],
                    'serbia': ['croatia', 'bosnia and herzegovina', 'montenegro', 'albania', 'macedonia', 'bulgaria', 'romania', 'hungary'],
                    'romania': ['hungary', 'serbia', 'bulgaria', 'moldova', 'ukraine'],
                    'moldova': ['romania', 'ukraine'],
                    'ukraine': ['moldova', 'romania', 'hungary', 'slovakia', 'poland', 'belarus', 'russia'],
                    'belarus': ['poland', 'ukraine', 'russia', 'latvia', 'lithuania'],
                    'lithuania': ['latvia', 'belarus', 'poland', 'russia'],
                    'latvia': ['lithuania', 'belarus', 'estonia', 'russia'],
                    'estonia': ['russia', 'latvia'],
                    'russia': ['finland', 'estonia', 'latvia', 'belarus', 'ukraine', 'norway', 'poland', 'lithuania'],
                    'finland': ['russia', 'sweden', 'norway'],
                    'sweden': ['norway', 'finland'],
                    'norway': ['sweden', 'finland', 'russia']
                }

def border(country, n):
    i = 0
    new_borders = set(country_borders[country])
    while i < n:
        yield new_borders
        s = set(c for key in new_borders for c in country_borders[key])
        new_borders = s.difference(new_borders)
        i += 1

def crossing(country, n):
    visited_countries  = res = set([country])
    for borders in border(country, n):
        visited_countries = visited_countries.union(res)
        res = borders.difference(visited_countries)
    return res