text="test"
decalage=int(input("enter le num de décalage"))

def cesar (text,decalage):
    resultat= ""
    for i in text:
        resultat += chr((ord(i) - ord('a') + decalage) % 26 + ord('a'))
    return resultat

def decrypt(text, decalage):
    resultat = ""
    for i in text:
        resultat += chr((ord(i) - ord('a') - decalage) % 26 + ord('a'))
    return resultat

encripter= cesar(text,decalage)
print(encripter)

decrypter = decrypt(encripter, decalage)
print("Texte décrypté:", decrypter)
    
