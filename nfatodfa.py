archivo = open("entrada.txt","r")
nfa = ""
for linea in archivo:
    nfa += linea

nfa = nfa.split(")")
#print nfa
transiciones = []
transiciones_diccionario_0 = {}
transiciones_diccionario_1 = {}
for i in range(len(nfa)-1):
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

print transiciones
for i in range(len(transiciones)):
    if(transiciones[i][0] == '0'):
        if(not transiciones_diccionario_0.has_key(transiciones[i][2])):
            estados_llegada = []
            estados_llegada.append(transiciones[i][4])
            transiciones_diccionario_0[transiciones[i][2]] = estados_llegada
        else:
            estados_llegada = transiciones_diccionario_0.get(transiciones[i][2])
            estados_llegada.append(transiciones[i][4])
            transiciones_diccionario_0[transiciones[i][2]] = estados_llegada
            #transiciones_diccionario_0.append({transiciones[i][2]: transiciones[i][4]})
    else:
        if (not transiciones_diccionario_1.has_key(transiciones[i][2])):
            estados_llegada = []
            estados_llegada.append(transiciones[i][4])
            transiciones_diccionario_1[transiciones[i][2]] = estados_llegada
        else:
            estados_llegada = transiciones_diccionario_0.get(transiciones[i][2])
            estados_llegada.append(transiciones[i][4])
            transiciones_diccionario_1[transiciones[i][2]] = estados_llegada

tabla_transiciones = {}

tabla_transiciones[transiciones[0][2]] = []
valores_0 = transiciones_diccionario_0.get(transiciones[0][2])
valores_1 = transiciones_diccionario_1.get(transiciones[0][2])
tabla_transiciones

while(True):


print tabla_transiciones
print "Con 0 ", transiciones_diccionario_0
print "Con 1 ", transiciones_diccionario_1





