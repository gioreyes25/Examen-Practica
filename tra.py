# Diccionarios iniciales
datos = {
    "A001": ["Michael Jackson", "Thriller", "1982", "Pop"],
    "A002": ["AC/DC", "Back in Black", "1980", "Rock"],
    "A003": ["Pink Floyd", "The Dark Side of the Moon", "1973", "Rock"],
    "A004": ["Whitney Houston", "The Bodyguard", "1992", "R&B"],
    "A005": ["Adele", "21", "2011", "Pop"]
}

inventario = {
    "A001": [15, "Pop"],
    "A002": [10, "Rock"],
    "A003": [8, "Rock"],
    "A004": [0, "R&B"],
    "A005": [5, "Pop"]
}

while True:
    print("\n*** MENÚ PRINCIPAL ***")
    print("1. Stock por Género.")
    print("2. Búsqueda por Año de Lanzamiento.")
    print("3. Actualizar Cantidad de Stock.")
    print("4. Salir.")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        genero_input = input("Ingrese género a consultar: ").title()
        total = 0
        for id, (cantidad, genero) in inventario.items():
            if genero == genero_input:
                total += cantidad
        print(f"Stock total para el género '{genero_input}': {total}")

    elif opcion == "2":
        while True:
            try:
                anio_min = int(input("Ingrese año mínimo: "))
                anio_max = int(input("Ingrese año máximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros!!")

        resultados = []

        for id, info in datos.items():
            artista, titulo, anio, genero = info
            if id in inventario:
                cantidad = inventario[id][0]
                if cantidad > 0 and anio_min <= int(anio) <= anio_max:
                    resultados.append(f"{artista}--{titulo}")

        if resultados:
            print("\nÁlbumes encontrados:")
            for r in sorted(resultados):
                print(r)
        else:
            print("No hay álbumes en ese rango de años.")

    elif opcion == "3":
        while True:
            album_id = input("Ingrese ID del álbum a actualizar: ").upper()
            if album_id in inventario:
                try:
                    nueva_cantidad = int(input("Ingrese nueva cantidad de stock: "))
                    inventario[album_id][0] = nueva_cantidad
                    print("Stock actualizado!!")
                except ValueError:
                    print("Debe ingresar un número entero.")
            else:
                print("El álbum no existe!!")

            continuar = input("¿Desea actualizar otro stock de álbum? (si/no): ").lower()
            if continuar != "si":
                break

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Debe selecciona")
