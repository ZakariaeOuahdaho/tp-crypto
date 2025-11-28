import math

# Données du problème
C = 997593903573  # Message chiffré
e = 7  # Exposant public
n = 1037594094337  # Module public

print("DÉCRYPTAGE RSA - SOLUTION COMPLÈTE")
print(f"\nMessage chiffré: {C}")
print(f"Clé publique: (e={e}, n={n})")


# ÉTAPE 1 : FACTORISATION DE n

print("ÉTAPE 1 : FACTORISATION DE n")

def factoriser(n):
    """Factorise n en trouvant ses deux facteurs premiers"""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

p, q = factoriser(n)
print(f"\nFactorisation de n = {n}")
print(f"p = {p}")
print(f"q = {q}")
print(f"Vérification: {p} × {q} = {p * q}")
print(f"Correct: {p * q == n}")


# ÉTAPE 2 : CALCUL DE LA CLÉ PRIVÉE d

print("ÉTAPE 2 : CALCUL DE LA CLÉ PRIVÉE")

# Calcul de φ(n)
phi_n = (p - 1) * (q - 1)
print(f"\nφ(n) = (p-1) × (q-1)")
print(f"φ(n) = {p-1} × {q-1}")
print(f"φ(n) = {phi_n}")

# Calcul de d (inverse modulaire de e mod φ(n))
def euclide_etendu(a, b):
    """Algorithme d'Euclide étendu"""
    if b == 0:
        return a, 1, 0
    pgcd, x1, y1 = euclide_etendu(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return pgcd, x, y

def inverse_modulaire(e, phi):
    """Calcule l'inverse modulaire de e mod phi"""
    pgcd, x, _ = euclide_etendu(e, phi)
    if pgcd != 1:
        raise Exception("L'inverse modulaire n'existe pas")
    return x % phi

d = inverse_modulaire(e, phi_n)
print(f"\nCalcul de d tel que: e × d ≡ 1 (mod φ(n))")
print(f"d = {d}")
print(f"\nVérification: ({e} × {d}) mod {phi_n} = {(e * d) % phi_n}")
print(f"Correct: {(e * d) % phi_n == 1}")


# ÉTAPE 3 : DÉCHIFFREMENT DU MESSAGE

print("ÉTAPE 3 : DÉCHIFFREMENT DU MESSAGE")

def exponentiation_modulaire(base, exp, mod):
    """Calcule (base^exp) mod mod efficacement"""
    resultat = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            resultat = (resultat * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return resultat

M = exponentiation_modulaire(C, d, n)
print(f"\nMessage clair M = C^d mod n")
print(f"M = {C}^{d} mod {n}")
print(f"M = {M}")

# ÉTAPE 4 : CONVERSION EN TEXTE

print("ÉTAPE 4 : CONVERSION ASCII")

def decoder_message(nombre):
    """Décode un nombre en chaîne de caractères ASCII"""
    chaine = str(nombre)
    message = ""
    i = 0
    
    # On essaie de décoder par groupes de 2 ou 3 chiffres
    while i < len(chaine):
        # Essayer avec 3 chiffres d'abord (pour les codes 100-127)
        if i + 2 < len(chaine):
            code_3 = int(chaine[i:i+3])
            if 32 <= code_3 <= 127:
                message += chr(code_3)
                i += 3
                continue
        
        # Essayer avec 2 chiffres (pour les codes 32-99)
        if i + 1 < len(chaine):
            code_2 = int(chaine[i:i+2])
            if 32 <= code_2 <= 127:
                message += chr(code_2)
                i += 2
                continue
        
        # Si aucun ne marche, passer au suivant
        i += 1
    
    return message

# Méthode automatique
message_auto = decoder_message(M)
print(f"\nMessage numérique: {M}")
print(f"Décodage automatique: '{message_auto}'")

# Décodage manuel détaillé
print("\nDécodage détaillé:")
chaine_M = str(M)
print(f"Chaîne de chiffres: {chaine_M}")

# Essayons différents découpages
print("\nEssai de découpage par paires:")
i = 0
message_manuel = ""
while i < len(chaine_M):
    if i + 2 < len(chaine_M):
        code_3 = int(chaine_M[i:i+3])
        if 65 <= code_3 <= 90 or 97 <= code_3 <= 122:  # Lettres
            print(f"  {chaine_M[i:i+3]} → {code_3} → '{chr(code_3)}'")
            message_manuel += chr(code_3)
            i += 3
            continue
    
    if i + 1 < len(chaine_M):
        code_2 = int(chaine_M[i:i+2])
        if 65 <= code_2 <= 90 or 97 <= code_2 <= 122:  # Lettres
            print(f"  {chaine_M[i:i+2]} → {code_2} → '{chr(code_2)}'")
            message_manuel += chr(code_2)
            i += 2
            continue
    
    i += 1

print("RÉSULTAT FINAL")
print(f"\nMessage chiffré: {C}")
print(f"Clé privée: d = {d}")
print(f"Message déchiffré (numérique): {M}")
print(f"Message en clair: '{message_manuel}'")
