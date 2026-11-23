def merge_sort(a):
    if len(a) <= 1:
        return a

    mijloc = len(a) // 2

    stanga = merge_sort(a[:mijloc])
    dreapta = merge_sort(a[mijloc:])

    rezultat = []
    i = 0
    j = 0

    while i < len(stanga) and j < len(dreapta):
        if stanga[i] < dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1

    while i < len(stanga):
        rezultat.append(stanga[i])
        i += 1

    while j < len(dreapta):
        rezultat.append(dreapta[j])
        j += 1

    return rezultat

a = list(map(int, input("Introdu numerele: ").split()))

print (merge_sort(a))
