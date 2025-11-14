string = input()
dicionario = {}

for x in string:
    if x == " ":
        continue
    if x not in dicionario:
        dicionario[x] = 1
    else:
        dicionario[x] += 1

print(dicionario)

