import os
import sys
import json

dossier = os.path.dirname(__file__)
chemin = os.path.join(dossier, "liste.json")
if os.path.exists(chemin):
    with open(chemin, "r", encoding='utf-8') as verification:
        menu = json.load(verification)
else:
    menu = []
options = """Choisissez parmi les 5 options suivantes:\
                \n1: Ajouter un élément à la liste de courses\
                \n2: Retirer un élément de la liste de courses\
                \n3: Afficher les éléments de la liste de courses\
                \n4: Vider la liste de courses\
                \n5: Quitter le programme
          """
commandes = ["1","2","3","4","5"]
while True:
    print("_"*40)
    print(options)
    choix = input("\U0001F449 Choix: ")
    print("_"*40)
    while choix not in commandes:
        continue
    if choix == "1" :
        element = input("Entrez le nom d'un élément à ajouter à la liste de courses \U0001F449 : ")
        if element in menu:
            print(f"L'élémént {element.strip()} existe déjà dans la liste")
            continue
        else:
            while element.isdigit():
                print("\U0001F47A Vous ne pouvez pas ajouter ce type d'élément ! ")
                element = input("Entrez le nom d'un élément à ajouter à la liste de courses \U0001F449 : ")
            menu.append(element.strip())
            print(f"L'élémént {element.strip()} a bien été ajouté dans la liste ")
    elif choix=="2":
        element = input("Entrez le nom d'un élément à retirer de la liste de courses \U0001F449 : ")
        if element in menu:
            menu.remove(element)
            print(f"L'élément {element} a bien été supprimé à la liste \U0001F44D")
        else:
            print(f"\U0001F92F L'élément {element.strip()} n'est pas dans la liste")
    elif choix == "3":
        print("Les éléments de la liste de menu \U0001F9D0 : ")
        if len(menu)==0:
            print("\U0001F92F Votre liste ne contient aucun élément.")
            continue
        else:
            for i, element in enumerate(menu):
                if i==0:
                    print((str(i+1))+'. '+element)
                    continue
                else:
                    print((str(i+1))+'. '+element)
    elif choix == "4":
        menu.clear()
        print("La liste a été vidée de son contenu \U0001F44D")
    elif choix == "5":
        with open(chemin, "w", encoding='utf-8') as conserver:
            json.dump(menu, conserver, indent=4)
        print ("Bye !\nSee you again ! \U0001F44D ")
        print("_"*40)
        sys.exit()