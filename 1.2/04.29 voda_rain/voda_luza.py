def voda_search(voda):
    if not voda:
        return 0
    l, r = 0, len(voda) - 1
    maximus, maxumam = voda[l], voda[r]
    voda_izmerenie = 0
    while l < r:
        if maximus >= maxumam:
            voda_izmerenie += maxumam - voda[r]
            r -= 1
            maxumam = max(maxumam, voda[r])
        else:
            voda_izmerenie += maximus - voda[l]
            l += 1
            maximus = max(maximus, voda[l])
    return voda_izmerenie
print(voda_search([8, 0, 2, 7, 3, 8, 6, 1, 5, 6]))