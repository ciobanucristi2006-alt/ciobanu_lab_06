def insertion_sort(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1

        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j = j - 1

        a[j + 1] = x

    return a



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

try:
    f = open("date.txt", "r")
    linii = f.readlines()
    f.close()

    if len(linii) < 2:
        print("Fisierul trebuie sa contina doua linii!")

    else:
        try:
            numere = list(map(int, linii[0].split()))
            algoritm = linii[1].strip()

            if len(numere) == 0:
                print("Lista de numere este goala!")

            elif algoritm == "Insertion":
                rezultat = insertion_sort(numere.copy())

            elif algoritm == "Merge":
                rezultat = merge_sort(numere.copy())

            else:
                rezultat = None
                print("Algoritm necunoscut!")

            if rezultat is not None:
                f = open("date.txt", "a")
                f.write("\n" + algoritm + ": ")

                for x in rezultat:
                    f.write(str(x) + " ")

                f.close()

                print("Sortarea a fost realizata cu succes!")
                print(algoritm, ":", rezultat)

        except ValueError:
            print("Eroare: Introduceti doar numere intregi!")

except FileNotFoundError:
    print("Eroare: Fisierul date.txt nu exista!")