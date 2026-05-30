from funciones import *

lista_paises = cargar_paises()

opcion = ""

while opcion != "0":

    # mostrar menu

    print(
        "\n============================\n"
        "        MENU PRINCIPAL       \n"
        "============================\n"
        "1. Mostrar paises\n"
        "2. Agregar pais\n"
        "3. Buscar pais\n"
        "4. Actualizar pais\n"
        "5. Filtrar por continente\n"
        "6. Filtrar por poblacion\n"
        "7. Filtrar por superficie\n"
        "8. Ordenar por nombre\n"
        "9. Ordenar por poblacion\n"
        "10. Ordenar por superficie\n"
        "11. Mostrar estadisticas\n"
        "0. Salir\n"
        "============================"
    )


    opcion = input("Elija una opcion: ")

    if opcion == "1":
        mostrar_paises(lista_paises)

    elif opcion == "2":
        agregar_paises(lista_paises)

    elif opcion == "3":
        buscar_paises(lista_paises)

    elif opcion == "4":
        actualizar_paises(lista_paises)

    elif opcion == "5":
        filtrar_continente(lista_paises)

    elif opcion == "6":
        filtrar_poblacion(lista_paises)

    elif opcion == "7":
        filtrar_superficie(lista_paises)

    elif opcion == "8":
        orden = input(
            "\nOrdenar por nombre:\n"
            "(1) Ascendente (A-Z)\n"
            "(2) Descendente (Z-A)\n"
            "Seleccione una opcion: "
        ).strip()

        while orden not in ["1", "2"]:
            print("Opcion invalida")
            orden = input("Seleccione una opcion: ").strip()

        if orden == "1":
            descendente = False

        elif orden == "2":
            descendente = True

        ordenar_nombre(lista_paises, descendente)

    elif opcion == "9":

        orden = input(
            "\nOrdenar por poblacion:\n"
            "(1) Ascendente (A-Z)\n"
            "(2) Descendente (Z-A)\n"
            "Seleccione una opcion: "
        ).strip()

        while orden not in ["1", "2"]:
            print("Opcion invalida")
            orden = input("Seleccione una opcion: ").strip()

        if orden == "1":
            descendente = False

        elif orden == "2":
            descendente = True

        ordenar_poblacion(lista_paises, descendente)

    elif opcion == "10":

        orden = input(
            "\nOrdenar por supericie:\n"
            "(1) Ascendente (A-Z)\n"
            "(2) Descendente (Z-A)\n"
            "Seleccione una opcion: "
        ).strip()

        while orden not in ["1", "2"]:
            print("Opcion invalida")
            orden = input("Seleccione una opcion: ").strip()

        if orden == "1":
            descendente = False

        elif orden == "2":
            descendente = True

        ordenar_superficie(lista_paises, descendente)

    elif opcion == "11":
        mostrar_estadisticas(lista_paises)

guardar_paises(lista_paises)