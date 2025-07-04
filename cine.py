datos= {
    "F001": ["Duna 2", "Ciencia Ficcion", 6500, 6, 0],
    "F002": ["Intensamente 2", "Animacion", 4000, 8, 0],
    "F003": ["El Planeta de los Simios", "Ciencia Ficcion", 4300, 4, 0],
    "F004": ["Kung Fu Panda 4", "Animacion", 3900, 5, 0],
    "F005": ["Bad Boys 4", "Accion", 4200, 5, 0],
    "F006": ["Garfield", "Animacion", 3700, 10, 0],
    "F007": ["Furiosa", "Accion", 4500, 8, 0],
    "F008": ["El Hombre del Norte", "Drama", 4100, 7, 0],
    "F009": ["Napoleon", "Drama", 4300, 5, 0],
    "F010": ["Rescate Imposible", "Accion", 4400, 2, 0]
}
while True:
    print("\n1. Comprar Boletos")
    print("2. Ver Cantidad De Boletos Vendidso Por Genero")
    print("3. Ver Peliculas")
    print("4. Ver Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            id=input("Ingrese ID der la funcion a comprar: ").upper()
            if id in datos:
                for n,i in datos.items():
                    if id==n:
                        print(f"{i[0]},{i[1]} Boletos Vendidos: {i[3]}")
                        cantidad=int(input("Ingrese Cantidad de boletos que comprara: "))
                        datos[id][3]+=cantidad
                        print(f"Ha comprado {cantidad} boletos, ahora el total de boletos en esta pelicula es {i[3]}")
            else:
                print("No hay coincidencias")
        case 2:
            genero=input("Ingrese genero que desea buscar: ").title
            total=0
            for n,i in datos.items():
                if genero==i[1]:
                    total+=i[3]
            print(f"El total de boletos vendidos a el genero {genero} es: {total}")
        case 3:
            print("1. Ver Todas Las Peliculas")
            print("2. Ver Pelicula Por Genero")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    ordenados=sorted(datos.items(),key= lambda x:x[1][0])
                    resultados=[]
                    for n,i in ordenados:
                        if i[3]!=0:
                            resultados.append(f"{i[0]},{i[1]} Boletos Vendidos: {i[3]}")
                    if resultados:
                        for r in resultados:
                            print(r)
                    else:
                        print("No hay coincidencias")
                case 2:
                    buscar=input("Ingrese genero de pelicula").title()
                    ordenados=sorted(datos.items(),key= lambda x:x[1][0])
                    resultados=[]
                    for n,i in ordenados:
                        if i[3]!=0 and buscar==i[1]:
                            resultados.append(f"{i[0]},{i[1]} Boletos Vendidos: {i[3]}")
                    if resultados:
                        for r in resultados:
                            print(r)
                    else:
                        print("No hay coincidencias")
        case 4:
            import heapq
            print("1. Ver Peliculas Con Mas Boletos Vendidos")
            print("2. Ver Peliculas Con Mas Ganancias")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][3])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- Funcion: {n}|Pelicula: {v[0]}|Boletos Vendidos: {v[3]}")
                case 2:
                    for n,i in datos.items():
                        total=0
                        if n:
                            total=i[2]*i[3]
                            datos[n][4]+=total
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][4])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- Funcion: {n}|Pelicula: {v[0]}|Ganancias Totaless: {v[4]}")