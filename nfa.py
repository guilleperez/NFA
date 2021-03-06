#encoding: UTF-8
#Equipo
#Guillermo Pérez Trueba A01377162
#Mauricio Maximiliano Përez Pérez A01371473

def calcular_transiciones():
    estados_actual = [estados[0]]
    while (True):
        for k in estados_actual:
            estado_actual = k
            # valores que toma el estado con 0 y 1

            estado_actual_0 = []
            estado_actual_1 = []
            for i in estado_actual:
                if (i != " "):
                    # valor en 0 y 1
                    if (transiciones_diccionario.get(i)[0] != None):
                        for j in transiciones_diccionario.get(i)[0]:
                            if (j not in estado_actual_0):
                                estado_actual_0.append(j)
                    if (transiciones_diccionario.get(i)[1] != None):
                        for j in transiciones_diccionario.get(i)[1]:
                            if (j not in estado_actual_1):
                                estado_actual_1.append(j)

            # agregar estado actual al diccionario
            if (not transiciones_diccionario.get(estado_actual)):
                agregar = []
                agregar.append(estado_actual_0)
                agregar.append(estado_actual_1)
                transiciones_diccionario[estado_actual] = agregar

            llave_0 = ""
            llave_1 = ""

            # crea llave de 0
            for i in range(len(estado_actual_0)):
                if (i < len(estado_actual_0) - 1):
                    llave_0 += estado_actual_0[i] + " "
                else:
                    llave_0 += estado_actual_0[i]

            # crea llave de 1
            for i in range(len(estado_actual_1)):
                if (i < len(estado_actual_1) - 1):
                    llave_1 += estado_actual_1[i] + " "
                else:
                    llave_1 += estado_actual_1[i]

            valores_0 = []
            valores_0_1 = []
            valores_1 = []
            valores_1_1 = []
            # crea los caminos que tomara el estado con 0
            if (estado_actual_0 != None):
                # 0
                for i in (estado_actual_0):
                    t = transiciones_diccionario.get(i)[0]
                    if (t != None):
                        for j in t:
                            if not valores_0.__contains__(j):
                                valores_0.append(j)
                # 1
                for i in (estado_actual_0):
                    t = transiciones_diccionario.get(i)[1]
                    if (t != None):
                        for j in t:
                            if not valores_0_1.__contains__(j):
                                valores_0_1.append(j)

            # crea los caminos que tomara el estado con 1
            if (estado_actual_1 != None):
                # 0
                for i in (estado_actual_1):
                    t = transiciones_diccionario.get(i)[0]
                    if (t != None):
                        for j in t:
                            if not valores_1.__contains__(j):
                                valores_1.append(j)
                 # 1
                for i in (estado_actual_1):
                    t = transiciones_diccionario.get(i)[1]
                    if (t != None):
                        for j in t:
                            if not valores_1_1.__contains__(j):
                                valores_1_1.append(j)

            # agregar llave al diccionario
            if (not transiciones_diccionario.get(llave_0)):
                agregar = []
                agregar.append(valores_0)
                agregar.append(valores_0_1)
                transiciones_diccionario[llave_0] = agregar

            if (not transiciones_diccionario.get(llave_1)):
                agregar = []
                agregar.append(valores_1)
                agregar.append(valores_1_1)
                transiciones_diccionario[llave_1] = agregar

            estados_actual = []

            # agrega el siguiente valor para revisar
            for i in range(len(transiciones_diccionario[llave_0])):
                key = ""
                for j in range(len(transiciones_diccionario[llave_0][i])):
                    if (j < len(transiciones_diccionario[llave_0][i]) - 1):
                        key += transiciones_diccionario[llave_0][i][j] + " "
                    else:
                        key += transiciones_diccionario[llave_0][i][j]

                # verifica si la llave ya esta en el diccionario
                if (not transiciones_diccionario.get(key)):
                    estados_actual.append(key)
                    # print key

            # agrega el siguiente valor para revisar
            for i in range(len(transiciones_diccionario[llave_1])):
                key = ""
                for j in range(len(transiciones_diccionario[llave_1][i])):
                    if (j < len(transiciones_diccionario[llave_1][i]) - 1):
                        key += transiciones_diccionario[llave_1][i][j] + " "
                    else:
                        key += transiciones_diccionario[llave_1][i][j]

                # verifica si la llave ya esta en el diccionario
                if (not transiciones_diccionario.get(key)):
                    estados_actual.append(key)

        if (len(estados_actual) <= 0):
            break


archivo = open("entrada.txt", "r")
nfa = ""
lineasArchivo = 0

