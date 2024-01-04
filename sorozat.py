import math
import random


def elso():
    for i in range(0, 7, 1):
        fej_iras: int = math.floor(random.random() * 2 + 1)
        if fej_iras == 1:
            if i == 6:
                print("FEJ", end="")
            else:
                print("FEJ", end="-")
        elif fej_iras == 2:
            if i == 6:
                print("ÍRÁS", end="")
            else:
                print("ÍRÁS", end="-")
