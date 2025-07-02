datos = {
    "A001": ["Thriller", 1982, "Pop", 15],
    "A002": ["Back in Black", 1982, "Rock", 10],
    "A003": ["The Dark Side of the Moon", 1973, "Rock", 8],
    "A004": ["The Bodyguard", 1992, "RB", 12],
    "A005": ["Rumours", 1977, "Rock", 9],
    "A006": ["Run", 2011, "Pop", 11],
    "A007": ["Come Away With Me", 2002, "Jazz", 7],
    "A008": ["Abbey Road", 1970, "Rock", 13],
    "A009": ["Hotel California", 1970, "Rock", 10],
    "A010": ["Hilk", 2014, "Pop", 14]
}
inventario = {
    "A001": [15, "Pop"],
    "A002": [10, "Rock"],
    "A003": [8, "Rock"],
    "A004": [12, "RB"],
    "A005": [9, "Rock"],
    "A006": [11, "Pop"],
    "A007": [7, "Jazz"],
    "A008": [13, "Rock"],
    "A009": [10, "Rock"],
    "A010": [14, "Pop"]
}

while True:
    print("\n1. Stock Por Genero")
    print("2. Busqueda Por Año De Lanzamiento")
    print("3. Actualizar Cantidad de Stock")
    print("4. Salir")
    op=int(input("Ingrese auna opcion: "))
    match op:
        case 1:
            gene=input("Ingrese genero que buscara: ").title()
            total=0
            for id, album in datos.items():
                cancion = album[0]
                año = album[1]
                genero=album[2]
                if gene in datos[id]:
                    print(f"ID: {id} | Canción: {cancion} | Año: {año}| Genero: {genero}")
            for idd,canti in inventario.items():
                if gene==canti[1]:
                    cantidad=canti[0]
                    total+=cantidad
            print(f"Stock De Genero De {gene}: {total}")
        case 2:
            c=0
            while True:
                try:
                    buscar1 = int(input("Ingrese año min: "))
                    buscar2 = int(input("Ingrese año max: "))
                    break 
                except ValueError:
                    print("Solo se permiten números enteros.")
                    
            for id,album in datos.items():
                cancion = album[0]
                año = album[1]
                genero=album[2]
                cantidad=album[3]
                if buscar1 <= int(año) <= buscar2 and cantidad!=0:
                    ordenados = sorted(datos.items(), key=lambda item: item[1][0])
                else:
                    print("No hay coincidencias")
                    break
                resultados = []
            for ida,albuma in ordenados:
                cancion, año, genero, cantidad = albuma
                if buscar1 <= int(año) <= buscar2:
                    if ida not in resultados:
                        resultados.append(f"{ida}--{cancion}--{año}--{genero}")
                    else:
                        print
            if resultados:
                for r in resultados:
                    print(r)

                    
