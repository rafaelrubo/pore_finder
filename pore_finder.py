# pore_finder - Code that generates matrices and find porosity from RGB values of an image (1st line-R, 2nd line-G, 3rd line-B)

arquivo = open("poros.txt", "r")

dados = arquivo.readline()
matriz = [[0,0,0]]

while dados != "" :
    numero1 = 0
    numero2 = 0
    numero3 = 0
    contador = 0
    vetor_RGB = [0,0,0]
    for i in range(len(dados)) :
        if dados[i] != "\n" :
            numero1 = numero1 * 10 + int(dados[i])
        else:
            dados = arquivo.readline()
    for i in range(len(dados)) :
        if dados[i] != "\n" :
            numero2 = numero2 * 10 + int(dados[i])
        else:
            dados = arquivo.readline()
    for i in range(len(dados)) :
        if dados[i] != "\n" :
            numero3 = numero3 * 10 + int(dados[i])
        else:
            vetor_RGB = [numero1, numero2, numero3]
            matriz.append(vetor_RGB)
            contador = contador + 1
            numero1 = 0
            numero2 = 0
            numero3 = 0
            dados = arquivo.readline()

poro = 0.0
for i in range(len(matriz)):
    if matriz[i][0] < 240 and matriz[i][1] < 240 and matriz[i][2] < 240 :
        poro = poro + 1

porosidade = poro / len(matriz)

print ('porosidade = ')
print (porosidade)
