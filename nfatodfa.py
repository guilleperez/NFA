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

while(True):
     valores_estado_actual = []
     llave_nueva = ""
     nuevos_valores_estados = ""
     #print "ESTADO ACTUAL ", estado_actual
     #calcula todo con la llave nueva
     for i in range(len(estado_actual)):
         valores_estado_actual = transiciones_diccionario_0.get(estado_actual[i])
         #print "vae ",valores_estado_actual


         # crear la llave nueva
         if(len(valores_estado_actual) == 1):
             if(valores_estado_actual[0] not in llave_nueva):
                llave_nueva += " " + valores_estado_actual[0]
         else:
             for valor_llave in range(len(valores_estado_actual)):
                 if(valor_llave < len(valores_estado_actual) - 1):
                    llave_nueva += valores_estado_actual[valor_llave] + " "
                 else:
                     llave_nueva += valores_estado_actual[valor_llave]
         #print llave_nueva, " lln"


         # obtener los nuevos valores de llave
         for j in range(len(valores_estado_actual)):
             #print "j ",valores_actual[j]
             valores_estado_actual = transiciones_diccionario_0.get(valores_estado_actual[j])


             for k in valores_estado_actual:
                 if(k not in nuevos_valores_estados):
                    nuevos_valores_estados += k + " "
             #print "vea ",valores_estado_actual

     #print "nve", nuevos_valores_estados
     agregar = nuevos_valores_estados.split()

     if (transiciones_diccionario_0.get(llave_nueva)):
         break

     transiciones_diccionario_0[llave_nueva] =  agregar

     #agregara el nuevo valor de llaves a la tabla
     estado_actual = llave_nueva.split()
     #print "ea", estado_actual



print "\nCon 0 ", transiciones_diccionario_0



