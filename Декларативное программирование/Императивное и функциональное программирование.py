def keep_odds_from_odds(spisok):
    j = len(spisok) - 1
    while j >= 0:
        if j % 2:
            spisok.pop(j)
        else:
            i = len(spisok[j]) - 1
            while i >= 0:
                if i % 2:
                    spisok[j].pop(i)
                i -= 1
        j -= 1


def odds_from_odds(spisok):
    res = []
    for key, value in enumerate(spisok):
        if not key % 2:
            res.append([])
            for k, v in enumerate(value):
                if not k % 2:
                    res[-1].append(v)
    return res

# END
