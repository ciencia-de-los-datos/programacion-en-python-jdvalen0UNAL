"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # Ruta del archivo .csv
    file_path = 'data.csv'
    #hola
    # Inicializa una variable para almacenar la suma de la segunda columna
    suma_segunda_columna = 0

    # Abre el archivo .csv
    with open(file_path, 'r') as csvfile:
        # Itera a través de las líneas del archivo
        for line in csvfile:
            # Divide la línea en espacios y obtén la segunda parte
            columns = line.strip().split()
            if len(columns) > 1:
                try:
                    valor = float(columns[1])  # Convierte el valor a número (float)
                    suma_segunda_columna += valor
                except ValueError:
                    # Ignora valores que no se pueden convertir a número
                    pass

    return suma_segunda_columna

    


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
   
    # Ruta del archivo .csv
    file_path = 'data.csv'

    # Diccionario para almacenar la cantidad de registros por letra
    registros_por_letra = {}

    # Abre el archivo .csv
    with open(file_path, 'r') as csvfile:
        # Itera a través de las líneas del archivo
        for line in csvfile:
            # Divide la línea en espacios y obtén la primera parte (letra)
            columns = line.strip().split()
            if len(columns) > 0:
                letra = columns[0]

                # Incrementa el contador de la letra en el diccionario
                registros_por_letra[letra] = registros_por_letra.get(letra, 0) + 1

    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    lista_ord_alphabet = sorted(registros_por_letra.items())

    return lista_ord_alphabet



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
     # Ruta del archivo .csv
    file_path = 'data.csv'

    # Diccionario para almacenar la suma de la columna 2 por letra de la primera columna
    suma_por_letra = {}

    # Abre el archivo .csv
    with open(file_path, 'r') as csvfile:
        # Itera a través de las líneas del archivo
        for line in csvfile:
            # Divide la línea en espacios y obtén las dos partes (letra y valor)
            columns = line.strip().split()
            if len(columns) >= 2:
                letra = columns[0]
                valor = float(columns[1]) if columns[1].replace(".", "", 1).isdigit() else 0

                # Suma el valor al diccionario por letra
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor

    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    lista_ord_alphabet = sorted(suma_por_letra.items())

    return lista_ord_alphabet


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    # Ruta del archivo .csv
    file_path = 'data.csv'

    # Diccionario para almacenar la cantidad de registros por mes
    registros_por_mes = {}

    # Abre el archivo .csv
    with open(file_path, 'r') as csvfile:
        # Itera a través de las líneas del archivo
        for line in csvfile:
            # Divide la línea en espacios y obtén las tres partes (la fecha)
            columns = line.strip().split()
            if len(columns) >= 3:
                fecha = columns[2]

                # Extrae el mes de la fecha (primeros 7 caracteres)
                mes = fecha[5:7]

                # Incrementa el contador del mes en el diccionario
                registros_por_mes[mes] = registros_por_mes.get(mes, 0) + 1

    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    lista_ord_alphabet = sorted(registros_por_mes.items())

    return lista_ord_alphabet


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
        # Ruta del archivo .csv
    archivo = 'data.csv'

    # Diccionario para almacenar el valor máximo y mínimo por letra
    max_min_por_letra = {}

    # Abre el archivo .csv
    with open(archivo, 'r') as csvfile:
        # Itera a través de las líneas del archivo
        for linea in csvfile:
            # Divide la línea en espacios y obtén las dos partes (letra y valor)
            partes = linea.strip().split()
            if len(partes) >= 2:
                letra = partes[0]
                valor = float(partes[1]) if partes[1].replace(".", "", 1).isdigit() else 0

                # Actualiza el valor máximo y mínimo por letra
                if letra in max_min_por_letra:
                    max_min_por_letra[letra][0] = max(max_min_por_letra[letra][0], valor)
                    max_min_por_letra[letra][1] = min(max_min_por_letra[letra][1], valor)
                else:
                    max_min_por_letra[letra] = [valor, valor]

    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente por la letra
    lista_tuplas = sorted([(letra, max_min[0], max_min[1]) for letra, max_min in max_min_por_letra.items()], key=lambda x: x[0])

    return lista_tuplas



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    # Ruta del archivo .csv
    archivo_csv = 'data.csv'

    # Diccionario para almacenar el valor mínimo y máximo por clave
    min_max_por_clave = {}

    # Abre el archivo .csv
    with open(archivo_csv, 'r') as csvfile:
        # Itera a través de las líneas del archivo
        for linea in csvfile:
            # Divide la línea en espacios y obtén la quinta parte (diccionario)
            partes = linea.strip().split()
            if len(partes) >= 5:
                diccionario = partes[4]

                # Divide el diccionario en pares clave:valor
                pares = diccionario.split(',')

                # Itera a través de los pares clave:valor
                for par in pares:
                    clave, valor = par.split(':')
                    valor = int(valor)

                    # Si la clave ya está en el diccionario, actualiza los valores mínimo y máximo
                    if clave in min_max_por_clave:
                        min_valor, max_valor = min_max_por_clave[clave]
                        min_max_por_clave[clave] = (min(min_valor, valor), max(max_valor, valor))
                    else:
                        min_max_por_clave[clave] = (valor, valor)

    # Convierte el diccionario a una lista de tuplas
    lista_tuplas = [(clave, min_valor, max_valor) for clave, (min_valor, max_valor) in min_max_por_clave.items()]

    # Ordena la lista alfabéticamente por clave
    lista_tuplas.sort(key=lambda x: x[0])

    return lista_tuplas



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
       # Crear un diccionario para almacenar las letras asociadas a cada valor de la columna 2
    resultado_dict = {}
    
    # Abrir el archivo CSV con pestaña ('\t') como delimitador
    with open('data.csv', 'r') as csvfile:
        # Iterar a través de las líneas del archivo
        for line in csvfile:
            # Dividir la línea en función de la pestaña ('\t')
            columns = line.strip().split('\t')
            if len(columns) >= 3:
                try:
                    valor_col2 = int(columns[1])  # Convertir el valor de la columna 2 a entero
                    letra_col0 = columns[0]
                
                    # Verificar si el valor de la columna 2 ya está en el diccionario
                    if valor_col2 in resultado_dict:
                        resultado_dict[valor_col2].append(letra_col0)
                    else:
                        resultado_dict[valor_col2] = [letra_col0]
                except ValueError:
                    # Ignorar filas con valores no numéricos en la columna 2
                    continue
    
    # Crear una lista de tuplas a partir del diccionario
    resultado = [(key, value) for key, value in resultado_dict.items()]
    
    # Ordenar la lista de tuplas en orden ascendente por el valor de la columna 2
    resultado = sorted(resultado, key=lambda x: x[0])
    
    return resultado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
     # Crear un diccionario para almacenar las letras asociadas a cada valor de la columna 1
    resultado_dict = {}
    
    # Abrir el archivo CSV con pestaña ('\t') como delimitador
    with open('data.csv', 'r') as csvfile:
        # Iterar a través de las líneas del archivo
        for line in csvfile:
            # Dividir la línea en función de la pestaña ('\t')
            columns = line.strip().split('\t')
            if len(columns) >= 3:
                try:
                    valor_col2 = int(columns[1])  # Obtener el valor de la columna 2 como entero
                    letra_col0 = columns[0]
                
                    # Verificar si el valor de la columna 2 ya está en el diccionario
                    if valor_col2 in resultado_dict:
                        resultado_dict[valor_col2].add(letra_col0)  # Usar un conjunto para eliminar duplicados
                    else:
                        resultado_dict[valor_col2] = {letra_col0}
                except ValueError:
                    # Ignorar filas con valores no numéricos en la columna 2
                    continue
    
    # Crear una lista de tuplas a partir del diccionario
    resultado = [(key, sorted(value)) for key, value in resultado_dict.items()]
    
    # Ordenar la lista de tuplas por el valor de la columna 2 en orden ascendente
    resultado = sorted(resultado, key=lambda x: x[0])
    
    return resultado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    # Crear un diccionario para almacenar la cantidad de registros por clave
    contador_claves = {}

    # Abrir el archivo CSV con pestaña ('\t') como delimitador
    with open('data.csv', 'r') as csvfile:
        # Iterar a través de las líneas del archivo
        for line in csvfile:
            # Dividir la línea en función de la pestaña ('\t')
            columns = line.strip().split('\t')
            
            if len(columns) >= 5:
                # Obtener la columna 5 (índice 4)
                columna_5 = columns[4]
                
                # Dividir la columna 5 en subelementos usando coma (',') como delimitador
                subelementos = columna_5.split(',')
                
                # Iterar a través de los subelementos
                for subelemento in subelementos:
                    # Dividir cada subelemento en clave y valor usando dos puntos (':') como delimitador
                    clave, valor = subelemento.split(':')
                    
                    # Incrementar el contador de la clave en el diccionario o inicializarlo en 1 si es la primera vez
                    if clave in contador_claves:
                        contador_claves[clave] += 1
                    else:
                        contador_claves[clave] = 1
    
    return contador_claves


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    # Crear una lista para almacenar las tuplas resultado
    resultado = []

    # Abrir el archivo CSV con pestaña ('\t') como delimitador
    with open('data.csv', 'r') as csvfile:
        # Iterar a través de las líneas del archivo
        for line in csvfile:
            # Dividir la línea en función de la pestaña ('\t')
            columns = line.strip().split('\t')

            if len(columns) >= 5:
                # Obtener la letra de la columna 1 (índice 0)
                letra = columns[0]

                # Obtener las columnas 4 y 5 (índices 3 y 4)
                columna_4 = columns[3]
                columna_5 = columns[4]

                # Dividir las columnas 4 y 5 en subelementos usando coma (',') como delimitador y contarlos
                elementos_columna_4 = len(columna_4.split(','))
                elementos_columna_5 = len(columna_5.split(','))

                # Crear una tupla con la letra y la cantidad de elementos de las columnas 4 y 5
                tupla_resultado = (letra, elementos_columna_4, elementos_columna_5)

                # Agregar la tupla al resultado
                resultado.append(tupla_resultado)

    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    # Inicializamos un diccionario vacío para almacenar los resultados
    resultado = {}
    
    try:
        # Abre el archivo data.csv en modo lectura
        with open("data.csv", "r") as archivo:
            # Itera sobre cada línea del archivo
            for linea in archivo:
                # Divide la línea en columnas utilizando el espacio como delimitador
                columnas = linea.strip().split()
                
                # Verifica que la línea tenga al menos cuatro columnas antes de continuar
                if len(columnas) < 4:
                    continue
                
                # Extrae la columna 2 y la columna 4
                columna_2 = columnas[1]
                columna_4 = columnas[3]
                
                # Verifica si la columna 2 es un valor numérico
                if columna_2.isnumeric():
                    columna_2 = int(columna_2)
                else:
                    # Si no es numérico, omite esta línea
                    continue
                
                # Itera sobre cada letra en la columna 4
                for letra in columna_4.split(','):
                    # Si la letra ya está en el diccionario, suma el valor actual
                    if letra in resultado:
                        resultado[letra] += columna_2
                    # Si la letra no está en el diccionario, crea una nueva entrada
                    else:
                        resultado[letra] = columna_2
        
        # Ordena el diccionario alfabéticamente
        resultado_ordenado = dict(sorted(resultado.items()))
        
        return resultado_ordenado
    
    except Exception as e:
        return str(e)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
        # Crear un diccionario para almacenar la suma de los valores de la columna 5 por cada letra de la columna 1
    suma_por_letra = {}

    # Abrir el archivo CSV con pestaña ('\t') como delimitador
    with open('data.csv', 'r') as csvfile:
        # Iterar a través de las líneas del archivo
        for line in csvfile:
            # Dividir la línea en función de la pestaña ('\t')
            columns = line.strip().split('\t')

            if len(columns) >= 2:
                # Obtener la letra de la columna 1 (índice 0)
                letra = columns[0]

                # Obtener la columna 5 (índice 4)
                columna_5 = columns[4]

                # Dividir la columna 5 en subelementos usando coma (',') como delimitador
                valores_columna_5 = columna_5.split(',')

                # Calcular la suma de los valores en la columna 5
                suma_columna_5 = sum(int(valor.split(':')[1]) for valor in valores_columna_5)

                # Agregar la suma al diccionario, sumando si la clave ya existe o creándola si no
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma_columna_5

    # Ordenar el diccionario por clave y devolverlo
    suma_por_letra_ordenado = dict(sorted(suma_por_letra.items()))
    return suma_por_letra_ordenado
    
