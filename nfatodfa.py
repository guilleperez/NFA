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

#tabla_transiciones[transiciones[0][2]] = []
#valores_0 = transiciones_diccionario_0.get(transiciones[0][2])
#valores_1 = transiciones_diccionario_1.get(transiciones[0][2])

print tabla_transiciones
print "Con 0 ", transiciones_diccionario_0
print "Con 1 ", transiciones_diccionario_1

estado_actual = [transiciones[0][2]]
#print estado_actual

w = 0
while(w<5):
     valores_estado_actual = []
     llave_nueva = ""
     for i in range(len(estado_actual)):
         valores_actual = transiciones_diccionario_0.get(estado_actual[i])
         print "valores_actual ",valores_actual

         # crear la llave nueva

         for valor_llave in valores_actual:
             llave_nueva += valor_llave + " "
         print llave_nueva, " lln"

         nuevos_valores_estados = ""

         # obtener los nuevos valores de llave
         for j in range(len(valores_actual)):
             print "j ",valores_actual[j]
             valores_estado_actual = transiciones_diccionario_0.get(valores_actual[j])


             for k in valores_estado_actual:
                 nuevos_valores_estados += k + " "
             print "vea ",valores_estado_actual

         print "nve", nuevos_valores_estados
         agregar = nuevos_valores_estados.split()
         transiciones_diccionario_0[llave_nueva] =  agregar

     estado_actual = agregar
     print "ea", estado_actual
     w+=1


print "\nCon 0 ", transiciones_diccionario_0



