#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = [input("Give a value: ") for _ in range(10)]

    return sorted(values)  # We assume values are heterogeneous


def anagrams(words: list = None) -> bool:
    if words is None:
        words = [input("Enter a word: ") for i in range(2)]

    return sorted(words[0]) == sorted(words[1])


def contains_doubles(items: list) -> bool:
    return len(items) != len(set(items))


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = sorted(student_grades.items(), key=lambda grade: sum(grade[1]) / len(grade[1]), reverse=True)[0]

    return {best_student[0]: sum(best_student[1]) / len(best_student[1])}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    frequencies = {}
    for letter in sentence:
        if letter not in frequencies:
            frequencies[letter] = 1
        else:
            frequencies[letter] += 1

    return frequencies


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recipe_name = input("Enter a recipe name: ")
    ingredients = []

    ingredient = input("Give an ingredient: ")
    while ingredient:
        ingredients.append(ingredient)
        ingredient = input("Give an ingredient: ")

    return {recipe_name: ingredients}


def print_recipe(ingredients: dict) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe

    print(ingredients.get(input("What recipe do you want to consult? "), ""))


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
