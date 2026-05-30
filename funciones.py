import csv

# ======================
# FUNCION CARGAR PAISES
# ======================

# Funcion para cargar los paises desde el archivo CSV
def cargar_paises():

    # Lista donde se guardaran todos los paises
    lista_paises = []

    try:

        # Se abre el archivo CSV en modo lectura
        with open("paises.csv", "r", encoding="utf-8") as archivo:

            # DictReader convierte cada fila en un diccionario
            lector = csv.DictReader(archivo)

            # Se recorre cada fila del archivo
            for fila in lector:

                # Se crea un diccionario con los datos del país
                # convirtiendo población y superficie a enteros
                # Mayuscula modo titulo a nombre del pais y continente
                pais = {
                    "nombre": fila["nombre"].title(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].title()
                }

                # Cada fila (diccionario) se agrega a la lista
                lista_paises.append(pais)

    # Error si el archivo CSV no existe
    except FileNotFoundError:
        print("Error: no se encontro el archivo CSV")

    # Error si un dato numerico tiene formato inválido
    except ValueError:
        print("Error: formato invalido en el archivo CSV")

    # La funcion devuelve la lista completa de paises
    return lista_paises

# ======================
# FUNCION MOSTRAR PAIS
# ======================

def mostrar_pais(pais):
                
    # Muestra los datos del pais encontrado
    print(f"Nombre: {pais['nombre']}")
    # f"{...:,}" inserta comas como separador de miles
    # replace(",", ".") convierte el formato a estilo español (puntos)
    poblacion = f"{pais['poblacion']:,}".replace(",", ".")
    print(f"Población: {poblacion}")
    superficie = f"{pais['superficie']:,}".replace(",", ".")
    print(f"Superficie: {superficie}")
    print(f"Continente: {pais['continente']}")
    print("------------------------")


# ============================
# FUNCION FORMATO CONTINENTE
# ============================

# Corrige continentes ingresados sin tilde
# para mantener el mismo formato en todo el sistema

def formato_continente(continente):

    if continente == "America":
        continente = "América"

    elif continente == "Africa":
        continente = "África"

    elif continente == "Oceania":
        continente = "Oceanía"

    return continente


# ======================
# FUNCION GUARDAR PAISES
# ======================

# Funcion para guardar los paises en el archivo CSV
def guardar_paises(lista_paises):

    # Columnas que tendra el archivo CSV
    columnas = ["nombre", "poblacion", "superficie", "continente"]

    try:

        # Se abre el archivo CSV en modo escritura (w reemplaza el original)
        with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:

            # DictWriter permite escribir diccionarios en el CSV
            escritor = csv.DictWriter(archivo, fieldnames=columnas)

            # Se escriben los encabezados
            escritor.writeheader()

            # Se escriben todos los paises de la lista
            escritor.writerows(lista_paises)
        
        print("Datos guardados correctamente")

    # Captura cualquier error inesperado durante el guardado del archivo
    except Exception as e:

        # Se muestra el mensaje de error ocurrido
        print("Error al guardar el archivo:", e)

# ======================
# FUNCION MOSTRAR PAISES
# ======================

# Funcion para mostrar los paises cargados 
def mostrar_paises(lista_paises):

    # Verifica si la lista está vacía
    if len(lista_paises) == 0:
        print("No hay paises cargados")

    else:
        print("------------------------")

        # Recorre la lista de paises
        for pais in lista_paises:
            mostrar_pais(pais)

# ======================
# FUNCION AGREGAR PAISES
# ======================

