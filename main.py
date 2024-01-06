import sorozat
import epuletek

lista = sorozat.elso()
fejszam = sorozat.fejek_szama(lista)
print()
sorozat.konzol_kiir(fejszam)
sorozat.file_kiir(fejszam)

epulet_lista = epuletek.fajl_beolvasas()
e_szam = epuletek.epuletek_szama(epulet_lista)
print(f"Az épületek száma: {e_szam}.")

m_szam = epuletek.magas(epulet_lista)
print(f"Az 555 lábnál magasabb épületek száma: {m_szam}.")

legoregebb_orszag = epuletek.legoregebb(epulet_lista)
print(f"A legöregebb épület országa: {legoregebb_orszag}.")
