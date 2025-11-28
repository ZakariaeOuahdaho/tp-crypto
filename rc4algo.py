text="salut amine comment allez vous "
key="simozihi"


def RC4 (key,text) :
    S = list(range(256))
    j=0
    for i in range (0,255):
        j= (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    print(S[:25])
    resultat=""

    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        resultat += chr(ord(char) ^ K)
    
    print(S[:25])

    return resultat


enc=RC4(key,text)
print(enc)

decrypt=RC4(key,enc)
print(decrypt)
