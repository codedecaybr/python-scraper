# blocos identados
for i in range(10):
    print(i)

# if-else
for i in range(10):
    if i % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

# saída formatada
materia = "Cálculo"
print("Eu me ferrei em %s" %materia)

# iteração em vetores
materias = ["Cálculo", "Física", "Algelin", "Mecflu"]
for m in materias:
    print("Eu me ferrei em %m" %materia)

# tamanho de vetores
print( len(materias) )

# replace
base = "Já estou há ##MESES## procurando um emprego!"
meuTexto = base.replace("##MESES##", "6")
print(meuTexto)

# busca textual
"estou" in meuTexto

# split
minhaLista = meuTexto.split(" ")
print("minhaLista")