# Funcion para agregar un nuevo pais a la lista
def agregar_paises(lista_paises):

    continentes_validos = ["América", "Europa", "Asia", "África", "Oceanía"]

    try:

        # Se solicita el nombre del pais
        # strip() elimina espacios al inicio y final
        # title() coloca la primera letra de cada palabra en mayuscula
        nombre = input("Ingrese el pais: ").strip().title()

        # Valida que el nombre no este vacio o contenga algo distinto de letras
        # replace(" ", "") elimina temporalmente los espacios del texto
        # Esto permite aceptar nombres compuestos como "Estados Unidos" 
        # y luego isalpha() verifica que sean letras
        # El not invierte el resultado, si hay numeros o simbolos la condicion sera True
        while nombre == "" or not nombre.replace(" ", "").isalpha():

            # Si el campo esta vacio
            if nombre == "":
                print("No se puede ingresar un nombre vacio\n")

            # Si contiene numeros o caracteres invalidos
            else:
                print("Solo se permiten letras\n")

            # Se vuelve a solicitar el nombre
            nombre = input("Ingrese el pais: ").strip().title()

        # Se verifica que el pais no exista previamente en la lista
        for pais in lista_paises:

            if nombre.lower() == pais["nombre"].lower():
                print("El pais ya existe en la lista")
                return

        # Se solicitan poblacion y superficie como numeros enteros mayores a 0
        poblacion = int(input("Ingrese la poblacion: "))
    
        while poblacion <= 0:
            print("La poblacion debe ser mayor a 0")
            poblacion = int(input("Ingrese la poblacion: "))

        superficie = int(input("Ingrese la superficie: "))
        
        while superficie <= 0:
            print("La superficie debe ser mayor a 0")
            superficie = int(input("Ingrese la superficie: "))

        # Se solicita el continente
        continente = input("Ingrese el continente: ").strip().title()

        continente = formato_continente(continente)

        # Valida que el continente no este vacio o contenga algo distinto de letras
        # replace(" ", "") elimina temporalmente los espacios del texto para la verificacion de letras con isalpha()

        while continente == "" or not continente.replace(" ", "").isalpha():

            # Si el campo esta vacio
            if continente == "":
                print("No se puede ingresar un nombre vacio\n")

            # Si contiene numeros o caracteres invalidos
            else:
                print("Solo se permiten letras\n")

            # Se vuelve a solicitar el continente
            continente = input("Ingrese el continente: ").strip().title()

        # Corrige continentes ingresados sin tilde
        # para mantener el mismo formato utilizado en el archivo CSV
        continente = formato_continente(continente)

        # Verifica que el continente ingresado exista
        # dentro de la lista de continentes permitidos
        while continente not in continentes_validos:
            print("Continente invalido")
            print("Opciones: América, Europa, Asia, África, Oceanía")

            continente = input("Ingrese el continente: ").strip().title()

            continente = formato_continente(continente)

        # Se crea el diccionario con los datos del nuevo pais
        pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }

        # Se agrega el pais a la lista
        lista_paises.append(pais)

        print("Pais agregado correctamente")

    # Error si se ingresan letras en campos numericos
    except ValueError:
        print("Error: solo se permite ingresar numeros enteros")


# ======================
# FUNCION BUSCAR PAISES
# ======================

# Funcion para buscar un pais en la lista
def buscar_paises(lista_paises):

    # Bandera para verificar si se encontro el pais
    pais_encontrado = False

    # Se solicita el nombre del pais
    # lower() convierte el texto a minusculas para facilitar la comparacion
    nombre = input("Ingrese el pais: ").strip().lower()

    # Valida que el campo no este vacio
    while nombre == "":
        nombre = input("Debe ingresar un pais: ").strip().lower()

    # Verifica si la lista esta vacia
    if len(lista_paises) == 0:
        print("No hay paises cargados")

    else:

        print("------------------------")

        # Recorre la lista de paises
        for pais in lista_paises:

            # lower() convierte temporalmente el nombre del pais a minusculas
            # startswith() verifica si el nombre del pais comienza
            # con el texto ingresado por el usuario
            if pais["nombre"].lower().startswith(nombre):
                mostrar_pais(pais)

                # Marca que se encontro al menos un pais
                pais_encontrado = True

        # Si no se encontro ningun pais
        if pais_encontrado == False:
            print("El pais no se encuentra en la lista")

