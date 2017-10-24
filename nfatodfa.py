archivo = open("entrada.txt","r")
nfa = ""
for linea in archivo:
    nfa += linea

nfa = nfa.split(")")
print nfa
transiciones = []

for i in range(len(nfa)):
    estado = ""
    for j in range(len(nfa[i])):
       if(nfa[i][j] != '{' and nfa[i][j] != '('  and nfa[i][j] != ')' and nfa[i][j] != '}'):
           estado += nfa[i][j]
    transiciones.append(estado)

print transiciones


