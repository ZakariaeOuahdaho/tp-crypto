

# Tables de permutation et S-boxes pour DES

# Permutation initiale (IP)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Permutation finale (IP^-1)
IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Expansion E (32 bits -> 48 bits)
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# Permutation P
P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# S-boxes (8 boîtes de substitution)
S_BOXES = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

# Permutation de choix de clé 1 (PC-1)
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Permutation de choix de clé 2 (PC-2)
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Nombre de rotations pour chaque round
ROTATIONS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def permuter(bloc, table):
    """Applique une permutation selon une table donnée"""
    return ''.join([bloc[i - 1] for i in table])


def xor(bits1, bits2):
    """Opération XOR entre deux chaînes de bits"""
    return ''.join(['0' if bits1[i] == bits2[i] else '1' for i in range(len(bits1))])


def rotation_gauche(bits, n):
    """Rotation circulaire à gauche de n positions"""
    return bits[n:] + bits[:n]


def s_box_substitution(bloc_48bits):
    """Substitution via les S-boxes (48 bits -> 32 bits)"""
    resultat = ""
    for i in range(8):
        # Extraire 6 bits pour chaque S-box
        groupe = bloc_48bits[i * 6:(i + 1) * 6]
        
        # Ligne : premier et dernier bit
        ligne = int(groupe[0] + groupe[5], 2)
        
        # Colonne : 4 bits du milieu
        colonne = int(groupe[1:5], 2)
        
        # Valeur de la S-box
        valeur = S_BOXES[i][ligne][colonne]
        
        # Convertir en binaire sur 4 bits
        resultat += format(valeur, '04b')
    
    return resultat


def fonction_f(moitie_droite, sous_cle):
    """Fonction de Feistel"""
    # Expansion de 32 à 48 bits
    etendu = permuter(moitie_droite, E)
    
    # XOR avec la sous-clé
    xor_resultat = xor(etendu, sous_cle)
    
    # Substitution via S-boxes (48 -> 32 bits)
    substitue = s_box_substitution(xor_resultat)
    
    # Permutation P
    return permuter(substitue, P)


def generer_sous_cles(cle_64bits):
    """Génère les 16 sous-clés de 48 bits"""
    # Permutation PC-1 (64 -> 56 bits)
    cle_56bits = permuter(cle_64bits, PC1)
    
    # Division en deux moitiés de 28 bits
    C = cle_56bits[:28]
    D = cle_56bits[28:]
    
    sous_cles = []
    
    for i in range(16):
        # Rotation
        C = rotation_gauche(C, ROTATIONS[i])
        D = rotation_gauche(D, ROTATIONS[i])
        
        # Concaténation et PC-2 (56 -> 48 bits)
        cle_concatenee = C + D
        sous_cle = permuter(cle_concatenee, PC2)
        sous_cles.append(sous_cle)
    
    return sous_cles


def chiffrer_bloc_des(bloc_64bits, sous_cles):
    """Chiffre un bloc de 64 bits avec DES"""
    # Permutation initiale
    bloc = permuter(bloc_64bits, IP)
    
    # Division en deux moitiés
    L = bloc[:32]
    R = bloc[32:]
    
    # 16 rounds
    for i in range(16):
        L_precedent = L
        L = R
        R = xor(L_precedent, fonction_f(R, sous_cles[i]))
    
    # Permutation finale (noter l'inversion R + L)
    bloc_final = R + L
    return permuter(bloc_final, IP_INV)


def dechiffrer_bloc_des(bloc_64bits, sous_cles):
    """Déchiffre un bloc de 64 bits avec DES"""
    # Même processus mais avec les sous-clés inversées
    sous_cles_inversees = sous_cles[::-1]
    return chiffrer_bloc_des(bloc_64bits, sous_cles_inversees)


def texte_vers_binaire(texte):
    """Convertit un texte en binaire"""
    return ''.join([format(ord(c), '08b') for c in texte])


def binaire_vers_texte(binaire):
    """Convertit du binaire en texte"""
    texte = ""
    for i in range(0, len(binaire), 8):
        octet = binaire[i:i + 8]
        if len(octet) == 8:
            texte += chr(int(octet, 2))
    return texte


