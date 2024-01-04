jatekos_nev:str = str(input("Játékos neve: "))
szerepkor:str = str(input("szerepkör: "))

if szerepkor == "varázsló":
    print(f"Üdvözlünk {jatekos_nev}, 2 életed van!")
elif szerepkor == "harcos":
    print(f"Üdvözlünk {jatekos_nev}, 10 életed van!")
else:
    print(f"Üdvözlünk {jatekos_nev}, 8 életed van!")