import math
import random


def elso():
    adat_lista = []
    for i in range(0, 7, 1):
        fej_iras: int = math.floor(random.random() * 2)
        adat_lista.append(fej_iras)

        if fej_iras == 1:
            if i == 6:
                print("FEJ", end="")
            else:
                print("FEJ", end="-")
        elif fej_iras == 0:
            if i == 6:
                print("ÍRÁS", end="")
            else:
                print("ÍRÁS", end="-")

    return adat_lista


def fejek_szama(lista):
    fej_osszegzo = 0
    for i in range(0, len(lista), 1):
        if lista[i] == 1:
            fej_osszegzo += 1
    return fej_osszegzo


def konzol_kiir(fejszam):
    print(f"A fejek száma: {fejszam}.")


def file_kiir(fejszam):
    fajl = open("fejek.txt", "w", encoding="utf-8")
    fajl.write(f"A fejek száma: {fejszam}.")
