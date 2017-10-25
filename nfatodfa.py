def calcular_transiciones(transiciones_diccionario,  i):
     estado_actual = estados[0]
     valor = i
     # Corrige los valores de 0 y 1
     while (True):
         llave_nueva_0= ""
         llave_nueva_1 = ""
         nuevos_valores_estados_0 = ""
         nuevos_valores_estados_1 = ""
         print "ESTADO ACTUAL ", estado_actual
         # calcula todo con la llave nueva

         for i in range(len(estado_actual)):
             valores_estado_actual_0 = transiciones_diccionario_0.get(estado_actual[i])
             valores_estado_actual_1 = transiciones_diccionario_1.get(estado_actual[i])
             print "vae ",valores_estado_actual_0 , " " , valores_estado_actual_1

             # crear la llave nueva para 0
             if (len(valores_estado_actual_0) == 1):
                 if (valores_estado_actual_0[0] not in llave_nueva_0):
                     llave_nueva_0 += " " + valores_estado_actual_0[0]
             else:
                 for valor_llave in range(len(valores_estado_actual_0)):
                     if (valor_llave < len(valores_estado_actual_0) - 1):
                         llave_nueva_0 += valores_estado_actual_0[valor_llave] + " "
                     else:
                         llave_nueva_0 += valores_estado_actual_0[valor_llave]
             #print llave_nueva, " lln"

             # crear la llave nueva para 1
             if (len(valores_estado_actual_1) == 1):
                 if (valores_estado_actual_1[0] not in llave_nueva_1):
                    llave_nueva_1 += " " + valores_estado_actual_1[0]
                 else:
                     for valor_llave_1 in range(len(valores_estado_actual_1)):
                            if (valor_llave_1 < len(valores_estado_actual_1) - 1):
                                llave_nueva_1 += valores_estado_actual_1[valor_llave] + " "
                            else:
                                llave_nueva_1 += valores_estado_actual_1[valor_llave]

             if (valores_estado_actual_0 != None):

                 # obtener los nuevos valores de llave
                 for j in range(len(valores_estado_actual_0)):
                     # print "j ",valores_actual[j]
                     valores_estado_actual_0 = transiciones_diccionario_0.get(valores_estado_actual_0[j])

                     for k in valores_estado_actual_0:
                         if (k not in nuevos_valores_estados_0):
                            nuevos_valores_estados_0 += k + " "
                            # print "vea ",valores_estado_actual

             if (valores_estado_actual_1 != None):
                 # obtener los nuevos valores de llave 1
                 for j in range(len(valores_estado_actual_1)):
                     valores_estado_actual_1 = transiciones_diccionario_1.get(valores_estado_actual_1[j])
                     if (valores_estado_actual_1 != None):
                         for k in valores_estado_actual_1:
                            if (k not in nuevos_valores_estados_1):
                                nuevos_valores_estados_1 += k + " "
                             # print "vea ",valores_estado_actual
         # print "nve", nuevos_valores_estados
         #print llave_nueva, " lln"
         if (transiciones_diccionario.get(llave_nueva_0)):
             break


         agregar_0 = nuevos_valores_estados_0.split()
         agregar_1 = nuevos_valores_estados_1.split()

         agregar = []
         agregar.append(agregar_0)
         agregar.append(agregar_1)
         transiciones_diccionario[llave_nueva_0] = agregar


         # agregara el nuevo valor de llaves a la tabla
         estado_actual = llave_nueva_0.split()
         # print "ea", estado_actual

     return transiciones_diccionario


archivo = open("entrada.txt","r")
nfa = ""
for linea in archivo:
    nfa += linea

nfa = nfa.split(")")
#print nfa
transiciones = []
estados = []
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

    if(not estados.__contains__(transiciones[i][4])):
        estados.append(transiciones[i][4])

    if(transiciones[i][0] == '0'):
        if(not transiciones_diccionario_0.has_key(transiciones[i][2])):
            estados_llegada = []
            estados_llegada.append(transiciones[i][4])
            transiciones_diccionario_0[transiciones[i][2]] = estados_llegada
        else:
            estados_llegada = transiciones_diccionario_0.get(transiciones[i][2])
            estados_llegada.append(transiciones[i][4])
            transiciones_diccionario_0[transiciones[i][2]] = estados_llegada
    else:
        if (not transiciones_diccionario_1.has_key(transiciones[i][2])):
            estados_llegada = []
            estados_llegada.append(transiciones[i][4])
            transiciones_diccionario_1[transiciones[i][2]] = estados_llegada
        else:
            estados_llegada = transiciones_diccionario_0.get(transiciones[i][2])
            estados_llegada.append(transiciones[i][4])
            transiciones_diccionario_1[transiciones[i][2]] = estados_llegada


print "Con 0 ", transiciones_diccionario_0
print "Con 1 ", transiciones_diccionario_1

transiciones_diccionario = {}

for transiciones in transiciones_diccionario_0:
    if(not transiciones_diccionario_0.get(transiciones)):
        transiciones_diccionario[transiciones] = transiciones_diccionario_0.get(transiciones)
    else:
        v = []
        values = transiciones_diccionario_0.get(transiciones)
        v.append(values)
        values = transiciones_diccionario_1.get(transiciones)
        v.append(values)
        transiciones_diccionario[transiciones] = v
print "Estados ", estados

#transiciones_diccionario_0 = calcular_transiciones(transiciones_diccionario_0, transiciones_diccionario_0)
#transiciones_diccionario_1 = calcular_transiciones(transiciones_diccionario_0, transiciones_diccionario_1)

calcular_transiciones(transiciones_diccionario, 0)
print "\nCon 0  ", transiciones_diccionario