# ==========================
# FUNCION ACTUALIZAR PAISES
# ==========================

def actualizar_paises(lista_paises):

    # Bandera para verificar si se encontro el pais
    pais_encontrado = False


    try:

        # Se solicita el nombre del pais
        # lower() convierte el texto a minusculas para facilitar la comparacion
        nombre = input("Ingrese el pais: ").strip().lower()

        # Valida que el campo no este vacio
        while nombre == "":
            nombre = input("Debe ingresar un pais: ").strip().lower()

        # Verifica si la lista esta vacia
        if len(lista_paises) == 0:
            print("No hay paises cargados")

        else:

            # Recorre la lista de paises
            for pais in lista_paises:

                # lower() convierte temporalmente el nombre del pais a minusculas
                if nombre == pais["nombre"].lower():

                    
                    nueva_poblacion = int(input("Ingrese la poblacion: "))

                    while nueva_poblacion <= 0:
                        print("La poblacion debe ser mayor a 0")
                        nueva_poblacion = int(input("Ingrese la poblacion: "))

                    nueva_superficie = int(input("Ingrese la superficie: "))
                    while nueva_superficie <= 0:
                        print("La superficie debe ser mayor a 0")
                        nueva_superficie = int(input("Ingrese la superficie: "))

                    pais['poblacion'] = nueva_poblacion
                    pais['superficie'] = nueva_superficie

                    # Marca que se encontro al menos un pais
                    pais_encontrado = True

                    print("\nDatos actualizados correctamente")

                    print("------------------------")
                    mostrar_pais(pais)

                    break

            # Si no se encontro ningun pais
            if pais_encontrado == False:
                print("El pais no se encuentra en la lista")



    # Error si se ingresan letras en campos numericos
    except ValueError:
        print("Error: solo se permite ingresar numeros enteros")


# =============================
# FUNCION FILTRAR X CONTINENTE
# =============================

# Funcion para filtrar paises por continente
def filtrar_continente(lista_paises):

    # Bandera para verificar si se encontraron paises
    encontrado = False

    # Verifica si la lista esta vacia
    if len(lista_paises) == 0:

        print("No hay paises cargados")

    else:

        # Se solicita el continente
        # strip() elimina espacios al inicio y final
        continente = input("Ingrese el continente: ").strip().title()

        # Valida que el continente no este vacio
        # y que solo contenga letras
        while continente == "" or not continente.replace(" ", "").isalpha():

            # Si el campo esta vacio
            if continente == "":
                print("No se puede ingresar un nombre vacio\n")

            # Si contiene numeros o caracteres invalidos
            else:
                print("Solo se permiten letras\n")

            # Se vuelve a solicitar el continente
            continente = input("Ingrese el continente: ").strip().title()

        print("------------------------")

        continente = formato_continente(continente)
            
        # Recorre la lista de paises
        for pais in lista_paises:

            # Verifica si el continente ingresado
            # coincide con el continente del pais
            if continente == pais["continente"]:
                mostrar_pais(pais)

                # Marca que se encontro al menos un pais
                encontrado = True

        # Si no se encontraron paises del continente ingresado
        if not encontrado:

            print("No se encontraron paises del continente de", continente.title())

# ============================
# FUNCION FILTRAR X POBLACION
# ============================

