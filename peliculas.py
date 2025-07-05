peliculas = {
    "M001": ["Matrix Reloaded", 2003, "Ciencia Ficcion", [3, 8, 9]],
    "M002": ["John Wick", 2014, "Accion", [4, 9, 9]],
    "M003": ["Interstellar", 2014, "Ciencia Ficcion", [7, 9, 10]],
    "M004": ["The Batman", 2022, "Accion", [8, 3, 8]],
    "M005": ["Her", 2013, "Drama", [9, 8, 10]],
    "M006": ["Inception", 2010, "Ciencia Ficcion", [5, 10, 9]],
    "M007": ["Logan", 2017, "Accion", [9, 5, 8]],
    "M008": ["The Whale", 2023, "Drama", [5, 9, 9]],
    "M009": ["Arrival", 2016, "Ciencia Ficcion", [6, 9, 9]],
    "M010": ["Joker", 2019, "Drama", [7, 10, 9]]
}

datos={}
if not datos:
    for n,i in peliculas.items():
        if n:
            promedio=(sum(i[3]))/3
            promedio=round(promedio,1)
            datos[n]=[i[0],i[1],i[2],promedio]
while True:
    print("1. Ver Peliculas")
    print("2. Buscar Pelicula por genero")
    print("3. Mostrar Top 3 Mejor Calificadas")
    print("4. Agregar Calificacion")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            n1=int(input("Ingrese un año min: "))
            n2=int(input("Ingrese un año max"))
            ordenados=sorted(datos.items(),key= lambda x:x[1][0])
            resultados=[]
            for n,i in ordenados:
                if n1 <= int(i[1]) <= n2:
                    resultados.append(f"{n}- {i[0]},{i[2]} Año: {i[1]}")
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("No hay pelicula en ese rango de años")
        case 2:
            gene=input("Ingrese genero a buscar: ").title()
            dispo=[valor[2] for valor in datos.values()]
            if gene in dispo:
                for n,i in datos.items():
                    if gene==i[2]:
                        print(f"{n}- {i[0]},{i[2]} Año: {i[1]}")
            else:
                print("No hay coincidencias")
        case 3:
            import heapq
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][3])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {v[0]},{v[2]} Año: {v[1]} Calificacion: {v[3]}")
        case 4:
            id=input("Ingrese ID de la pelicula a agregar calificacion: ").upper()
            if id in datos:
                for n,i in datos.items():
                    if id==n:
                        califi=float(input("Ingrese calificacion 1-10"))
                        if califi >10 and califi <1:
                            print("Calificacion ingresada incorrectamete")
                        else:
                            datos[n][3]+=califi
                            datos[n][3]/=2
                            print(f"Calificacion actual es: {i[3]}")