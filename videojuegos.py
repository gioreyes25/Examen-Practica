datos = {
    "V001": ["FIFA 23", 2022, "Ps5", 10],
    "V002": ["Elden Ring", 2022, "Pc", 7],
    "V003": ["Halo Infinite", 2021, "Xbox", 5],
    "V004": ["Spider-Man", 2018, "Ps5", 6],
    "V005": ["Minecraft", 2011, "Pc", 15],
    "V006": ["Forza Horizon 5", 2021, "Xbox", 8],
    "V007": ["The Last of Us", 2013, "Ps5", 0],
    "V008": ["Cyberpunk 2077", 2020, "Pc", 9],
    "V009": ["God of War Ragnarok", 2022, "Ps5", 11],
    "V010": ["Sea of Thieves", 2018, "Xbox", 6]
}
inventario = {
    "V001": [10, "Ps5"],
    "V002": [7, "PC"],
    "V003": [5, "Xbox"],
    "V004": [6, "Ps5"],
    "V005": [15, "Pc"],
    "V006": [8, "Xbox"],
    "V007": [4, "Ps5"],
    "V008": [9, "Pc"],
    "V009": [11, "Ps5"],
    "V010": [6, "Xbox"]
}
while True:
    print("1. Stock por consola")
    print("2. Buscar Videojuegos Por Rango de Años")
    print("3. Actuualizar Stock")
    print("4. Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            gene=input("Ingrese consola a buscar: ").title()
            t=0
            for n,i in inventario.items():
                if gene==i[1]:
                    t+=i[0]
            print(f"Stock de genero de {gene}: {t}")
        case 2:
            num1=int(input("Ingrese año min"))
            num2=int(input("Ingrese año max"))
            ordenados=sorted(datos.items(),key= lambda x:x[1][0])
            resultados=[]
            for id,valor in ordenados:
                video,año,consola,cantidad =valor
                if num1 <= int(año) <= num2 and cantidad!=0:
                    resultados.append(f"Videojuego: {video} Año: {año} Consola: {consola}")
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("No hay coincidencias")
        case 3:
            buscar=input("Ingrese ID para actualizar stock: ").upper()
            if buscar in datos:
                for n,i in datos.items():
                    if buscar==n:
                        print(f"{n}--{i[0]}--{i[1]}--{i[2]}--{i[3]}")
                        canti=int(input("Ingrese cantidad: "))
                        datos[n][3]+=canti
                        inventario[n][0]+=canti
                        print(f"Ha comprado {canti}u de videojuego {i[0]}")   
            else:
                print("ID Ingresado no existe")  
        case 4:
            import heapq
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][3])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {v[0]} {v[3]} unidades")              