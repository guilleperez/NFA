archivo = open("entrada.txt","r")
nfa = ""
for linea in archivo:
    nfa += linea

nfa = nfa.split(")")
print nfa
transiciones = []
transiciones_diccionario = {}
for i in range(len(nfa)):
    estado = ""
    if(i == 0):
        for j in range(len(nfa[i])):
           if(nfa[i][j] != '{' and nfa[i][j] != '('  and nfa[i][j] != ')' and nfa[i][j] != '}'):
               estado += nfa[i][j]
    else:
        for j in range(1,len(nfa[i])):
            if (nfa[i][j] != '{' and nfa[i][j] != '(' and nfa[i][j] != ')' and nfa[i][j] != '}'):
                estado += nfa[i][j]
    transiciones.append(estado)

for i in range(len(transiciones)):
    print transiciones[i]

print transiciones


