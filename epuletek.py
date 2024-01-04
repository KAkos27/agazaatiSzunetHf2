from Epulet import Epulet


def fajl_beolvasas():
    epuletek = []
    fajl = open("epulet.txt", "r", encoding="utf-8")
    fajl.readline()
    epulet_lista = fajl.readlines()
    fajl.close()

    for i in range(0, len(epulet_lista), 1):
        sor_lista = epulet_lista[i].strip()
        sor_lista = sor_lista.split("$")
        epulet = Epulet(
            sor_lista[0],
            sor_lista[1],
            sor_lista[2],
            sor_lista[3],
            sor_lista[4],
            sor_lista[5],
        )
        epuletek.append(epulet)

    return epuletek


def epuletek_szama(lista):
    return len(lista)


def magas(lista):
    osszegzo = 0
    for i in range(0, len(lista), 1):
        lab_meter = float(lista[i].magassag.replace(",", ".")) * 3.280839895
        if lab_meter > 555:
            osszegzo += 1
    return osszegzo
