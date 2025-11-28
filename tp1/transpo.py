

def chiffrer_transposition(texte, longueur_cle, ordre_permutation):
    """
    Chiffre un texte par la méthode de transposition
    
    Args:
        texte: Texte à chiffrer
        longueur_cle: Nombre de colonnes (ex: 4)
        ordre_permutation: Ordre de lecture des colonnes (ex: [3,2,5,1,4])
    
    Returns:
        Texte chiffré
    """
    # Nettoyer le texte (enlever espaces et mettre en majuscules)
    texte = texte.replace(" ", "").upper()
    
    # Compléter le texte si nécessaire avec des 'X'
    while len(texte) % longueur_cle != 0:
        texte += 'X'
    
    # Nombre de lignes
    nb_lignes = len(texte) // longueur_cle
    
    # Créer la matrice
    matrice = []
    index = 0
    for i in range(nb_lignes):
        ligne = []
        for j in range(longueur_cle):
            ligne.append(texte[index])
            index += 1
        matrice.append(ligne)
    
    # Afficher la matrice pour debug
    print("\nMatrice de transposition :")
    print("  ", end="")
    for i in range(longueur_cle):
        print(f"Col{i+1}", end=" ")
    print()
    
    for i, ligne in enumerate(matrice):
        print(f"L{i+1}: ", end="")
        for char in ligne:
            print(f" {char}  ", end=" ")
        print()
    
    # Lire les colonnes selon l'ordre de permutation
    texte_chiffre = ""
    for col_num in ordre_permutation:
        # col_num est 1-indexé, donc on soustrait 1
        col_index = col_num - 1
        for ligne in matrice:
            if col_index < len(ligne):
                texte_chiffre += ligne[col_index]
    
    return texte_chiffre


def dechiffrer_transposition(texte_chiffre, longueur_cle, ordre_permutation):
    """
    Déchiffre un texte chiffré par transposition
    
    Args:
        texte_chiffre: Texte chiffré
        longueur_cle: Nombre de colonnes
        ordre_permutation: Ordre utilisé pour le chiffrement
    
    Returns:
        Texte déchiffré
    """
    texte_chiffre = texte_chiffre.upper()
    nb_lignes = len(texte_chiffre) // longueur_cle
    
    # Créer une matrice vide
    matrice = [['' for _ in range(longueur_cle)] for _ in range(nb_lignes)]
    
    # Remplir la matrice en suivant l'ordre inverse de permutation
    index = 0
    for col_num in ordre_permutation:
        col_index = col_num - 1
        for i in range(nb_lignes):
            matrice[i][col_index] = texte_chiffre[index]
            index += 1
    
    # Lire la matrice ligne par ligne
    texte_dechiffre = ""
    for ligne in matrice:
        for char in ligne:
            texte_dechiffre += char
    
    return texte_dechiffre.rstrip('X')  # Enlever les 'X' de padding


def inverser_permutation(ordre):
    """
    Calcule l'ordre inverse d'une permutation
    
    Args:
        ordre: Liste représentant l'ordre de permutation
    
    Returns:
        Permutation inverse
    """
    inverse = [0] * len(ordre)
    for i, val in enumerate(ordre):
        inverse[val - 1] = i + 1
    return inverse


def main():
    print("="*50)
    print("Chiffrement par Transposition Classique")
    print("="*50)
    
    # Paramètres de la clé du TP : (4, {3,2,5,1,4})
    longueur_cle = 4
    ordre_permutation = [3, 2, 5, 1, 4]
    
    print(f"\nClé de transposition :")
    print(f"  - Longueur : {longueur_cle}")
    print(f"  - Ordre de permutation : {ordre_permutation}")
    
    # Exemple
    message = "HELLO WORLD THIS IS A TEST MESSAGE"
    
    print(f"\nMessage original : {message}")
    
    # Chiffrement
    message_chiffre = chiffrer_transposition(message, longueur_cle, ordre_permutation)
    print(f"\nMessage chiffré : {message_chiffre}")
    
    # Déchiffrement
    message_dechiffre = dechiffrer_transposition(message_chiffre, longueur_cle, ordre_permutation)
    print(f"\nMessage déchiffré : {message_dechiffre}")
    
    print("\n" + "="*50)
    print("Mode interactif")
    print("="*50)
    
    choix = input("\nChiffrer (C) ou Déchiffrer (D) ? ").upper()
    
    if choix == 'C':
        texte = input("Entrez le texte à chiffrer : ")
        
        # Utiliser la clé par défaut ou personnalisée
        utiliser_defaut = input("Utiliser la clé par défaut (4, {3,2,5,1,4}) ? (O/N) : ").upper()
        
        if utiliser_defaut == 'N':
            longueur_cle = int(input("Entrez la longueur de la clé : "))
            ordre_str = input(f"Entrez l'ordre de permutation (ex: 3,2,5,1,4) : ")
            ordre_permutation = [int(x.strip()) for x in ordre_str.split(',')]
        
        resultat = chiffrer_transposition(texte, longueur_cle, ordre_permutation)
        print(f"\nTexte chiffré : {resultat}")
        
        # Sauvegarder
        with open("transposition_chiffre.txt", "w") as f:
            f.write(resultat)
        with open("transposition_cle.txt", "w") as f:
            f.write(f"Longueur: {longueur_cle}\n")
            f.write(f"Ordre: {','.join(map(str, ordre_permutation))}\n")
        print("Résultat sauvegardé dans 'transposition_chiffre.txt'")
        print("Clé sauvegardée dans 'transposition_cle.txt'")
        
    elif choix == 'D':
        texte = input("Entrez le texte à déchiffrer : ")
        
        utiliser_defaut = input("Utiliser la clé par défaut (4, {3,2,5,1,4}) ? (O/N) : ").upper()
        
        if utiliser_defaut == 'N':
            longueur_cle = int(input("Entrez la longueur de la clé : "))
            ordre_str = input(f"Entrez l'ordre de permutation : ")
            ordre_permutation = [int(x.strip()) for x in ordre_str.split(',')]
        
        resultat = dechiffrer_transposition(texte, longueur_cle, ordre_permutation)
        print(f"\nTexte déchiffré : {resultat}")
        
        with open("transposition_dechiffre.txt", "w") as f:
            f.write(resultat)
        print("Résultat sauvegardé dans 'transposition_dechiffre.txt'")
    
    else:
        print("Choix invalide!")


if __name__ == "__main__":
    main()