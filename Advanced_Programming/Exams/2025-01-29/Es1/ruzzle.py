filename = "C:/Dev/VsCProject/Master_Course/Advanced_Programming/Exams/2025-01-29/Es1/dictionary.txt"

def ruzzles(grid):
    def search(w_founded, visited, row, col):
        if not ( (0 <= row < 4) and (0 <= col < 4) ) or ((row, col) in visited): return {w_founded}
        new_words = set()
        for step_r in range(-1, 2):
            for step_c in range(-1, 2):
                new_visited = visited | {(row, col)}
                if abs(step_r) != abs(step_c):
                    new_words |= search(w_founded+grid[row][col], new_visited, row+step_r, col+step_c)
        return new_words

    with open(filename) as f:
        words = list(filter(lambda w: 3 <= len(w) <= 16, [word.strip() for word in f]))

    founded = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            founded |= search("", set(), i, j)
    return sorted(filter(lambda w: w in words, founded))

