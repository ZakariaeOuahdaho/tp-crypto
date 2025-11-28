

def chiffrer_vigenere(texte, cle):
    """
    Chiffre un texte avec la méthode de Vigenère
    
    Args:
        texte: Texte à chiffrer
        cle: Clé de chiffrement (chaîne alphabétique)
    
    Returns:
        Texte chiffré
    """
    texte = texte.upper()
    cle = cle.upper()
    resultat = ""
    index_cle = 0
    
    for char in texte:
        if char.isalpha():
            # Conversion lettre -> nombre (A=0, B=1, ..., Z=25)
            pos_char = ord(char) - ord('A')
            pos_cle = ord(cle[index_cle % len(cle)]) - ord('A')
            
            # Chiffrement : (texte + clé) mod 26
            nouvelle_pos = (pos_char + pos_cle) % 26
            resultat += chr(nouvelle_pos + ord('A'))
            
            index_cle += 1
        else:
            resultat += char
    
    return resultat


def dechiffrer_vigenere(texte_chiffre, cle):
    """
    Déchiffre un texte chiffré avec Vigenère
    
    Args:
        texte_chiffre: Texte chiffré
        cle: Clé de déchiffrement
    
    Returns:
        Texte déchiffré
    """
    texte_chiffre = texte_chiffre.upper()
    cle = cle.upper()
    resultat = ""
    index_cle = 0
    
    for char in texte_chiffre:
        if char.isalpha():
            pos_char = ord(char) - ord('A')
            pos_cle = ord(cle[index_cle % len(cle)]) - ord('A')
            
            # Déchiffrement : (texte - clé) mod 26
            nouvelle_pos = (pos_char - pos_cle) % 26
            resultat += chr(nouvelle_pos + ord('A'))
            
            index_cle += 1
        else:
            resultat += char
    
    return resultat


def afficher_table_vigenere():
    """
    Affiche la table de Vigenère (carré de Vigenère)
    """
    print("\nTable de Vigenère :")
    print("   ", end="")
    for i in range(26):
        print(chr(65 + i), end=" ")
    print()
    
    for i in range(26):
        print(chr(65 + i), ":", end=" ")
        for j in range(26):
            print(chr(65 + (i + j) % 26), end=" ")
        print()


def main():
    print("="*50)
    print("Chiffrement de Vigenère")
    print("="*50)
    
    # Exemple du TP : "mastercsuemf" avec clé "clefvigenere"
    message = "mastercsuemf"
    cle = "clefvigenere"
    
    print(f"\nMessage original : {message}")
    print(f"Clé             : {cle}")
    
    # Chiffrement
    message_chiffre = chiffrer_vigenere(message, cle)
    print(f"\nMessage chiffré : {message_chiffre}")
    
    # Déchiffrement
    message_dechiffre = dechiffrer_vigenere(message_chiffre, cle)
    print(f"Message déchiffré : {message_dechiffre.lower()}")
    
    # Afficher la table
    afficher_table_vigenere()
    
    print("\n" + "="*50)
    print("Mode interactif")
    print("="*50)
    
    choix = input("\nChiffrer (C) ou Déchiffrer (D) ? ").upper()
    
    if choix == 'C':
        texte = input("Entrez le texte à chiffrer : ")
        cle = input("Entrez la clé : ")
        resultat = chiffrer_vigenere(texte, cle)
        print(f"\nTexte chiffré : {resultat}")
        
        # Sauvegarder dans un fichier
        with open("vigenere_chiffre.txt", "w") as f:
            f.write(resultat)
        print("Résultat sauvegardé dans 'vigenere_chiffre.txt'")
        
    elif choix == 'D':
        texte = input("Entrez le texte à déchiffrer : ")
        cle = input("Entrez la clé : ")
        resultat = dechiffrer_vigenere(texte, cle)
        print(f"\nTexte déchiffré : {resultat}")
        
        # Sauvegarder dans un fichier
        with open("vigenere_dechiffre.txt", "w") as f:
            f.write(resultat)
        print("Résultat sauvegardé dans 'vigenere_dechiffre.txt'")
    
    else:
        print("Choix invalide!")


if __name__ == "__main__":
    main()