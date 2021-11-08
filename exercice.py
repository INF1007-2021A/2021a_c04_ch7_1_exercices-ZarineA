#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import chap6
import turtle

# TODO: Définissez vos fonction ici


def volume_masse_ellipsoide(a = 1, b = 1, c = 1, masse_volumique = 1):
    volume = 4 / 3 * math.pi * a * b * c
    return volume, volume * masse_volumique


def dessiner_arbre(nombre_branches, longueur_branche, epaisseur, angle):
    rapport_taille_branches = 4/5
    turtle.pensize(epaisseur)
    turtle.forward(longueur_branche)
    if nombre_branches > 1:
        longueur_prochaine_branche = longueur_branche * rapport_taille_branches
        prochaine_epaisseur = epaisseur * rapport_taille_branches
        prochain_angle = angle * rapport_taille_branches
        turtle.left(angle)
        dessiner_arbre(nombre_branches - 1, longueur_prochaine_branche, prochaine_epaisseur, prochain_angle)
        turtle.right(angle*2)
        dessiner_arbre(nombre_branches - 1, longueur_prochaine_branche, prochaine_epaisseur, prochain_angle)
        turtle.left(angle)
    turtle.backward(longueur_branche)
    turtle.pensize(epaisseur / rapport_taille_branches)


def valide(adn):
    somme_car_valides = adn.count('a') +  adn.count('t') + adn.count('g') + adn.count('c')
    return len(adn) != 0 and somme_car_valides == len(adn)


def saisie(texte):
    saisie = input(texte)
    while not valide(saisie):
        print("Saisie invalide")
        saisie = input(texte)
    return saisie


def proportion(chaine, sequence):
    dans_chaine = 0
    for car in sequence:
        if car in chaine:
            dans_chaine += 1
    return dans_chaine / len(sequence)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    # 1)
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    mass_volumique = int(input("Masse volumique = "))
    volume, masse = volume_masse_ellipsoide(a, b, c, mass_volumique)
    print("Volume de l'ellipsoïde :", volume)
    print("Masse de l'ellipsoïde :", masse)

    # 2)
    print("Entrez une phrase :")
    phrase = input()
    dict = chap6.frequence(phrase)
    tri = lambda dictionnaire: sorted(dictionnaire, key=dictionnaire.__getitem__)
    print("Lettre la plus fréquente :", tri(dict)[-1])

    # 3)
    turtle.color("green")
    turtle.left(90)
    dessiner_arbre(6, 50, 5, 35)
    turtle.done()

    # 4)
    sequence_ADN = saisie("Séquence d'ADN : ")
    chaine_ADN = saisie("Chaîne d'ADN : ")
    print("Proportion de sequence dans la chaine :", proportion(chaine_ADN, sequence_ADN))

