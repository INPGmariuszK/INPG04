#!/usr/bin/python
# -*- coding: utf-8 -*-


tab = [' ' for el in range(9)]


def graj():
    print("Numery pul:")
    t = [el for el in range(9)]
    pokasz(t)
    stan = ""
    p = ""
    znakzioma = ""
    znakkompa = ""
    while p != "T" and p != "N":
        p = input("Czy chcesz zaczynaci(T/N)?")
    while znakzioma != "X" and znakzioma != "O":
        znakzioma = input("Jaki ma byci twuj znak(X/O)?")
    if znakzioma == "X":
        znakkompa = "O"
    if znakzioma == "O":
        znakkompa = "X"
    if p == "T":
        while stan == "":
            ruch(znakzioma)
            pokasz(tab)
            stan = sprawdzi()
            if stan == "":
                ruchkompa(znakkompa)
                pokasz(tab)
                stan = sprawdzi()
    if p == "N":
        while stan == "":
            ruchkompa(znakkompa)
            pokasz(tab)
            stan = sprawdzi()
            if stan == "":
                ruch(znakzioma)
                pokasz(tab)
                stan = sprawdzi()
    print(stan)


def ruchkompa(znak):
    # tu powinien byci ruch kompa ale dla testuw duem to tak
    numer = input("Kliknij tu i podaj numer pola od 0 do 8")
    numer = int(numer[0])
    if tab[numer] == ' ':
        tab[numer] = znak
    else:
        print("To pole jest zajente")
        ruch(znak)


def ruch(znak):
    numer = input("Kliknij tu i podaj numer pola od 0 do 8")
    numer = int(numer[0])
    if tab[numer] == ' ':
        tab[numer] = znak
    else:
        print("To pole jest zajente")
        ruch(znak)


def pokasz(t):
    print("-------------")
    print("|", t[0], "|", t[1], "|", t[2], "|")
    print("-------------")
    print("|", t[3], "|", t[4], "|", t[5], "|")
    print("-------------")
    print("|", t[6], "|", t[7], "|", t[8], "|")
    print("-------------")


def sprawdzi():
    for el in range(3):
        if tab[el] != ' ' and tab[el] == tab[el + 3] and tab[el + 6] == tab[el + 3]:
            return "wygrau:" + tab[el]
    for el in (0, 3, 6):
        if tab[el] != ' ' and tab[el] == tab[el + 1] and tab[el] == tab[el + 2]:
            return "wygrau:" + tab[el]
    if tab[0] != ' ' and tab[0] == tab[4] and tab[8] == tab[0]:
        return "wygrau:" + tab[0]
    if tab[2] != ' ' and tab[2] == tab[4] and tab[6] == tab[2]:
        return "wygrau:" + tab[2]
    for el in tab:
        if el == ' ':
            return ""
    return "remis"