# Funcion para filtrar paises por rango de poblacion
def filtrar_poblacion(lista_paises):

    # Bandera para verificar si se encontraron paises
    encontrado = False

    try:

        # Verifica si la lista esta vacia
        if len(lista_paises) == 0:

            print("No hay paises cargados")

        else:

            # Se solicita la poblacion minima
            poblacion_min = int(input("Ingrese poblacion rango minimo: "))

            # Valida que la poblacion minima sea mayor a 0
            while poblacion_min <= 0:
                print("La poblacion debe ser mayor a 0")
                poblacion_min = int(input("Ingrese la poblacion minima: "))

            # Se solicita la poblacion maxima
            poblacion_max = int(input("Ingrese poblacion rango maximo: "))

            # Valida que la poblacion maxima sea mayor a 0
            while poblacion_max <= 0:
                print("La poblacion debe ser mayor a 0")
                poblacion_max = int(input("Ingrese la poblacion maxima: "))

            # Valida que la poblacion maxima sea mayor que la minima
            while poblacion_max <= poblacion_min:
                print("La poblacion maxima debe ser mayor a la minima")
                poblacion_max = int(input("Ingrese la poblacion maxima: "))

            print("------------------------")

            # Recorre la lista de paises
            for pais in lista_paises:

                # Verifica si la poblacion del pais
                # esta dentro del rango ingresado
                if poblacion_min <= pais["poblacion"] <= poblacion_max:
                    mostrar_pais(pais)

                    # Marca que se encontro al menos un pais
                    encontrado = True

            # Si no se encontraron paises en el rango ingresado
            if not encontrado:

                print(f"No se encontraron paises en el rango de poblacion de {poblacion_min} a {poblacion_max}")

    # Error si se ingresan letras en campos numericos
    except ValueError:
        print("Error: solo se permite ingresar numeros enteros")

# ============================
# FUNCION FILTRAR X SUPERFICIE
# ============================

# Funcion para filtrar paises por rango de superficie
def filtrar_superficie(lista_paises):

    # Bandera para verificar si se encontraron paises
    encontrado = False

    try:

        # Verifica si la lista esta vacia
        if len(lista_paises) == 0:

            print("No hay paises cargados")

        else:

            # Se solicita la superficie minima
            superficie_min = int(input("Ingrese superficie rango minimo: "))

            # Valida que la superficie minima sea mayor a 0
            while superficie_min <= 0:
                print("La superficie debe ser mayor a 0")
                superficie_min = int(input("Ingrese la superficie minima: "))

            # Se solicita la superficie maxima
            superficie_max = int(input("Ingrese superficie rango maximo: "))

            # Valida que la superficie maxima sea mayor a 0
            while superficie_max <= 0:
                print("La superficie debe ser mayor a 0")
                superficie_max = int(input("Ingrese la superficie maxima: "))

            # Valida que la superficie maxima sea mayor que la minima
            while superficie_max <= superficie_min:
                print("La superficie maxima debe ser mayor a la minima")
                superficie_max = int(input("Ingrese la superficie maxima: "))

            print("------------------------")

            # Recorre la lista de paises
            for pais in lista_paises:

                # Verifica si la superficie del pais
                # esta dentro del rango ingresado
                if superficie_min <= pais["superficie"] <= superficie_max:
                    mostrar_pais(pais)

                    # Marca que se encontro al menos un pais
                    encontrado = True

            # Si no se encontraron paises en el rango ingresado
            if not encontrado:

                print(f"No se encontraron paises en el rango de superficie de {superficie_min} a {superficie_max}")

    # Error si se ingresan letras en campos numericos
    except ValueError:
        print("Error: solo se permite ingresar numeros enteros")

# ============================
# FUNCION ORDENAR POR NOMBRE
# ============================

# Funcion para ordenar la lista de paises por nombre
def ordenar_nombre(lista_paises, descendente):
    
    # Verifica si la lista esta vacia
    if len(lista_paises) == 0:

        print("No hay paises cargados")

    else:

        # Ordena la lista utilizando sorted()
        # key=lambda pais: pais["nombre"] indica que el criterio de orden es el nombre del pais
        # reverse=descendente permite definir si el orden es ascendente (False) o descendente (True)

        lista_ordenada = sorted(lista_paises, key=lambda pais: pais["nombre"], reverse=descendente)
        
        print("------------------------")

        # Recorre la lista ya ordenada y muestra los paises
        for pais in lista_ordenada:
            mostrar_pais(pais)

# ==============================
# FUNCION ORDENAR POR POBLACION
# ==============================

