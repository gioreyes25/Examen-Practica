datos = {
    "C001": ["Python Basico", "Programacion", 15000, 0, 2022,0],
    "C002": ["Matematica Fundamental", "Matematicas", 12000, 0, 2019,0],
    "C003": ["Ingles Basico", "Idiomas", 10000,  0, 2021,0],
    "C004": ["Diseno Grafico", "Arte", 18000,  0, 2023],
    "C005": ["Algoritmos y Estructuras", "Programacion", 17000,  0, 2018,0],
    "C006": ["Calculo I", "Matematicas", 14000,  0, 2005,0],
    "C007": ["Ingles Intermedio", "Idiomas", 13000,  0, 2015,0],
    "C008": ["Dibujo Artistico", "Arte", 16000,  0, 2020,0],
    "C009": ["Bases de Datos", "Programacion", 19000,  0, 2017,0],
    "C010": ["Algebra Lineal", "Matematicas", 15000,  0, 2003,0]
}
while True:
    print("1. Ver stock por categorias")
    print("2. Buscar por rango de años")
    print("3. Comprar Cursos")
    print("4. Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            cate=input("Ingrese categoria: ").title()
            dispo=[valor[1] for valor in datos.values()]
            total=0
            if cate in dispo:
                for n,i in datos.items():
                    if cate==i[1]:
                        total+=i[5]
                print(f"El stock de cursos de {cate} es: {total}")      
            else:
                print("No hay coincidencias")
        case 2:
            n1=int(input("Ingrese años min"))
            n2=int(input("Ingrese años max"))
            ordenados=sorted(datos.items(),key=lambda x:x[1][0])
            resultados=[]
            for n,i in ordenados:
                if n1 <= int(i[4]) <=n2:
                    resultados.append(f"{n}- |{i[0]},{i[1]}| Año: {i[4]}")
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("No hay coincidencias")
        case 3:
            id=input("Ingrese ID de curso a comprar: ").upper()
            if id in datos:
                total=0
                for n,i in datos.items():
                    if id==n:
                        print(f"{n}- |{i[0]},{i[1]}| Año: {i[4]}")
                        cantidad=int(input("Ingrese cantidad que comprara: "))
                        total=cantidad*i[2]
                        datos[n][3]+=total
                        datos[n][5]+=cantidad
                        print(f"Ha comprado {cantidad} unidades de el curso {i[0]},{i[1]} ")
            else:
                print("No hay coincidencias")
        case 4:
            import heapq
            top=heapq.nlargest(3,datos.items(),key=lambda x:x[1][3])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {n} {v[0]},{v[1]} Ganancias Totales: {v[3]}")