for linea in archivo:
    lineasArchivo+=1
    #posibles alfabetos
    alfabeto=[]
    # cambia a lista
    nfa = linea.split(")")
    # reinicia las variables para la segunda corrida
    transiciones = []
    estados = []
    transiciones_diccionario_0 = {}
    transiciones_diccionario_1 = {}
    estados_llegada = []

    # elimina , ( )  y { }
    for i in range(len(nfa) - 1):
        estado = ""
        if (i == 0):
            for j in range(len(nfa[i])):
                if (nfa[i][j] != '{' and nfa[i][j] != '(' and nfa[i][j] != ')' and nfa[i][j] != '}'):
                    estado += nfa[i][j]
        else:
            for j in range(1, len(nfa[i])):
                if (nfa[i][j] != '{' and nfa[i][j] != '(' and nfa[i][j] != ')' and nfa[i][j] != '}'):
                    estado += nfa[i][j]
        transiciones.append(estado)

    for i in range(len(transiciones)):

        # guarda los estados
        if (not estados.__contains__(transiciones[i][2])):
            estados.append(transiciones[i][2])

        # guarda las trancisiones en 0 con 0 o a
        if (transiciones[i][0] == '0' or transiciones[i][0] == 'a'):
            # verifica el alfabeto
            if(transiciones[i][0] == '0' and transiciones[i][0] not in alfabeto):
                alfabeto.append('0')
            elif(transiciones[i][0] == 'a' and transiciones[i][0] not in alfabeto):
                alfabeto.append('a')

            if (not transiciones_diccionario_0.has_key(transiciones[i][2])):
                estados_llegada = []
                estados_llegada.append(transiciones[i][4])
                transiciones_diccionario_0[transiciones[i][2]] = estados_llegada
            else:
                estados_llegada = transiciones_diccionario_0.get(transiciones[i][2])
                estados_llegada.append(transiciones[i][4])
                transiciones_diccionario_0[transiciones[i][2]] = estados_llegada
        else:
            # guarda las trancisiones en 1
            if (not transiciones_diccionario_1.has_key(transiciones[i][2])):
                estados_llegada = []
                estados_llegada.append(transiciones[i][4])
                transiciones_diccionario_1[transiciones[i][2]] = estados_llegada
            else:
                estados_llegada = transiciones_diccionario_1.get(transiciones[i][2])
                estados_llegada.append(transiciones[i][4])
                transiciones_diccionario_1[transiciones[i][2]] = estados_llegada

    transiciones_diccionario = {}

    # Verifica que las transacciones de 0 estan en 1
    for transiciones in transiciones_diccionario_0:
        if (not transiciones_diccionario_1.has_key(transiciones)):
            v = []
            values = transiciones_diccionario_0.get(transiciones)
            v.append(values)
            v.append([])
            transiciones_diccionario[transiciones] = v
        else:
            v = []
            values = transiciones_diccionario_0.get(transiciones)
            v.append(values)
            values = transiciones_diccionario_1.get(transiciones)
            v.append(values)
            transiciones_diccionario[transiciones] = v

    # Verifica que las transacciones de 0 estan en transiciones
    for transiciones in transiciones_diccionario_1:
        if (not transiciones_diccionario.has_key(transiciones)):
                v = []
                v.append([])
                values = transiciones_diccionario_1.get(transiciones)
                v.append(values)
                transiciones_diccionario[transiciones] = v

    calcular_transiciones()

    lista=[]
    listaDfa=[]
    for i in transiciones_diccionario:
        estado = transiciones_diccionario.get(i)
        if('0' in alfabeto):
            nuevo= "0",i, estado[0]
            lista.append(nuevo)
            nuevo2 = "1",i,estado[1]
            lista.append(nuevo2)
        else:
            nuevo= "a",i, estado[0]
            lista.append(nuevo)
            nuevo2 = "b",i,estado[1]
            lista.append(nuevo2)

    strin = ""
    for j in lista:
        for k in j[2]:
            strin+=k
            estadoNuevo = j[0],j[1],strin
        listaDfa.append(estadoNuevo)
        strin=""


    if(lineasArchivo == 1):
        respuesta = "{"
    else:
        respuesta += "{"
    for index in range(len(listaDfa)):
        if(index < len(listaDfa)-1):
            respuesta += "("+listaDfa[index][0]+","+listaDfa[index][1]+","+listaDfa[index][2]+"),\n"
        else:
            respuesta += "(" + listaDfa[index][0] + "," + listaDfa[index][1] + "," + listaDfa[index][2] + ")}\n"
    respuesta +="\n"

archivo2 = open("salida.txt", "w")
archivo2.write(respuesta)
archivo2.close()