def ordenar_poblacion(lista_paises, descendente):

    # Verifica si la lista esta vacia
    if len(lista_paises) == 0:

        print("No hay paises cargados")

    else:

        # Ordena la lista segun la poblacion de los paises
        lista_ordenada = sorted(lista_paises, key=lambda pais: pais["poblacion"], reverse=descendente)
        
        print("------------------------")

        # Recorre la lista ya ordenada y muestra los paises
        for pais in lista_ordenada:
            mostrar_pais(pais)

# ==============================
# FUNCION ORDENAR POR SUPERFICIE
# ==============================

def ordenar_superficie(lista_paises, descendente):

    # Verifica si la lista esta vacia
    if len(lista_paises) == 0:

        print("No hay paises cargados")

    else:

        # Ordena la lista segun la superficie de los paises
        lista_ordenada = sorted(lista_paises, key=lambda pais: pais["superficie"], reverse=descendente)
        
        print("------------------------")

        # Recorre la lista ya ordenada y muestra los paises
        for pais in lista_ordenada:
            mostrar_pais(pais)

# ============================
# FUNCION MOSTRAR ESTADISTICAS
# ============================

# Funcion para mostrar estadisticas generales de los paises
def mostrar_estadisticas(lista_paises):

    # Variables para mayor poblacion, acumuladores y contador
    mayor = acumulador_poblacion = acumulador_superficie = contador = 0

    # Diccionario contador de paises por continente
    contadores = {
    "América": 0,
    "Europa": 0,
    "Asia": 0,
    "África": 0,
    "Oceanía": 0
    }

    # Variable para almacenar la menor poblacion
    # Se inicializa con infinito para asegurar que cualquier poblacion sera menor
    menor = float("inf")

    # Verifica si la lista esta vacia
    if len(lista_paises) == 0:

        print("No hay paises cargados")

    else:

        # Recorre la lista de paises
        for pais in lista_paises:

            # Verifica si el pais tiene la mayor poblacion
            if pais["poblacion"] > mayor:

                # Guarda el nombre del pais con mayor poblacion
                pais_mayor = pais['nombre']

                # Actualiza la mayor poblacion encontrada
                mayor = pais["poblacion"]

            # Verifica si el pais tiene la menor poblacion
            if pais["poblacion"] < menor:

                # Guarda el nombre del pais con menor poblacion
                pais_menor = pais['nombre']

                # Actualiza la menor poblacion encontrada
                menor = pais["poblacion"]

            # Incrementa en 1 la cantidad de paises del continente correspondiente
            # usando el nombre del continente como clave del diccionario
            contadores[pais["continente"]] += 1

            # Acumula poblacion y superficie total
            acumulador_poblacion += pais["poblacion"]
            acumulador_superficie += pais["superficie"]

            # Cuenta cantidad total de paises
            contador += 1

        print("------------------------")
        # Formateo de resultados para salida legible
        mayor = f"{mayor:,}".replace(",", ".")
        menor = f"{menor:,}".replace(",", ".")
        promedio_poblacion = f"{(acumulador_poblacion / contador):,.0f}".replace(",", ".")
        promedio_superficie = f"{(acumulador_superficie / contador):,.0f}".replace(",", ".")

        # Muestra las estadisticas calculadas
        print(
            f"Estadisticas:\n"
            f"Pais con mayor poblacion: {pais_mayor} con {mayor} habitantes\n"
            f"Pais con menor poblacion: {pais_menor} con {menor} habitantes\n"
            f"Promedio de poblacion: {promedio_poblacion} habitantes por pais\n"
            f"Promedio de superficie: {promedio_superficie} km2 por pais\n"
            f"America: {contadores['América']} paises\n"
            f"Europa: {contadores['Europa']} paises\n"
            f"Africa: {contadores['África']} paises\n"
            f"Asia: {contadores['Asia']} paises\n"
            f"Oceania: {contadores['Oceanía']} paises"
        )

        print("------------------------")