def chiffrer_des(texte_clair, cle):
    """Chiffre un texte complet avec DES"""
    # Préparer la clé (doit faire 64 bits)
    cle_binaire = texte_vers_binaire(cle)
    cle_binaire = (cle_binaire + '0' * 64)[:64]
    
    # Générer les sous-clés
    sous_cles = generer_sous_cles(cle_binaire)
    
    # Convertir le texte en binaire
    texte_binaire = texte_vers_binaire(texte_clair)
    
    # Padding si nécessaire
    while len(texte_binaire) % 64 != 0:
        texte_binaire += '00000000'
    
    # Chiffrer bloc par bloc
    texte_chiffre_binaire = ""
    for i in range(0, len(texte_binaire), 64):
        bloc = texte_binaire[i:i + 64]
        bloc_chiffre = chiffrer_bloc_des(bloc, sous_cles)
        texte_chiffre_binaire += bloc_chiffre
    
    return texte_chiffre_binaire


def dechiffrer_des(texte_chiffre_binaire, cle):
    """Déchiffre un texte chiffré avec DES"""
    # Préparer la clé
    cle_binaire = texte_vers_binaire(cle)
    cle_binaire = (cle_binaire + '0' * 64)[:64]
    
    # Générer les sous-clés
    sous_cles = generer_sous_cles(cle_binaire)
    
    # Déchiffrer bloc par bloc
    texte_dechiffre_binaire = ""
    for i in range(0, len(texte_chiffre_binaire), 64):
        bloc = texte_chiffre_binaire[i:i + 64]
        bloc_dechiffre = dechiffrer_bloc_des(bloc, sous_cles)
        texte_dechiffre_binaire += bloc_dechiffre
    
    # Convertir en texte
    return binaire_vers_texte(texte_dechiffre_binaire).rstrip('\x00')


def main():
    print("="*60)
    print("Implémentation de l'algorithme DES")
    print("="*60)
    
    # Test avec un exemple
    message = "HELLO"
    cle = "SECRETKEY"
    
    print(f"\nMessage original : {message}")
    print(f"Clé             : {cle}")
    
    # Chiffrement
    message_chiffre_bin = chiffrer_des(message, cle)
    message_chiffre_hex = hex(int(message_chiffre_bin, 2))[2:].upper()
    
    print(f"\nMessage chiffré (hex) : {message_chiffre_hex}")
    print(f"Message chiffré (bin) : {message_chiffre_bin[:64]}...")
    
    # Déchiffrement
    message_dechiffre = dechiffrer_des(message_chiffre_bin, cle)
    print(f"\nMessage déchiffré : {message_dechiffre}")
    
    print("\n" + "="*60)
    print("Mode interactif")
    print("="*60)
    
    choix = input("\nChiffrer (C) ou Déchiffrer (D) ? ").upper()
    
    if choix == 'C':
        texte = input("Entrez le texte à chiffrer : ")
        cle = input("Entrez la clé (8 caractères recommandés) : ")
        
        resultat = chiffrer_des(texte, cle)
        resultat_hex = hex(int(resultat, 2))[2:].upper()
        
        print(f"\nTexte chiffré (hex) : {resultat_hex}")
        
        with open("des_chiffre.txt", "w") as f:
            f.write(resultat_hex)
        print("Résultat sauvegardé dans 'des_chiffre.txt'")
        
    elif choix == 'D':
        texte_hex = input("Entrez le texte chiffré (hex) : ")
        cle = input("Entrez la clé : ")
        
        # Convertir hex en binaire
        texte_bin = bin(int(texte_hex, 16))[2:].zfill(len(texte_hex) * 4)
        
        resultat = dechiffrer_des(texte_bin, cle)
        print(f"\nTexte déchiffré : {resultat}")
        
        with open("des_dechiffre.txt", "w") as f:
            f.write(resultat)
        print("Résultat sauvegardé dans 'des_dechiffre.txt'")
    
    else:
        print("Choix invalide!")


if __name__ == "__main__":
    main()