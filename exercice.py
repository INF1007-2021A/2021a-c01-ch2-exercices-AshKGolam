#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    nouv = ""
    for j in range(len(mot)):
        car = mot[j]
        car = chr(ord(car)-32)
        nouv = nouv + car

    return nouv


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
