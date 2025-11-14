#Pede duas frases
fraseUm = input()
fraseDois = input()

#Transforma as duas frases em conjuntos de palavras
DaPrimeira = set(fraseUm.split())
DaSegunda = set(fraseDois.split())

intersesao = DaPrimeira.intersection(DaSegunda)

ordenado = sorted(intersesao)

print(" ".join(sorted(ordenado, key=lambda isWord: (not isWord[0].isalpha()))))

